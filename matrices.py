# Guillermo Jair Montiel Juárez
# Actividad Complementaria 3 - Unidad 3
# Programa para sumar y restar dos matrices de dimensiones N x M.

def obtener_dimensiones():
    """
    Esta función pide al usuario las dimensiones (filas y columnas) para las matrices.
    Se valida que los valores ingresados sean números enteros positivos.
    """
    print("\n--- PASO 1: Ingresar dimensiones de las matrices ---")
    while True: # Bucle infinito hasta que se obtengan datos válidos.
        try:
            # Se pide el número de filas y se convierte a entero.
            filas = int(input("Introduce el número de FILAS: "))
            # Se pide el número de columnas y se convierte a entero.
            columnas = int(input("Introduce el número de COLUMNAS: "))
            
            # Las matrices no pueden tener 0 o menos filas/columnas.
            if filas > 0 and columnas > 0:
                # Si los datos son correctos, se devuelven.
                return filas, columnas
            else:
                print("Error: El número de filas y columnas debe ser mayor que cero.")
        except ValueError:
            # Si el usuario introduce algo que no es un número, se muestra un error.
            print("Error: Por favor, introduce solo números enteros.")

def leer_matriz(nombre_matriz, filas, columnas):
    """
    Esta función lee los valores para una matriz, solicitándolos al usuario.
    Recibe el nombre de la matriz ('A' o 'B') y sus dimensiones.
    Devuelve la matriz como una lista de listas.
    """
    print(f"\n--- PASO 2: Ingresar valores para la Matriz {nombre_matriz} ---")
    matriz = []
    # Se recorre cada fila de la matriz.
    for i in range(filas):
        # Se crea una lista vacía para guardar los elementos de la fila actual.
        fila_actual = []
        # Se recorre cada columna de la fila actual.
        for j in range(columnas):
            while True:
                try:
                    # Se pide al usuario el valor para la posición [fila][columna].
                    valor = int(input(f"Introduce el valor para {nombre_matriz}[{i+1}][{j+1}]: "))
                    # Se agrega el valor a la lista de la fila.
                    fila_actual.append(valor)
                    # Se sale del bucle de validación si el dato es correcto.
                    break
                except ValueError:
                    # Si el dato no es un número, se pide que se ingrese de nuevo.
                    print("Error: Por favor, introduce solo números enteros.")
        # Se agrega la fila completa a la matriz.
        matriz.append(fila_actual)
    return matriz

def sumar_matrices(matriz_a, matriz_b, filas, columnas):
    """
    Esta función suma dos matrices (A y B) y devuelve la matriz resultante (C).
    La lógica consiste en crear una nueva matriz vacía y llenarla con la suma
    de los elementos de A y B en la misma posición.
    """
    matriz_c = []
    # Se recorren las filas.
    for i in range(filas):
        fila_resultado = []
        # Se recorren las columnas.
        for j in range(columnas):
            # Se suman los elementos que están en la misma posición (i, j).
            suma = matriz_a[i][j] + matriz_b[i][j]
            # Se agrega el resultado a la nueva fila.
            fila_resultado.append(suma)
        # Se agrega la fila con los resultados a la matriz final.
        matriz_c.append(fila_resultado)
    return matriz_c

def restar_matrices(matriz_a, matriz_b, filas, columnas):
    """
    Esta función resta dos matrices (A y B) y devuelve la matriz resultante (D).
    Funciona igual que la suma, pero con el operador de resta.
    """
    matriz_d = []
    # Se recorren las filas.
    for i in range(filas):
        fila_resultado = []
        # Se recorren las columnas.
        for j in range(columnas):
            # Se restan los elementos que están en la misma posición (i, j).
            resta = matriz_a[i][j] - matriz_b[i][j]
            # Se agrega el resultado a la nueva fila.
            fila_resultado.append(resta)
        # Se agrega la fila con los resultados a la matriz final.
        matriz_d.append(fila_resultado)
    return matriz_d

def imprimir_matriz(nombre_matriz, matriz):
    """
    Esta función imprime una matriz en la consola de forma ordenada y legible.
    """
    print(f"\n--- Matriz {nombre_matriz} ---")
    # Se recorre cada fila de la matriz.
    for fila in matriz:
        # Se imprime cada elemento de la fila, separado por un tabulador.
        for elemento in fila:
            print(elemento, end="\t")
        # Después de imprimir todos los elementos de una fila, se hace un salto de línea.
        print()

# --- Inicio de la ejecución del programa ---

print("Bienvenido al programa de operaciones con matrices.")

# Bucle principal para permitir repetir la operación.
while True:
    print("\nPara poder sumar y restar, ambas matrices deben tener las mismas dimensiones.")
    
    # 1. Se obtienen las dimensiones que tendrán las matrices.
    filas, columnas = obtener_dimensiones()
    
    # 2. Se leen los valores para la Matriz A y la Matriz B.
    matriz_a = leer_matriz("A", filas, columnas)
    matriz_b = leer_matriz("B", filas, columnas)
    
    # 3. Se muestran las matrices originales ingresadas por el usuario.
    imprimir_matriz("A (ingresada)", matriz_a)
    imprimir_matriz("B (ingresada)", matriz_b)
    
    # 4. Se calcula la suma y se muestra el resultado.
    matriz_suma_c = sumar_matrices(matriz_a, matriz_b, filas, columnas)
    imprimir_matriz("C = A + B", matriz_suma_c)
    
    # 5. Se calcula la resta y se muestra el resultado.
    matriz_resta_d = restar_matrices(matriz_a, matriz_b, filas, columnas)
    imprimir_matriz("D = A - B", matriz_resta_d)
    
    # 6. Se pregunta al usuario si desea continuar.
    respuesta = input("\n¿Deseas realizar otra operación? (s/n): ").lower().strip()
    
    # Si la respuesta no es 's', se rompe el bucle.
    if respuesta != 's':
        break

print("\n¡Gracias por usar el programa! Finalizando...")