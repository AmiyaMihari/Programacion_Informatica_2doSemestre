// Guillermo Jair Montiel Juárez
// Unidad 3 - Actividad Complementaria 1

#include <stdio.h>
#include <stdlib.h> // Necesaria para la función system()

// Define una constante simbólica para el número total de empleados.
#define NUM_EMPLEADOS 10

// Se define la estructura para almacenar los datos de un empleado.
struct Empleado {
    int id;
    char apellido_paterno[50];
    char apellido_materno[50];
    char nombres[50];
    int edad;
    char puesto[50];
    float salario;
};

// DECLARACIÓN DE FUNCIONES
void limpiarPantalla();
void pausarPantalla();
void mostrarMenu();
void mostrarTodos(struct Empleado empleados[]);
void mostrarSueldoBajo(struct Empleado empleados[]);
void mostrarMayorEdad(struct Empleado empleados[]);


// FUNCIÓN PRINCIPAL
int main() {
    // Se crea un arreglo de estructuras 'Empleado' con 10 elementos.
    struct Empleado empleados[NUM_EMPLEADOS] = {
        {101, "Gonzalez", "Perez", "Juan", 42, "Gerente", 35000.50f},
        {102, "Martinez", "Lopez", "Ana", 28, "Analista", 18000.00f},
        {103, "Rodriguez", "Hernandez", "Carlos", 55, "Director", 60000.75f},
        {104, "Sanchez", "Garcia", "Laura", 35, "Contador", 22500.00f},
        {105, "Ramirez", "Diaz", "Pedro", 25, "Asistente", 15500.25f},
        {106, "Gomez", "N.", "Barney", 40, "Seguridad", 16000.00f},
        {107, "Simpson", "J.", "Homero", 39, "Inspector de Calidad", 21000.00f},
        {108, "Vargas", "Mendoza", "Sofia", 22, "Becaria", 8000.00f},
        {109, "Fernandez", "Rojas", "Ricardo", 62, "Mantenimiento", 19500.00f},
        {110, "Castillo", "Soto", "Lucia", 31, "Ventas", 24000.00f}
    };

    int opcion = 0;

    // Bucle principal del menú. Se repetirá hasta que el usuario elija la opción 4.
    do {
        limpiarPantalla();
        mostrarMenu();
        
        // Se lee la opción del usuario.
        scanf("%d", &opcion);

        // Limpia el buffer de entrada para evitar problemas con futuras lecturas.
        while(getchar() != '\n');

        limpiarPantalla();

        // Estructura de control para ejecutar la opción seleccionada.
        switch (opcion) {
            case 1:
                mostrarTodos(empleados);
                break;
            case 2:
                mostrarSueldoBajo(empleados);
                break;
            case 3:
                mostrarMayorEdad(empleados);
                break;
            case 4:
                printf("Saliendo del programa...\n");
                break;
            default:
                printf("Opcion no valida. Por favor, intente de nuevo.\n");
                break;
        }

        if (opcion != 4) {
            pausarPantalla();
        }

    } while (opcion != 4);

    return 0; // Finaliza el programa.
}


// FUNCIONES

// Limpia la consola. Compatible con Windows y Linux/Mac.
void limpiarPantalla() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// Pausa la ejecución del programa hasta que el usuario presione Enter.
void pausarPantalla() {
    printf("\n\nPresione Enter para volver al menu...");
    getchar();
}

// Muestra el menú de opciones formateado.
void mostrarMenu() {
    printf("=========================================\n");
    printf("         MENU DE EMPLEADOS\n");
    printf("=========================================\n");
    printf(" 1. Mostrar todos los empleados\n");
    printf(" 2. Mostrar empleado con sueldo mas bajo\n");
    printf(" 3. Mostrar empleado de mayor edad\n");
    printf(" 4. Salir\n");
    printf("=========================================\n");
    printf("Seleccione una opcion: ");
}

// Muestra todos los empleados en un formato de tabla.
void mostrarTodos(struct Empleado empleados[]) {
    printf("--- LISTA COMPLETA DE EMPLEADOS ---\n\n");
    // Encabezados de las columnas con formato.
    printf("%-5s %-15s %-15s %-10s %-5s %-20s %-10s\n", "ID", "AP. PATERNO", "AP. MATERNO", "NOMBRE", "EDAD", "PUESTO", "SALARIO");
    printf("------------------------------------------------------------------------------------------\n");
    for (int i = 0; i < NUM_EMPLEADOS; i++) {
        // Imprime cada campo del empleado con un ancho fijo para alinear las columnas.
        printf("%-5d %-15s %-15s %-10s %-5d %-20s %-10.2f\n",
               empleados[i].id,
               empleados[i].apellido_paterno,
               empleados[i].apellido_materno,
               empleados[i].nombres,
               empleados[i].edad,
               empleados[i].puesto,
               empleados[i].salario);
    }
}

// Busca y muestra la información del empleado con el salario más bajo.
void mostrarSueldoBajo(struct Empleado empleados[]) {
    // Guarda la posición (índice) del empleado con el menor sueldo encontrado hasta ahora.
    int indiceSueldoBajo = 0; // Inicia asumiendo que el primer empleado (índice 0) tiene el sueldo más bajo.

    // Recorre el arreglo de empleados desde el segundo elemento (índice 1).
    for (int i = 1; i < NUM_EMPLEADOS; i++) {
        // Compara el salario del empleado actual con el del menor sueldo guardado.
        if (empleados[i].salario < empleados[indiceSueldoBajo].salario) {
            // Si el salario del empleado actual es menor, actualiza el índice guardado.
            indiceSueldoBajo = i;
        }
    }

    printf("--- Empleado con el sueldo mas bajo ---\n");
    // Al final del bucle, la variable 'indiceSueldoBajo' contiene la posición del empleado correcto.
    printf("ID: %d\n", empleados[indiceSueldoBajo].id);
    printf("Nombre: %s %s %s\n", empleados[indiceSueldoBajo].nombres, empleados[indiceSueldoBajo].apellido_paterno, empleados[indiceSueldoBajo].apellido_materno);
    printf("Edad: %d\n", empleados[indiceSueldoBajo].edad);
    printf("Puesto: %s\n", empleados[indiceSueldoBajo].puesto);
    printf("Salario: %.2f\n", empleados[indiceSueldoBajo].salario);
}

// Busca y muestra la información del empleado con mayor edad.
void mostrarMayorEdad(struct Empleado empleados[]) {
    // Guarda la posición (índice) del empleado con la mayor edad encontrada hasta ahora.
    int indiceMayorEdad = 0; // Inicia asumiendo que el primer empleado (índice 0) es el de mayor edad.
    
    // Recorre el arreglo de empleados desde el segundo elemento (índice 1).
    for (int i = 1; i < NUM_EMPLEADOS; i++) {
        // Compara la edad del empleado actual con la del de mayor edad guardado.
        if (empleados[i].edad > empleados[indiceMayorEdad].edad) {
            // Si la edad del empleado actual es mayor, actualiza el índice guardado.
            indiceMayorEdad = i;
        }
    }

    printf("--- Empleado de mayor edad ---\n");
    // Al terminar el bucle, 'indiceMayorEdad' apunta al empleado correcto para mostrar sus datos.
    printf("ID: %d\n", empleados[indiceMayorEdad].id);
    printf("Nombre: %s %s %s\n", empleados[indiceMayorEdad].nombres, empleados[indiceMayorEdad].apellido_paterno, empleados[indiceMayorEdad].apellido_materno);
    printf("Edad: %d\n", empleados[indiceMayorEdad].edad);
    printf("Puesto: %s\n", empleados[indiceMayorEdad].puesto);
    printf("Salario: %.2f\n", empleados[indiceMayorEdad].salario);
}