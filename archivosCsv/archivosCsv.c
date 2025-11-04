/*
* Guillermo Jair Montiel Juárez 
* archivo: archivosCsv.c
 * Actividad Complementaria 2 - Unidad 4
 *
 * Programa interactivo en C para leer un archivo CSV de registros de prácticas,
 * cargarlo en memoria y permitir al usuario realizar búsquedas por diferentes campos.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h> // Se incluye para system()
#include <ctype.h>  // Se incluye para usar la funcion toupper

// Se definen constantes para la gestión de datos
#define MAX_REGISTROS 500
#define MAX_LINEA 1024
#define MAX_CAMPO 100
// IMPORTANTE: Asegurate de que este nombre coincida con tu archivo CSV
#define NOMBRE_ARCHIVO "encuestas_2022.csv"


// Se define la estructura para almacenar cada fila (registro) del CSV.
struct RegistroPractica
{
    char id[MAX_CAMPO];
    char alumno[MAX_CAMPO];
    char sala[MAX_CAMPO];
    char grupo[MAX_CAMPO];
    char asignatura[MAX_CAMPO];
    char semestre[MAX_CAMPO];
    char practica_nombre[MAX_CAMPO];
    char practica_numero[MAX_CAMPO];
    char equipo[MAX_CAMPO];
    char fecha[MAX_CAMPO];
};

// Funcion multiplataforma para limpiar la pantalla de la terminal.
void limpiarPantalla()
{
#if defined(_WIN32) || defined(_WIN64)
    system("cls");
#else
    system("clear");
#endif
}


// Funcion para normalizar un texto: convierte a mayusculas.

void normalizarTexto(char *str)
{
    for (int i = 0; str[i]; i++)
    {
        str[i] = toupper((unsigned char)str[i]);
    }
}

/*
 * Función para cargar todos los datos del archivo CSV
 * en un arreglo de estructuras en memoria, normalizando campos.
 */
int cargarDatos(struct RegistroPractica registros[])
{
    FILE *archivo;
    char linea[MAX_LINEA];
    char *token;
    int contador = 0;

    archivo = fopen(NOMBRE_ARCHIVO, "r");

    if (archivo == NULL)
    {
        printf("Error: No se pudo abrir el archivo %s.\n", NOMBRE_ARCHIVO);
        printf("Asegurese de que el archivo este en la misma carpeta que el ejecutable.\n");
        return -1;
    }

    // Omite encabezados
    fgets(linea, MAX_LINEA, archivo);

    while (fgets(linea, MAX_LINEA, archivo) && contador < MAX_REGISTROS)
    {
        linea[strcspn(linea, "\n")] = 0;

        token = strtok(linea, ","); if (token != NULL) strcpy(registros[contador].id, token);
        token = strtok(NULL, ","); if (token != NULL) { strcpy(registros[contador].alumno, token); normalizarTexto(registros[contador].alumno); }
        token = strtok(NULL, ","); if (token != NULL) strcpy(registros[contador].sala, token);
        token = strtok(NULL, ","); if (token != NULL) strcpy(registros[contador].grupo, token);
        token = strtok(NULL, ","); if (token != NULL) { strcpy(registros[contador].asignatura, token); normalizarTexto(registros[contador].asignatura); }
        token = strtok(NULL, ","); if (token != NULL) strcpy(registros[contador].semestre, token);
        token = strtok(NULL, ","); if (token != NULL) { strcpy(registros[contador].practica_nombre, token); normalizarTexto(registros[contador].practica_nombre); }
        token = strtok(NULL, ","); if (token != NULL) strcpy(registros[contador].practica_numero, token);
        token = strtok(NULL, ","); if (token != NULL) strcpy(registros[contador].equipo, token);
        token = strtok(NULL, ","); if (token != NULL) strcpy(registros[contador].fecha, token);

        contador++;
    }

    fclose(archivo);
    printf("Se cargaron exitosamente %d registros.\n", contador);
    return contador;
}


// Función para imprimir el encabezado de la tabla de resultados.
void imprimirEncabezado()
{
    // Se anade la columna Asignatura y se ajustan anchos
    printf("\n%-6s | %-30s | %-5s | %-28s | %-15s | %-10s\n", "ID", "Alumno", "Sala", "Asignatura", "Practica", "Fecha");
    printf("------------------------------------------------------------------------------------------------------------------\n");
}


// Función para imprimir un único registro formateado.
void imprimirRegistro(struct RegistroPractica reg)
{
    // Se anade el campo asignatura y se ajustan anchos/precisiones
    printf("%-6.6s | %-30.30s | %-5.5s | %-28.28s | %-15.15s | %-10.10s\n",
           reg.id,
           reg.alumno,
           reg.sala,
           reg.asignatura,
           reg.practica_nombre,
           reg.fecha);
}

// Función para mostrar el menú de opciones de búsqueda al usuario.
void mostrarMenu()
{
    printf("\n--- Sistema de Busqueda de Practicas ---\n");
    printf("Seleccione una opcion de busqueda:\n");
    printf(" 1. Buscar por ID de registro\n");
    printf(" 2. Buscar por Alumno (parcial)\n");
    printf(" 3. Buscar por Sala\n");
    printf(" 4. Buscar por Grupo\n");
    printf(" 5. Buscar por Asignatura (parcial)\n");
    printf(" 6. Buscar por Semestre\n");
    printf(" 7. Buscar por Nombre de Practica (parcial)\n");
    printf(" 8. Buscar por Numero de Practica\n");
    printf(" 9. Buscar por Equipo\n");
    printf("10. Buscar por Fecha\n");
    printf("11. Salir\n");
    printf("Opcion: ");
}

/*
 * Función principal de búsqueda. Solicita el término
 * y recorre el arreglo de registros.
 * Retorna 1 si el usuario elige 'Salir', 0 en cualquier otro caso.
 */
int buscarRegistros(struct RegistroPractica registros[], int numRegistros)
{
    int opcion, i, contadorResultados;
    char terminoBusqueda[MAX_CAMPO];
    int dia, mes, anio;

    if (scanf("%d", &opcion) != 1)
    {
        printf("Entrada invalida. Por favor, ingrese un numero.\n");
        while (getchar() != '\n');
        return 0;
    }
    while (getchar() != '\n');

    if (opcion == 11)
    {
        return 1;
    }

    // Obtener termino de busqueda
    if (opcion == 10) // Fecha
    {
        printf("Introduce el dia (dd): "); scanf("%d", &dia);
        printf("Introduce el mes (mm): "); scanf("%d", &mes);
        printf("Introduce el año (aaaa): "); scanf("%d", &anio);
        while (getchar() != '\n');
        sprintf(terminoBusqueda, "%02d/%02d/%04d", dia, mes, anio);
        printf("Buscando fecha: %s\n", terminoBusqueda);
    }
    else if (opcion > 0 && opcion < 10) // Otros campos
    {
        printf("Introduce el termino a buscar: ");
        fgets(terminoBusqueda, MAX_CAMPO, stdin);
        terminoBusqueda[strcspn(terminoBusqueda, "\n")] = 0;
        normalizarTexto(terminoBusqueda);
    }
    else
    {
        printf("Opcion no valida.\n");
        return 0;
    }

    // Busqueda
    contadorResultados = 0;
    for (i = 0; i < numRegistros; i++)
    {
        int encontrado = 0;
        switch (opcion)
        {
        case 1: if (strcmp(registros[i].id, terminoBusqueda) == 0) encontrado = 1; break;
        case 2: if (strstr(registros[i].alumno, terminoBusqueda) != NULL) encontrado = 1; break;
        case 3: if (strcmp(registros[i].sala, terminoBusqueda) == 0) encontrado = 1; break;
        case 4: if (strcmp(registros[i].grupo, terminoBusqueda) == 0) encontrado = 1; break;
        case 5: if (strstr(registros[i].asignatura, terminoBusqueda) != NULL) encontrado = 1; break;
        case 6: if (strcmp(registros[i].semestre, terminoBusqueda) == 0) encontrado = 1; break;
        case 7: if (strstr(registros[i].practica_nombre, terminoBusqueda) != NULL) encontrado = 1; break;
        case 8: if (strcmp(registros[i].practica_numero, terminoBusqueda) == 0) encontrado = 1; break;
        case 9: if (strcmp(registros[i].equipo, terminoBusqueda) == 0) encontrado = 1; break;
        case 10: if (strcmp(registros[i].fecha, terminoBusqueda) == 0) encontrado = 1; break;
        }

        if (encontrado)
        {
            if (contadorResultados == 0) { imprimirEncabezado(); }
            imprimirRegistro(registros[i]);
            contadorResultados++;
        }
    }

    // Reporte final
    if (contadorResultados == 0)
    {
        printf("\nNo se encontraron resultados para \"%s\".\n", terminoBusqueda);
    }
    else
    {
        // Se ajusta la linea separadora final
        printf("------------------------------------------------------------------------------------------------------------------\n");
        printf("Se encontraron %d resultados.\n", contadorResultados);
    }
    return 0;
}

// Función principal (main)
int main()
{
    struct RegistroPractica registros[MAX_REGISTROS];
    int numRegistros;
    char continuar = 's';
    int salir = 0;

    numRegistros = cargarDatos(registros);

    if (numRegistros == -1)
    {
        printf("Error critico al cargar datos. El programa terminara.\n");
        return 1;
    }

    while (continuar == 's' || continuar == 'S')
    {
        limpiarPantalla();
        mostrarMenu();
        salir = buscarRegistros(registros, numRegistros);
        if (salir) { break; }
        printf("\n¿Deseas realizar otra busqueda? (s/n): ");
        scanf(" %c", &continuar);
        while (getchar() != '\n');
    }

    limpiarPantalla();
    printf("Saliendo del programa.\n");
    return 0;
}