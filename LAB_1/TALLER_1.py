# Lista para almacenar la información de las personas
directorio = []

# Lista para almacenar los textos que se mostrarán en pantalla
mensajes = [
    "Bienvenido al directorio telefónico.",
    "Digite el nombre y apellido de la persona: ",
    "Digite el teléfono celular de la persona: ",
    "Digite el cumpleaños de la persona (DD/MM/AAAA): ",
    "Digite el correo electrónico de la persona: ",
    "Registro agregado exitosamente.",
    "No se encontró ninguna persona con ese teléfono.",
    "Registro eliminado exitosamente.",
    "Saliendo del programa...",
    "Opción no válida, por favor intente de nuevo.",
    "El número de teléfono debe tener exactamente 10 dígitos."
]

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar un nuevo registro")
    print("2. Buscar una persona por teléfono celular")
    print("3. Borrar un registro")
    print("4. Salir de la aplicación")

# Función para validar el número de teléfono
def validar_telefono(telefono):
    # Verifica si el teléfono tiene exactamente 10 dígitos y es un número
    return telefono.isdigit() and len(telefono) == 10

# Función para agregar un nuevo registro
def agregar_registro():
    persona = {}
    print(mensajes[1])
    persona['nombre'] = input()
    
    # Validación del número de teléfono
    while True:
        print(mensajes[2])
        telefono = input()
        if validar_telefono(telefono):
            persona['telefono'] = int(telefono)
            break
        else:
            print(mensajes[10])  # Mensaje de error: teléfono no válido
    
    print(mensajes[3])
    persona['cumpleanos'] = input()
    print(mensajes[4])
    persona['correo'] = input()
    
    directorio.append(persona)
    print(mensajes[5])  # Mensaje de confirmación: registro agregado

# Función para buscar una persona por teléfono
def buscar_por_telefono():
    while True:
        print("Digite el teléfono celular a buscar: ")
        telefono = input()
        if validar_telefono(telefono):
            telefono = int(telefono)
            break
        else:
            print(mensajes[10])  # Mensaje de error: teléfono no válido
    
    for persona in directorio:
        if persona['telefono'] == telefono:
            print(f"Nombre: {persona['nombre']}")
            print(f"Teléfono: {persona['telefono']}")
            print(f"Cumpleaños: {persona['cumpleanos']}")
            print(f"Correo: {persona['correo']}")
            return
    print(mensajes[6])  # Mensaje de error: no se encontró el teléfono

# Función para borrar un registro
def borrar_registro():
    while True:
        print("Digite el teléfono celular del registro a borrar: ")
        telefono = input()
        if validar_telefono(telefono):
            telefono = int(telefono)
            break
        else:
            print(mensajes[10])  # Mensaje de error: teléfono no válido
    
    for persona in directorio:
        if persona['telefono'] == telefono:
            directorio.remove(persona)
            print(mensajes[7])  # Mensaje de confirmación: registro eliminado
            return
    print(mensajes[6])  # Mensaje de error: no se encontró el teléfono

# Función principal
def main():
    print(mensajes[0])  # Mensaje de bienvenida
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        # Validación de la opción del menú
        if opcion in ['1', '2', '3', '4']:
            if opcion == '1':
                agregar_registro()
            elif opcion == '2':
                buscar_por_telefono()
            elif opcion == '3':
                borrar_registro()
            elif opcion == '4':
                print(mensajes[8])  # Mensaje de despedida
                break
        else:
            print(mensajes[9])  # Mensaje de error: opción no válida

# Ejecutar el programa
if __name__ == "__main__":
    main()