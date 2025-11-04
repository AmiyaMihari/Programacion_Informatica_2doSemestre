# Guillermo Jair Montiel Juárez
# Unidad 4 - Actividad Complementaria 3

# comparacionArchivos.py
# Programa para comparar el contenido de dos archivos de texto línea por línea.


# Importar el módulo sys para manejo de excepciones y salida del programa
import sys

def pedir_nombres_archivos():
    """
    Solicita al usuario los nombres de los dos archivos que se van a comparar.
    Retorna una tupla con ambos nombres.
    """
    print("--- Comparador de Archivos ---")
    nombre1 = input("Introduce el nombre del primer archivo (ej. archivo1.txt): ")
    nombre2 = input("Introduce el nombre del segundo archivo (ej. archivo2.txt): ")
    return nombre1, nombre2

def leer_archivos(nombre1, nombre2):
    """
    Intenta abrir y leer el contenido de ambos archivos.
    Maneja excepciones si los archivos no se encuentran.
    Retorna dos listas, cada una con las líneas de un archivo.
    """
    try:
        # Se abre el primer archivo en modo lectura
        with open(nombre1, 'r', encoding='utf-8') as f1:
            # Se leen todas las líneas y se guardan en una lista
            lineas_f1 = f1.readlines()

        # Se abre el segundo archivo en modo lectura
        with open(nombre2, 'r', encoding='utf-8') as f2:
            lineas_f2 = f2.readlines()

        # Se prepara una lista limpia para el archivo 1, eliminando saltos de línea
        lineas_limpias1 = []
        for linea in lineas_f1:
            lineas_limpias1.append(linea.strip())

        # Se prepara una lista limpia para el archivo 2
        lineas_limpias2 = []
        for linea in lineas_f2:
            lineas_limpias2.append(linea.strip())

        return lineas_limpias1, lineas_limpias2

    except FileNotFoundError as e:
        # Manejo de error si un archivo no existe
        print(f"Error: No se pudo encontrar el archivo '{e.filename}'.")
        return None, None
    except Exception as e:
        # Manejo de otros posibles errores de lectura
        print(f"Ocurrió un error inesperado al leer los archivos: {e}")
        return None, None

def comparar_listas_lineas(lineas1, lineas2):
    """
    Compara las dos listas de líneas (una por cada archivo).
    Genera una lista de cadenas que describe las diferencias.
    """
    # Lista para almacenar los mensajes de diferencias
    diferencias = []
    
    # Se obtiene la cantidad de líneas de cada archivo
    len1 = len(lineas1)
    len2 = len(lineas2)
    
    # Se usa la longitud máxima para asegurar que se recorran todas las líneas
    max_len = max(len1, len2)

    # Se inicia la iteración comparativa línea por línea
    for i in range(max_len):
        numero_linea = i + 1

        # Caso 1: La línea existe en ambos archivos
        if i < len1 and i < len2:
            # Se comparan las líneas en la misma posición
            if lineas1[i] != lineas2[i]:
                # Se registra la discrepancia si son diferentes
                diferencias.append(f"\n[Línea {numero_linea} es diferente]")
                diferencias.append(f"  -> Archivo 1: '{lineas1[i]}'")
                diferencias.append(f"  -> Archivo 2: '{lineas2[i]}'")
        
        # Caso 2: La línea solo existe en el archivo 1 (archivo 1 es más largo)
        elif i < len1:
            diferencias.append(f"\n[Línea {numero_linea} solo existe en el Archivo 1]")
            diferencias.append(f"  -> Archivo 1: '{lineas1[i]}'")
        
        # Caso 3: La línea solo existe en el archivo 2 (archivo 2 es más largo)
        elif i < len2:
            diferencias.append(f"\n[Línea {numero_linea} solo existe en el Archivo 2]")
            diferencias.append(f"  -> Archivo 2: '{lineas2[i]}'")
            
    return diferencias

def mostrar_reporte(diferencias, nombre1, nombre2):
    """
    Imprime en consola el informe final de la comparación.
    """
    print("\n--- INFORME DE COMPARACIÓN ---")
    print(f"Archivo 1: {nombre1}")
    print(f"Archivo 2: {nombre2}")
    
    # Se comprueba si la lista de diferencias está vacía
    if not diferencias:
        print("\nResultado: Los archivos son idénticos.")
    else:
        print("\nResultado: Se encontraron las siguientes diferencias:")
        # Se itera sobre la lista de diferencias y se imprime cada una
        for d in diferencias:
            print(d)
    
    print("----------------------------------\n")

# --- Bucle principal de ejecución ---

continuar = 's'
while continuar.lower() == 's':
    
    # Paso 1: Obtener los nombres de los archivos
    nombre_f1, nombre_f2 = pedir_nombres_archivos()

    # Paso 2: Leer el contenido de los archivos
    lineas_f1, lineas_f2 = leer_archivos(nombre_f1, nombre_f2)

    # Se valida que la lectura de archivos haya sido exitosa
    if lineas_f1 is not None and lineas_f2 is not None:
        
        # Paso 3: Comparar las líneas
        reporte_diferencias = comparar_listas_lineas(lineas_f1, lineas_f2)
        
        # Paso 4: Mostrar el reporte al usuario
        mostrar_reporte(reporte_diferencias, nombre_f1, nombre_f2)

    # Se pregunta al usuario si desea realizar otra comparación
    continuar = input("¿Deseas comparar otros archivos? (s/n): ")

print("Hasta luego!")