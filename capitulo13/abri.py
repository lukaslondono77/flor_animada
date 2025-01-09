import ifcopenshell
import vtk


def visualizar_ifc(nombre_archivo):
    # Leer el archivo IFC
    modelo = ifcopenshell.open(nombre_archivo)

    # Crear ventana de renderizado
    render_window = vtk.vtkRenderWindow()
    render_window.SetSize(800, 600)

    # Interactor de renderizado
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Renderizador
    renderer = vtk.vtkRenderer()
    render_window.AddRenderer(renderer)

    # Configurar iluminación
    luz = vtk.vtkLight()
    luz.SetLightTypeToSceneLight()
    luz.SetPosition(10, 10, 10)  # Posición de la luz
    luz.SetFocalPoint(0, 0, 0)  # Donde apunta la luz
    luz.SetColor(1.0, 1.0, 1.0)  # Luz blanca
    luz.SetIntensity(1.0)  # Intensidad de la luz
    renderer.AddLight(luz)

    # Iterar por las entidades del modelo y crear geometría básica
    for entity in modelo.by_type("IfcProduct"):
        if not entity.Representation:
            continue

        # Crear un cubo como representación genérica (puedes usar más geometría específica)
        cube = vtk.vtkCubeSource()
        cube.SetXLength(2)
        cube.SetYLength(2)
        cube.SetZLength(2)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(cube.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Ajustar posición
        if entity.ObjectPlacement:
            placement = entity.ObjectPlacement.RelativePlacement.Location.Coordinates
            actor.SetPosition(*placement)

        renderer.AddActor(actor)

    # Configuración del renderizador
    renderer.SetBackground(0.2, 0.2, 0.2)  # Color de fondo (gris oscuro)
    render_window.Render()

    # Iniciar interacción
    interactor.Start()


if __name__ == "__main__":
    # Cambiar el nombre del archivo si es necesario
    visualizar_ifc("data_center_bim.ifc")
