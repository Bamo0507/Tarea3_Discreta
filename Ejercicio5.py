#----------Funciones de dispersión----------------

def hash_function(n, size):
    return n % size

def store_in_memory(data, size):
    memory = [-1] * size  # Inicializamos la memoria con -1 para indicar celdas vacías
    for number in data:
        pos = hash_function(number, size)
        original_pos = pos
        while memory[pos] != -1:  # Mientras la celda esté ocupada
            pos = (pos + 1) % size  # Vamos a la siguiente posición, y si llegamos al final volvemos al inicio
            if pos == original_pos:
                raise Exception("No hay espacio disponible para almacenar el número.")
        memory[pos] = number
    return memory

def get_memory_size():
    while True:
        try:
            size = int(input("Por favor, ingresa el tamaño de la memoria (debe ser un número entero positivo): "))
            if size <= 0:
                print("El tamaño debe ser un número entero positivo. Inténtalo de nuevo.")
            else:
                return size
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número entero.")

def get_number():
    while True:
        try:
            number = int(input("Ingresa un número mayor o igual a 0 para almacenar en la memoria: "))
            if number < 0:
                print("El número debe ser un entero positivo. Inténtalo de nuevo.")
            else:
                return number
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número entero positivo.")

#----------Programa principal----------------

print("¡Hola! Bienvenido al sistema de dispersión de datos.")
size = get_memory_size()  # Solicitamos el tamaño de la memoria solo una vez
data = []
memory_array = [-1] * size  # Inicializamos la memoria vacía

systemON = True

while systemON:
    print("\n¿Qué te gustaría hacer?")
    print("1. Ingresar un número")
    print("2. Mostrar las celdas de memoria con los datos posicionados")
    print("3. Salir")
    inputMenu = input("Selecciona una opción: ")
    
    if inputMenu == "1":
        number = get_number()
        data.append(number)
        try:
            memory_array = store_in_memory(data, size)
            print(f"Número {number} almacenado exitosamente.")
        except Exception as e:
            print(f"\nError: {e}. No se puede almacenar más números.")
            data.remove(number)  # Eliminamos el número no almacenado de la lista

    elif inputMenu == "2":
        print("\nEstado actual de la memoria:")
        print(memory_array)

    elif inputMenu == "3":
        systemON = False
        print("Finalizando el programa. ¡Hasta la próxima!")
    else:
        print("Se ha seleccionado una opción inválida. Inténtalo de nuevo.\n")
