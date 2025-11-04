// Guillermo Jair Montiel Juárez
// Unidad 2 - Actividad Complementaria 1

#include <stdio.h>
#include <stdlib.h> // Librería para la función system(), que nos permite ejecutar comandos en la terminal.

// PROTOTIPOS DE LAS FUNCIONES
// Le decimos al compilador qué funciones vamos a usar en el programa.
void ingresarDatosAlumno();
void ingresarCalificaciones();
void calcularPromedio();
void limpiarPantalla();

// VARIABLES GLOBALES
char nombre[100];
char carrera[50];
int numeroCuenta;
int semestre;
float calificaciones[50]; // Arreglo para guardar hasta 50 calificaciones.
int totalCalificaciones = 0; // Contador para saber cuántas calificaciones se han ingresado.

// FUNCIÓN PRINCIPAL
int main() {
    int opcion; // Variable para guardar la opción del usuario.
    int datosIngresados = 0; // Bandera para saber si ya se ingresaron los datos del alumno (0 = no, 1 = si).

    // El ciclo do-while asegura que el menú se muestre al menos una vez
    // y se repita hasta que el usuario elija la opción 4 para salir.
    do {
        limpiarPantalla(); // Llamamos a la función para limpiar la pantalla de la terminal aquí.

        // Mostramos el menú principal.
        printf("\n.------------------------------------------------.\n");
        printf("  CALCULADORA DE PROMEDIO ESTUDIANTIL - FCA  \n");
        printf("'------------------------------------------------'\n");
        printf("1. Ingresar datos del alumno\n");
        printf("2. Ingresar sus calificaciones\n");
        printf("3. Calcular promedio\n");
        printf("4. Salir\n");
        printf("--------------------------------------------------\n");
        printf("Elige una opcion: ");
        scanf("%d", &opcion);

        // La estructura 'switch' ejecuta el código correspondiente a la opción elegida.
        switch (opcion) {
            case 1:
                ingresarDatosAlumno();
                datosIngresados = 1; // Marcamos que los datos ya fueron ingresados.
                break;
            case 2:
                // Verificamos si los datos del alumno ya fueron ingresados.
                if (datosIngresados == 1) {
                    ingresarCalificaciones();
                } else {
                    printf("\n[ERROR] Debes ingresar primero los datos del alumno (Opcion 1).\n");
                }
                break;
            case 3:
                // Verificamos si ya se ingresaron calificaciones para poder calcular el promedio.
                if (totalCalificaciones > 0) {
                    calcularPromedio();
                } else {
                    printf("\n[ERROR] Debes ingresar primero las calificaciones (Opcion 2).\n");
                }
                break;
            case 4:
                printf("\nSaliendo del programa...fin\n");
                break;
            default: // Caso cuando el usuario ingresa una opción no válida.
                printf("\n[ERROR] Opcion no valida. Por favor, elige una opcion del 1 al 4.\n");
                break;
        }

        // Pausa para que el usuario pueda leer los mensajes antes de que el menú se vuelva a mostrar.
        if (opcion != 4) {
             printf("\nPresiona Enter para continuar...");
             getchar(); // Limpia el buffer del teclado.
             getchar(); // Espera a que el usuario presione Enter.
        }

    } while (opcion != 4);

    return 0; // Indica que el programa finalizó con éxito.
}


//----------
// FUNCIONES

// Función que limpia la consola, compatible con Windows y Linux
void limpiarPantalla() {
    #ifdef _WIN32 // Si el compilador detecta que está en un sistema Windows...
        system("cls");
    #else // Para cualquier otro sistema (Linux)
        system("clear");
    #endif
}

//Función para solicitar y almacenar los datos del alumno.
//trabaja con variables globales.
void ingresarDatosAlumno() {
    printf("\n--- a) Ingresar Datos del Alumno ---\n");
    printf("Nombre completo: ");
    getchar(); // Limpia el buffer para leer correctamente la cadena de texto.
    scanf(" %[^\n]", nombre); // Lee el nombre completo, incluyendo espacios.

    printf("Numero de cuenta: ");
    scanf("%d", &numeroCuenta);

    printf("Semestre que cursa: ");
    scanf("%d", &semestre);

    printf("Carrera: ");
    getchar(); // Limpia el buffer de nuevo.
    scanf(" %[^\n]", carrera);

    printf("\n¡Datos del alumno guardados exitosamente!\n");
}


// Función para ingresar las calificaciones de las materias.
//Valida que cada calificación esté en el rango de 5 a 10.
void ingresarCalificaciones() {
    printf("\n--- b) Ingresar Calificaciones ---\n");
    printf("¿Cuantas calificaciones deseas ingresar?: ");
    scanf("%d", &totalCalificaciones);

    printf("\nPor favor, ingresa las %d calificaciones (deben estar entre 5 y 10):\n", totalCalificaciones);

    // Ciclo 'for' para pedir cada una de las calificaciones.
    for (int i = 0; i < totalCalificaciones; i++) {
        float calificacionTemporal; // Variable para guardar la calificación antes de validarla.

        printf("Calificacion de la materia %d: ", i + 1);
        scanf("%f", &calificacionTemporal);

        // Ciclo 'while' para validar que la calificación esté en el rango correcto.
        // Mientras la calificación sea menor a 5 o mayor a 10, seguirá pidiéndola.
        while (calificacionTemporal < 5.0 || calificacionTemporal > 10.0) {
            printf("[ERROR] Calificacion invalida. Debe estar entre 5 y 10. Intenta de nuevo: ");
            scanf("%f", &calificacionTemporal);
        }

        // Si la calificación es válida, la guardamos en nuestro arreglo.
        calificaciones[i] = calificacionTemporal;
    }

    printf("\n¡Calificaciones guardadas exitosamente!\n");
}

// Función para calcular el promedio y mostrar todos los datos.
// Realiza la suma de las calificaciones y las divide entre el total.
void calcularPromedio() {
    float sumaTotal = 0.0;
    float promedioFinal = 0.0;

    // Ciclo 'for' para sumar todas las calificaciones guardadas en el arreglo.
    for (int i = 0; i < totalCalificaciones; i++) {
        sumaTotal = sumaTotal + calificaciones[i];
    }

    // Calculamos el promedio final.
    promedioFinal = sumaTotal / totalCalificaciones;

    // Mostramos todos los datos del alumno junto con el promedio calculado.
    printf("\n--- c) Promedio Final del Alumno ---\n");
    printf("----------------------------------------\n");
    printf("Nombre:          %s\n", nombre);
    printf("Numero de Cuenta: %d\n", numeroCuenta);
    printf("Semestre:        %d\n", semestre);
    printf("Carrera:         %s\n", carrera);
    printf("----------------------------------------\n");
    printf("PROMEDIO FINAL:  %.2f\n", promedioFinal); // %.2f formatea el número para mostrar solo 2 decimales.
    printf("----------------------------------------\n");
}