import ifcopenshell
import ifcopenshell.api
import random


def crear_data_center_bim(nombre_archivo="data_center_realista.ifc"):
    modelo = ifcopenshell.api.run("project.create_file")
    proyecto = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcProject", name="Data Center Realista")

    # Crear contexto geométrico
    contexto_geom = modelo.create_entity(
        "IfcGeometricRepresentationContext",
        ContextType="Model",
        ContextIdentifier="Building",
        Precision=1e-5,
        WorldCoordinateSystem=modelo.create_entity(
            "IfcAxis2Placement3D",
            Location=modelo.create_entity("IfcCartesianPoint", Coordinates=[0.0, 0.0, 0.0]),
        ),
    )
    proyecto.RepresentationContexts = [contexto_geom]

    # Configurar las unidades del modelo
    unit_assignment = modelo.create_entity("IfcUnitAssignment")
    length_unit = modelo.create_entity("IfcSIUnit", UnitType="LENGTHUNIT", Name="METRE")
    unit_assignment.Units = [length_unit]
    proyecto.UnitsInContext = unit_assignment

    # Crear sitio y edificio
    sitio = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcSite", name="Sitio del Data Center")
    ifcopenshell.api.run("aggregate.assign_object", modelo, relating_object=proyecto, products=[sitio])
    edificio = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcBuilding", name="Edificio Principal")
    ifcopenshell.api.run("aggregate.assign_object", modelo, relating_object=sitio, products=[edificio])

    # Crear niveles
    nivel = ifcopenshell.api.run(
        "root.create_entity", modelo, ifc_class="IfcBuildingStorey", name="Nivel 0"
    )
    nivel.Elevation = 0.0
    ifcopenshell.api.run("aggregate.assign_object", modelo, relating_object=edificio, products=[nivel])

    def generar_color():
        """Generar un color aleatorio."""
        return [random.uniform(0.3, 0.7) for _ in range(3)]

    def crear_placement(location):
        punto = modelo.create_entity("IfcCartesianPoint", Coordinates=[float(coord) for coord in location])
        direccion_z = modelo.create_entity("IfcDirection", DirectionRatios=[0.0, 0.0, 1.0])
        direccion_x = modelo.create_entity("IfcDirection", DirectionRatios=[1.0, 0.0, 0.0])
        placement_3d = modelo.create_entity("IfcAxis2Placement3D", Location=punto, Axis=direccion_z, RefDirection=direccion_x)
        placement = modelo.create_entity("IfcLocalPlacement", RelativePlacement=placement_3d)
        return placement

    def agregar_representacion_geometrica(modelo, producto, dimensiones, color):
        punto = modelo.create_entity("IfcCartesianPoint", Coordinates=[0.0, 0.0])
        perfil = modelo.create_entity(
            "IfcRectangleProfileDef",
            ProfileType="AREA",
            XDim=dimensiones[0],
            YDim=dimensiones[1],
            Position=modelo.create_entity("IfcAxis2Placement2D", Location=punto),
        )
        extrude_direction = modelo.create_entity("IfcDirection", DirectionRatios=[0.0, 0.0, 1.0])
        solid = modelo.create_entity(
            "IfcExtrudedAreaSolid",
            SweptArea=perfil,
            ExtrudedDirection=extrude_direction,
            Depth=dimensiones[2],
        )
        shape_rep = modelo.create_entity(
            "IfcShapeRepresentation",
            ContextOfItems=contexto_geom,
            RepresentationIdentifier="Body",
            RepresentationType="SweptSolid",
            Items=[solid],
        )
        rep = modelo.create_entity("IfcProductDefinitionShape", Representations=[shape_rep])
        producto.Representation = rep

    def crear_pared(modelo, nivel, posicion, dimensiones):
        pared = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcWall", name="Pared")
        placement = crear_placement(posicion)
        pared.ObjectPlacement = placement
        agregar_representacion_geometrica(modelo, pared, dimensiones, generar_color())
        ifcopenshell.api.run("spatial.assign_container", modelo, relating_structure=nivel, products=[pared])

    def crear_piso_techo(modelo, nivel, posicion, dimensiones, nombre):
        slab = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcSlab", name=nombre)
        placement = crear_placement(posicion)
        slab.ObjectPlacement = placement
        agregar_representacion_geometrica(modelo, slab, dimensiones, generar_color())
        ifcopenshell.api.run("spatial.assign_container", modelo, relating_structure=nivel, products=[slab])

    def crear_puerta(modelo, nivel, posicion):
        puerta = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcDoor", name="Puerta")
        placement = crear_placement(posicion)
        puerta.ObjectPlacement = placement
        agregar_representacion_geometrica(modelo, puerta, [1.0, 0.1, 2.0], generar_color())
        ifcopenshell.api.run("spatial.assign_container", modelo, relating_structure=nivel, products=[puerta])

    def crear_ventana(modelo, nivel, posicion):
        ventana = ifcopenshell.api.run("root.create_entity", modelo, ifc_class="IfcWindow", name="Ventana")
        placement = crear_placement(posicion)
        ventana.ObjectPlacement = placement
        agregar_representacion_geometrica(modelo, ventana, [2.0, 0.1, 1.5], generar_color())
        ifcopenshell.api.run("spatial.assign_container", modelo, relating_structure=nivel, products=[ventana])

    # Salas y elementos
    dimensiones_piso = [10.0, 8.0, 0.5]
    crear_piso_techo(modelo, nivel, [0.0, 0.0, -0.5], dimensiones_piso, "Piso General")
    crear_piso_techo(modelo, nivel, [0.0, 0.0, 3.5], dimensiones_piso, "Techo General")
    crear_pared(modelo, nivel, [0.0, -4.0, 0.0], [10.0, 0.5, 4.0])  # Wall 1
    crear_puerta(modelo, nivel, [0.0, -3.0, 0.0])  # Door Example
    crear_ventana(modelo, nivel, [0.0, 4.0, 2.0])  # Window Example

    modelo.write(nombre_archivo)
    print(f"Archivo IFC creado: {nombre_archivo}")


if __name__ == "__main__":
    crear_data_center_bim()
