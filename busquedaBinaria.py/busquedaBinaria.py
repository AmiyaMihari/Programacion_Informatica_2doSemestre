# Guillermo Jair Montiel Juárez
# Unidad 5 - Actividad Complementaria 1

# Programa que realiza búsquedas secuencial y binaria

# time permite medir el tiempo de ejecución de las búsquedas
import time

def cargar_datos(nombre_archivo):
    """
    Carga el archivo de texto en la memoria, convirtiendo cada línea
    en un diccionario. Esto es un ejemplo de abstracción de datos estructurada.
    Asume que el archivo está ordenado por 'id'.
    """
    registros = []
    try:
        with open(nombre_archivo, 'r', encoding='latin-1') as f:
            # Se lee la primera línea para obtener los encabezados
            encabezados = f.readline().strip().split('\t')
            
            # Se itera sobre el resto del archivo
            for linea in f:
                valores = linea.strip().split('\t')
                
                # Se crea un diccionario (abstracción) para el registro
                registro_dic = {}
                for i in range(len(encabezados)):
                    registro_dic[encabezados[i]] = valores[i]
                
                # Conversión de tipos de dato para búsquedas
                try:
                    registro_dic['id'] = int(registro_dic['id'])
                    registro_dic['sueldo_issste'] = float(registro_dic['sueldo_issste'])
                except ValueError:
                    print(f"Error: No se pudo convertir un valor en la línea: {linea}")
                    continue
                
                registros.append(registro_dic)
                
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None
        
    print(f"Se cargaron {len(registros)} registros en memoria.")
    return registros

def busqueda_secuencial(registros, id_buscado):
    """
    Realiza una búsqueda secuencial (lineal) sobre la lista de registros.
    Esta función es una abstracción de control estructurada.
    """
    # Se inician los contadores
    inicio_tiempo = time.perf_counter()
    condiciones = 0
    
    # Se itera registro por registro desde el inicio
    for registro in registros:
        # Se cuenta cada comparación de ID
        condiciones += 1
        if registro['id'] == id_buscado:
            # Se detiene el tiempo al encontrar
            fin_tiempo = time.perf_counter()
            tiempo_total = fin_tiempo - inicio_tiempo
            # Se retorna el resultado
            return (registro, condiciones, tiempo_total)
            
    # Si el bucle termina, no se encontró
    fin_tiempo = time.perf_counter()
    tiempo_total = fin_tiempo - inicio_tiempo
    return (None, condiciones, tiempo_total)

def busqueda_binaria(registros, id_buscado):
    """
    Realiza una búsqueda binaria sobre la lista de registros.
    Esta función es una abstracción de control estructurada.
    """
    # Glosario
    # bajo: índice inferior del rango de búsqueda
    # alto: índice superior del rango de búsqueda
    # medio: índice medio del rango de búsqueda

    # Se inician los contadores y punteros
    inicio_tiempo = time.perf_counter()
    condiciones = 0
    bajo = 0
    alto = len(registros) - 1
    
    # El bucle se ejecuta mientras el rango de búsqueda sea válido
    while bajo <= alto:
        medio = (bajo + alto) // 2
        id_medio = registros[medio]['id']
        
        # Se cuenta la primera condición (igualdad)
        condiciones += 1
        if id_medio == id_buscado:
            fin_tiempo = time.perf_counter()
            tiempo_total = fin_tiempo - inicio_tiempo
            return (registros[medio], condiciones, tiempo_total)
            
        # Se cuenta la segunda condición (comparación)
        condiciones += 1
        if id_medio < id_buscado:
            bajo = medio + 1
        else:
            alto = medio - 1
            
    # Si el bucle termina, no se encontró
    fin_tiempo = time.perf_counter()
    tiempo_total = fin_tiempo - inicio_tiempo
    return (None, condiciones, tiempo_total)

def mostrar_resultado(titulo, resultado, id_buscado):
    """
    Función auxiliar para imprimir los resultados.
    """
    registro, condiciones, tiempo = resultado
    
    print(f"\n--- {titulo} ---")
    print(f"ID Buscado: {id_buscado}")
    
    if registro:
        # Se construye el nombre completo
        nombre_completo = f"{registro['nombre']} {registro['apellido_paterno']} {registro['apellido_materno']}"
        
        print(f"  Nombre: {nombre_completo}")
        print(f"  Sueldo: ${registro['sueldo_issste']:,.2f}")
    else:
        print("  Resultado: ID no encontrado.")
        
    print(f"  Condiciones ejecutadas: {condiciones}")
    # Se formatea el tiempo en microsegundos para mejor legibilidad
    print(f"  Tiempo de búsqueda: {tiempo * 1_000_000:.0f} microsegundos")

# --- Ejecución Principal ---

NOMBRE_ARCHIVO = "2021_04_3_AGUASCALIENTES.txt"
ID_ESPECIFICO = 276637868

# Paso 1: Aplicar la Abstracción de Datos
registros_en_memoria = cargar_datos(NOMBRE_ARCHIVO)

if registros_en_memoria:
    
    # Paso 2: Ejecutar la búsqueda obligatoria
    print("\n--- EJECUTANDO BÚSQUEDAS ---")
    
    # Búsqueda Secuencial
    res_sec = busqueda_secuencial(registros_en_memoria, ID_ESPECIFICO)
    mostrar_resultado("Búsqueda Secuencial", res_sec, ID_ESPECIFICO)
    
    # Búsqueda Binaria
    res_bin = busqueda_binaria(registros_en_memoria, ID_ESPECIFICO)
    mostrar_resultado("Búsqueda Binaria", res_bin, ID_ESPECIFICO)
    
    # Paso 3: Iniciar bucle interactivo
    while True:
        print("\n--- BÚSQUEDA INTERACTIVA ---")
        id_input = input("Introduce un ID para buscar (o 's' para salir): ")
        
        if id_input.lower() == 's':
            break
            
        try:
            # Se convierte la entrada del usuario a entero
            id_usuario = int(id_input)
            
            # Se ejecutan y muestran ambas búsquedas
            res_sec_usr = busqueda_secuencial(registros_en_memoria, id_usuario)
            mostrar_resultado("Búsqueda Secuencial (Usuario)", res_sec_usr, id_usuario)
            
            res_bin_usr = busqueda_binaria(registros_en_memoria, id_usuario)
            mostrar_resultado("Búsqueda Binaria (Usuario)", res_bin_usr, id_usuario)
            
        except ValueError:
            print("Error: Por favor, introduce un número de ID válido.")

print("Fin del programa.")