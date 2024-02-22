class Contrato:
    def __init__(self, empleado, cantidad_aseo, cliente_nombre, cliente_identidad, precio, estado="en espera"):
        self.empleado = empleado
        self.cantidad_aseo = cantidad_aseo
        self.cliente_nombre = cliente_nombre
        self.cliente_identidad = cliente_identidad
        self.precio = precio
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        estados_permitidos = ["en espera", "en proceso", "finalizado"]
        if nuevo_estado in estados_permitidos:
            self.estado = nuevo_estado
        else:
            print("Estado no válido")

    def __str__(self):
        return f"Empleado: {self.empleado}, Cantidad de aseo: {self.cantidad_aseo}, Cliente: {self.cliente_nombre} ({self.cliente_identidad}), Precio: {self.precio}, Estado: {self.estado}"

contratos = []

def agregar_contrato():
    empleado = input("Ingrese el nombre del empleado: ")
    cantidad_aseo = float(input("Ingrese la cantidad en metros de aseo: "))
    cliente_nombre = input("Ingrese el nombre del cliente: ")
    cliente_identidad = input("Ingrese la identidad del cliente: ")
    precio = float(input("Ingrese el precio del contrato: "))
    contrato = Contrato(empleado, cantidad_aseo, cliente_nombre, cliente_identidad, precio)
    contratos.append(contrato)

def cambiar_estado_contrato():
    cliente_identidad = input("Ingrese la identidad del cliente del contrato que desea modificar: ")
    nuevo_estado = input("Ingrese el nuevo estado (en espera, en proceso, finalizado): ")
    for contrato in contratos:
        if contrato.cliente_identidad == cliente_identidad:
            contrato.cambiar_estado(nuevo_estado)
            print("Estado cambiado correctamente.")
            return
    print("Contrato no encontrado.")

def mostrar_contratos():
    for i, contrato in enumerate(contratos, start=1):
        print(f"Contrato {i}: {contrato}")

def buscar_contratos_por_estado():
    estado_busqueda = input("Ingrese el estado por el cual desea buscar los contratos (en espera, en proceso, finalizado): ")
    contratos_en_estado = [contrato for contrato in contratos if contrato.estado == estado_busqueda]
    if contratos_en_estado:
        print(f"Contratos en estado '{estado_busqueda}':")
        for i, contrato in enumerate(contratos_en_estado, start=1):
            print(f"Contrato {i}: {contrato}")
    else:
        print("No se encontraron contratos en ese estado.")

while True:
    print("\nMenú:")
    print("1. Agregar contrato")
    print("2. Cambiar estado de contrato")
    print("3. Mostrar contratos")
    print("4. Buscar contratos por estado")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_contrato()
    elif opcion == "2":
        cambiar_estado_contrato()
    elif opcion == "3":
        mostrar_contratos()
    elif opcion == "4":
        buscar_contratos_por_estado()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")