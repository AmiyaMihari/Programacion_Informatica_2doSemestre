# Autor: Guillermo Jair Montiel Juárez
# Unidad 2 - Actividad Complementaria 2

# Este programa valida la estructura de una Clave Única de Registro de Población (CURP).

# Definición de constantes para la validación.
VOCALES = "AEIOU"
CONSONANTES = "BCDFGHJKLMNPQRSTVWXYZ"

# Conjunto de entidades federativas definidas.
ENTIDADES_FEDERATIVAS = {
    "AS", "BC", "BS", "CC", "CS", "CH", "CL", "CM", "DF", "DG", "GT",
    "GR", "HG", "JC", "MC", "MN", "MS", "NT", "NL", "OC", "PL", "QT",
    "QR", "SP", "SL", "SR", "TC", "TS", "TL", "VZ", "YN", "ZS", "NE"
}

def validar_formato_inicial(curp):
    """Revisa la longitud y las primeras cuatro letras de la CURP."""
    errores = []
    if len(curp) != 18:
        errores.append("Error: La CURP debe tener 18 caracteres.") # errores.append agrega un error a la lista de errores
        return errores  # Si la longitud es incorrecta, no tiene caso seguir validando.
    
    # Validación de las primeras 4 letras (nombre y apellidos)
    if not curp[0].isalpha(): # isalpha() verifica si es una letra
        errores.append("Posición 1: Debe ser una letra (primer apellido).")
    if curp[1] not in VOCALES:
        errores.append("Posición 2: Debe ser una vocal (primer apellido).")
    if not curp[2].isalpha():
        errores.append("Posición 3: Debe ser una letra (segundo apellido).")
    if not curp[3].isalpha():
        errores.append("Posición 4: Debe ser una letra (nombre).")
    return errores

def validar_fecha_nacimiento(fecha_str):
    """Valida que la sección de fecha (AAMMDD) sea correcta."""
    errores = []
    if not fecha_str.isdigit(): # isdigit() verifica si es un número
        errores.append("Posiciones 5-10: La fecha de nacimiento debe ser numérica (AAMMDD).")
        return errores
    
    try:
        mes = int(fecha_str[2:4])
        dia = int(fecha_str[4:6])
        if not (1 <= mes <= 12):
            errores.append(f"Posiciones 7-8: El mes '{fecha_str[2:4]}' no es válido.")
        if not (1 <= dia <= 31):
            # Nota: Esta es una validación simple, no verifica días por mes.
            errores.append(f"Posiciones 9-10: El día '{fecha_str[4:6]}' no es válido.")
    except ValueError:
        errores.append("La fecha contiene caracteres no numéricos.")
    return errores

def validar_componentes_finales(curp):
    """Valida el sexo, entidad federativa, consonantes y dígitos finales."""
    errores = []
    # Sexo (posición 11)
    if curp[10] not in ('H', 'M'):
        errores.append("Posición 11: El sexo debe ser 'H' o 'M'.")

    # Entidad federativa (posiciones 12-13)
    if curp[11:13] not in ENTIDADES_FEDERATIVAS:
        errores.append(f"Posiciones 12-13: La clave de entidad '{curp[11:13]}' no es válida.")

    # Consonantes internas (posiciones 14-16)
    if curp[13] not in CONSONANTES:
        errores.append("Posición 14: Debe ser una consonante (primer apellido).")
    if curp[14] not in CONSONANTES:
        errores.append("Posición 15: Debe ser una consonante (segundo apellido).")
    if curp[15] not in CONSONANTES:
        errores.append("Posición 16: Debe ser una consonante (nombre).")
    
    # Diferenciador de homonimia y siglo (posición 17)
    if not curp[16].isalnum(): # isalnum() verifica si es alfanumérico
        errores.append("Posición 17: El diferenciador debe ser alfanumérico.")
    
    # Dígito verificador (posición 18)
    if not curp[17].isdigit():
        errores.append("Posición 18: El dígito verificador debe ser un número.")
    
    return errores

def ejecutar_validador():
    """Función principal que orquesta el proceso de validación."""
    while True:
        # Solicita la CURP y la convierte a mayúsculas.
        curp = input("Por favor, ingresa la CURP a validar: ").upper() # upper() convierte a mayúsculas
        
        # Se juntan todos los errores encontrados en las diferentes validaciones.
        todos_los_errores = []
        
        errores_iniciales = validar_formato_inicial(curp)
        todos_los_errores.extend(errores_iniciales)
        
        # Si no hay errores de formato inicial (longitud), se sigue validando.
        if not errores_iniciales:
            todos_los_errores.extend(validar_fecha_nacimiento(curp[4:10]))
            todos_los_errores.extend(validar_componentes_finales(curp))

        if not todos_los_errores:
            print("\nLa CURP es válida.")
        else:
            print("\nLa CURP no es válida. Se encontraron estos detalles:")
            for error in todos_los_errores:
                print(f"  - {error}")
        
        # Pregunta al usuario si desea validar otra CURP.
        respuesta = input("\n¿Quieres validar otra CURP? (s/n): ").lower()
        if respuesta != 's':
            print("\n¡Gracias por usar el validador! Hasta luego.")
            break

# Se llama a la función principal para que el programa inicie.
ejecutar_validador()
