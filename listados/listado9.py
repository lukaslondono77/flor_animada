import vtk


def crear_data_center_dos_plantas():
    # Ventana de renderizado
    render_window = vtk.vtkRenderWindow()
    render_window.SetSize(1200, 800)

    # Interactor de renderizado
    render_interactor = vtk.vtkRenderWindowInteractor()
    render_interactor.SetRenderWindow(render_window)

    # Renderizador
    renderer = vtk.vtkRenderer()
    render_window.AddRenderer(renderer)

    # Función para crear un cubo (genérico para racks, paredes, etc.)
    def crear_cubo(posicion, tamano, color, opacidad=1.0):
        cubo = vtk.vtkCubeSource()
        cubo.SetXLength(tamano[0])
        cubo.SetYLength(tamano[1])
        cubo.SetZLength(tamano[2])
        cubo.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(cubo.GetOutput())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(color)
        actor.GetProperty().SetOpacity(opacidad)
        actor.SetPosition(posicion)
        return actor

    # Función para crear un cilindro orientado
    def crear_cilindro(posicion, radio, altura, direccion, color):
        cilindro = vtk.vtkCylinderSource()
        cilindro.SetRadius(radio)
        cilindro.SetHeight(altura)
        cilindro.SetResolution(50)
        cilindro.Update()

        # Transformar el cilindro para orientarlo
        transform = vtk.vtkTransform()
        if direccion == (1, 0, 0):  # Horizontal en X
            transform.RotateZ(90)
        elif direccion == (0, 0, 1):  # Horizontal en Z
            transform.RotateX(90)

        transform.Translate(posicion)

        transform_filter = vtk.vtkTransformPolyDataFilter()
        transform_filter.SetInputData(cilindro.GetOutput())
        transform_filter.SetTransform(transform)
        transform_filter.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(transform_filter.GetOutput())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(color)
        return actor

    # Crear piso del data center
    piso = crear_cubo(posicion=(0, -0.5, 0), tamano=(50, 1, 50), color=(0.5, 0.5, 0.5))
    renderer.AddActor(piso)

    # Crear la estructura del segundo piso
    piso_intermedio = crear_cubo(posicion=(0, 10.5, 0), tamano=(50, 1, 50), color=(0.4, 0.4, 0.4), opacidad=0.9)
    renderer.AddActor(piso_intermedio)

    # Racks de servidores en ambas plantas
    for planta, altura_base in enumerate([0, 11]):  # Planta baja y primera planta
        for x in range(-20, 21, 10):  # Filas de racks
            for z in range(-20, 21, 10):  # Columnas de racks
                rack = crear_cubo(posicion=(x, altura_base + 5, z), tamano=(2, 10, 4), color=(0, 0, 0.8))
                renderer.AddActor(rack)

    # Tuberías horizontales (refrigeración) en ambas plantas
    for planta, altura_base in enumerate([0, 11]):
        for z in range(-20, 25, 10):  # Cada fila de racks
            tuberia_h = crear_cilindro(posicion=(0, altura_base + 11, z), radio=0.3, altura=50, direccion=(1, 0, 0), color=(0.8, 0, 0))
            renderer.AddActor(tuberia_h)

    # Tuberías verticales (conexión entre plantas)
    for x in range(-20, 25, 10):  # Cada columna de racks
        tuberia_v = crear_cilindro(posicion=(x, 5, 25), radio=0.3, altura=20, direccion=(0, 1, 0), color=(0.8, 0, 0))
        renderer.AddActor(tuberia_v)

    # Bandejas de cableado en ambas plantas
    for planta, altura_base in enumerate([0, 11]):
        for x in range(-20, 25, 10):  # Cada fila de racks
            bandeja = crear_cubo(posicion=(x, altura_base + 11, 0), tamano=(2, 0.5, 50), color=(1, 0.8, 0.2), opacidad=0.8)
            renderer.AddActor(bandeja)

    # Cables colgando de las bandejas
    for planta, altura_base in enumerate([0, 11]):
        for x in range(-20, 25, 10):  # Cada fila de racks
            for z in range(-20, 25, 10):  # Cada rack
                cable = crear_cilindro(posicion=(x, altura_base + 7, z), radio=0.05, altura=4, direccion=(0, 1, 0), color=(0, 0, 0))
                renderer.AddActor(cable)

    # Escaleras entre plantas
    escalera = crear_cubo(posicion=(25, 6, -20), tamano=(5, 12, 5), color=(0.5, 0.3, 0.2), opacidad=0.8)
    renderer.AddActor(escalera)

    # Paredes transparentes
    paredes = [
        crear_cubo(posicion=(0, 5, -25), tamano=(50, 10, 1), color=(1, 1, 1), opacidad=0.3),  # Pared trasera
        crear_cubo(posicion=(0, 15, 25), tamano=(50, 10, 1), color=(1, 1, 1), opacidad=0.3),  # Pared delantera
        crear_cubo(posicion=(-25, 10, 0), tamano=(1, 20, 50), color=(1, 1, 1), opacidad=0.3),  # Pared izquierda
        crear_cubo(posicion=(25, 10, 0), tamano=(1, 20, 50), color=(1, 1, 1), opacidad=0.3),  # Pared derecha
    ]
    for pared in paredes:
        renderer.AddActor(pared)

    # Configuración de la cámara
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(45)
    renderer.GetActiveCamera().Elevation(30)
    renderer.GetActiveCamera().Dolly(1.5)
    renderer.ResetCameraClippingRange()

    # Fondo del renderizador
    renderer.SetBackground(0.1, 0.1, 0.1)  # Fondo oscuro

    # Iniciar renderizado
    render_window.Render()
    render_interactor.Start()


if __name__ == "__main__":
    crear_data_center_dos_plantas()
