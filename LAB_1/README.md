# LABORATORIO 1
## Integrantes
[Sebastian Camilo Martinez Gonzalez](https://github.com/SebasMtz30)

# Directorio Telefónico en Python
## Descripción del Programa
Este programa es una aplicación de consola en Python que permite gestionar un directorio telefónico. Los usuarios pueden agregar, buscar y eliminar registros de personas, almacenando información como:

- Nombre y apellido

- Teléfono celular

- Cumpleaños

- Correo electrónico

El programa utiliza listas para almacenar los registros y diccionarios para estructurar la información de cada persona. Además, se emplean mensajes predefinidos para guiar al usuario durante la ejecución.

## Estructura del Código
El programa está organizado en las siguientes partes:

1. Listas:

- directorio: Almacena los registros de las personas (cada registro es un diccionario).

- mensajes: Contiene los textos que se muestran en pantalla (bienvenida, solicitudes de datos, confirmaciones, etc.).

2. Funciones:

- mostrar_menu(): Muestra un menú con las opciones disponibles.

- agregar_registro(): Permite al usuario agregar un nuevo registro al directorio.

- buscar_por_telefono(): Busca una persona por su número de teléfono y muestra su información.

- borrar_registro(): Elimina un registro basado en el número de teléfono.

- main(): Función principal que controla el flujo del programa.

3. Flujo del Programa:

- El programa inicia mostrando un mensaje de bienvenida.

- Luego, se muestra un menú con las opciones: agregar, buscar, borrar y salir.

- Dependiendo de la opción seleccionada, el programa ejecuta la función correspondiente.

## Detalles Adicionales
- Persistencia de Datos: Los datos se almacenan en memoria (en una lista) durante la ejecución del programa. Si se cierra el programa, los datos se pierden. Para una versión más avanzada, se podrían guardar los datos en un archivo (por ejemplo, JSON o CSV).

- Validaciones: El programa no incluye validaciones avanzadas (por ejemplo, verificar si el teléfono ya existe o si el correo tiene un formato válido). Esto se podría implementar en futuras versiones.

- Interfaz de Usuario: El programa es una aplicación de consola, por lo que no tiene una interfaz gráfica. Sin embargo, es fácil de usar y sigue un flujo claro.

## Cómo se Podría Emplear en la Vida Real
Este programa es útil en situaciones donde se necesita gestionar un pequeño directorio de contactos de manera rápida y sencilla. Algunos casos de uso podrían ser:

1. Uso Personal:

- Mantener un registro de contactos personales (familiares, amigos, colegas).

- Buscar rápidamente el número de teléfono o correo de una persona.

2. Pequeñas Empresas:

- Gestionar los contactos de clientes o proveedores.

- Tener a mano la información de contacto clave para comunicarse rápidamente.

- Eventos o Comunidades:

- Mantener un directorio de participantes en un evento, taller o comunidad.

- Facilitar la comunicación entre los miembros.

3. Educación:

- Como herramienta de aprendizaje para estudiantes que están comenzando a programar en Python.

- Ejemplo práctico de cómo usar listas, diccionarios y funciones en un proyecto real.

## Ejemplo de Uso en la Vida Real
Imagina que eres el organizador de un evento y necesitas mantener un registro de los participantes. Con este programa, podrías:

- Agregar a cada participante con su nombre, teléfono, cumpleaños y correo.

- Buscar rápidamente a un participante por su número de teléfono si necesitas contactarlo.

- Eliminar a un participante si ya no asistirá al evento.

- Este tipo de herramienta es especialmente útil cuando no se tiene acceso a software más complejo (como una base de datos) y se necesita una solución rápida y eficiente.

## Conclusión
Este programa es un ejemplo sencillo pero efectivo de cómo se pueden utilizar listas y diccionarios en Python para resolver problemas del mundo real. Aunque es básico, puede ser ampliado con funcionalidades adicionales (como guardar los datos en un archivo o agregar validaciones) para adaptarse a necesidades más específicas.

