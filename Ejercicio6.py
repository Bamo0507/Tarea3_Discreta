#----------Función para generar números pseudoaleatorios----------------

def generar_pseudoaleatorios(m, a, c, s, n):
    secuencia = []
    x = s
    for i in range(n):
        x = (a * x + c) % m
        print(f"Iteración {i+1}: x = {x}")  # Debug: Muestra el valor de x en cada iteración
        secuencia.append(x)
    return secuencia


#----------Funciones para validación de entradas----------------

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                return value
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número entero positivo.")

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número entero.")

def get_valid_a(m):
    while True:
        a = get_positive_integer("Ingresa el valor de a (multiplicador): ")
        if 2 <= a < m:
            return a
        else:
            print(f"El valor de a debe estar entre 2 y {m-1}. Inténtalo de nuevo.")

#-------------Programa principal----------------

print("¡Hola! Bienvenido al generador de números pseudoaleatorios.")
systemON = True

while systemON:
    print("\n¿Qué te gustaría hacer?")
    print("1. Configurar parámetros y generar secuencia")
    print("2. Salir")
    inputMenu = input("Selecciona una opción: ")
    
    if inputMenu == "1":
        print("\nPara generar una secuencia de números pseudoaleatorios, necesitas configurar los siguientes parámetros:")
        print("1. m (módulo): El valor máximo que puede tomar cada número generado. Generalmente es un número grande, y define el rango de la secuencia.")
        print("2. a (multiplicador): Un valor que se utiliza para multiplicar el número generado en cada iteración. Afecta cómo se distribuyen los números en la secuencia.")
        print("3. c (incremento): Un valor constante que se suma en cada iteración. Puede ser positivo, negativo o cero. Introduce un sesgo adicional en la secuencia.")
        print("4. s (semilla): El valor inicial a partir del cual se empieza a generar la secuencia. Es esencial para la repetibilidad de la secuencia.")
        print("5. n (cantidad de números): La cantidad de números pseudoaleatorios que deseas generar en la secuencia.")
        
        m = get_positive_integer("\nIngresa el valor de m (modulo): ")
        a = get_valid_a(m)
        c = get_integer("Ingresa el valor de c (incremento): ")
        s = get_positive_integer("Ingresa el valor de s (semilla): ")
        n = get_positive_integer("Ingresa la cantidad de números a generar: ")

        secuencia = generar_pseudoaleatorios(m, a, c, s, n)
        print("\nSecuencia de números pseudoaleatorios generada:")
        print(secuencia)

    elif inputMenu == "2":
        systemON = False
        print("Finalizando el programa. ¡Hasta la próxima!")
    else:
        print("Se ha seleccionado una opción inválida. Inténtalo de nuevo.\n")
