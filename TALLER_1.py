# Lista para almacenar la base de datos de personas
base_datos = []

# Lista para almacenar los textos a mostrar
mensajes = [
    "Bienvenido al directorio telefónico", 
    "Digite el Nombre y Apellido: ", 
    "Digite el Teléfono celular: ", 
    "Digite el Cumpleaños (DD/MM/AAAA): ", 
    "Digite el Correo electrónico: ",
    "1. Agregar un nuevo registro",
    "2. Buscar una persona por teléfono celular",
    "3. Borrar un registro",
    "4. Salir de la aplicación",
    "Opción no válida, intente de nuevo.",
    "Ingrese el teléfono celular a buscar: ",
    "Registro encontrado:",
    "No se encontró un registro con ese número de teléfono.",
    "Ingrese el teléfono celular a eliminar: ",
    "Registro eliminado correctamente.",
    "No se encontró un registro con ese número de teléfono para eliminar.",
    "Gracias por usar el directorio telefónico."
]

def agregar_registro():
    persona = {}
    print(mensajes[0])  # Mensaje de bienvenida
    persona["Nombre"] = input(mensajes[1])
    persona["Telefono"] = input(mensajes[2])
    persona["Cumpleanos"] = input(mensajes[3])
    persona["Correo"] = input(mensajes[4])
    base_datos.append(persona)
    print("Registro agregado exitosamente.\n")

def buscar_por_telefono():
    telefono = input(mensajes[10])
    for persona in base_datos:
        if persona["Telefono"] == telefono:
            print(mensajes[11], persona)
            return
    print(mensajes[12])

def borrar_registro():
    telefono = input(mensajes[13])
    for persona in base_datos:
        if persona["Telefono"] == telefono:
            base_datos.remove(persona)
            print(mensajes[14])
            return
    print(mensajes[15])

def menu():
    print(mensajes[0]) 
    while True:
        print("\n" + mensajes[5])
        print(mensajes[6])
        print(mensajes[7])
        print(mensajes[8])
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_registro()
        elif opcion == "2":
            buscar_por_telefono()
        elif opcion == "3":
            borrar_registro()
        elif opcion == "4":
            print(mensajes[16])
            break
        else:
            print(mensajes[9])

if __name__ == "__main__":
    menu()
