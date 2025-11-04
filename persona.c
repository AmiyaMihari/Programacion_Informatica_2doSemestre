    // Guillermo Jair Montiel Juárez
    // Unidad 3 - Actividad Complementaria 2

    #include <stdio.h>
    #include <string.h>

    // Se define la estructura para almacenar los datos de una dirección.
    // Esta estructura será anidada dentro de la estructura Persona.
    struct Direccion {
        char calle[50];
        int numero;
        char colonia[50];
        char ciudad[50];
        int codigo_postal;
    };

    // Se define la estructura principal para los datos de una persona.
    // Incluye una estructura Direccion para guardar la dirección completa (estructura anidada).
    struct Persona {
        char apellido_paterno[50];
        char apellido_materno[50];
        char nombres[50];
        int edad;
        struct Direccion direccion;
    };

    void imprimirPersona(struct Persona p);
    void imprimirLista(struct Persona lista[], int tamano);

    int main() {
        // Se inicializa un arreglo de estructuras 'Persona' con datos de ejemplo.
        // El tamaño del arreglo se calcula automáticamente con sizeof.
        struct Persona listaPersonas[] = {
            {"Gonzalez", "Perez", "Juan", 30, {"Av. Insurgentes", 123, "Roma Norte", "Ciudad de Mexico", 6700}},
            {"Martinez", "Lopez", "Maria", 25, {"Calle Aguacate", 456, "Centro", "Guadalajara", 44100}},
            {"Sanchez", "Garcia", "Pedro", 42, {"Blvd. Kukulcan", 789, "Zona Hotelera", "Cancun", 77500}},
            {"Rodriguez", "Hernandez", "Ana", 22, {"Paseo de la Reforma", 101, "Juarez", "Ciudad de Mexico", 6600}},
            {"Diaz", "Ramirez", "Carlos", 35, {"Av. Lazaro Cardenas", 202, "Valle Oriente", "Monterrey", 66269}}
        };

        // Calculo del tamaño del arreglo.
        // Se calcula la cantidad de elementos del arreglo dividiendo su tamaño total por el de un elemento.
        int tamano = sizeof(listaPersonas) / sizeof(listaPersonas[0]);
        struct Persona temporal; // Variable auxiliar para el intercambio en el ordenamiento.
        int i, j;

        printf("--- Lista de Personas sin Ordenar ---\n\n");
        imprimirLista(listaPersonas, tamano);

        // Se implementa el algoritmo de ordenamiento de burbuja.
        for (i = 0; i < tamano - 1; i++) {
            for (j = 0; j < tamano - i - 1; j++) {
                // Se utiliza strcmp para comparar las cadenas de las ciudades.
                // Para ordenar de forma descendente (Z a A), se busca un resultado menor a 0.
                // Se accede al campo anidado 'ciudad' a través de 'direccion'.
                if (strcmp(listaPersonas[j].direccion.ciudad, listaPersonas[j + 1].direccion.ciudad) < 0) {
                    // Si la condición se cumple, se intercambian las posiciones de las estructuras completas.
                    temporal = listaPersonas[j];
                    listaPersonas[j] = listaPersonas[j + 1];
                    listaPersonas[j + 1] = temporal;
                }
            }
        }

        printf("\n\n--- Lista de Personas Ordenada por Ciudad (Descendente) ---\n\n");
        imprimirLista(listaPersonas, tamano);

        return 0;
    }

    /**
     * Función para imprimir los datos de una única persona.
     * Recibe una estructura Persona y formatea su salida en la consola.
     */

    void imprimirPersona(struct Persona p) {
        printf("Nombre: %s %s %s\n", p.nombres, p.apellido_paterno, p.apellido_materno);
        printf("Edad: %d\n", p.edad);
        printf("Direccion: %s %d, Col. %s, %s, C.P. %d\n",
            p.direccion.calle,
            p.direccion.numero,
            p.direccion.colonia,
            p.direccion.ciudad,
            p.direccion.codigo_postal);
        printf("--------------------------------------------------\n");
    }

    /**
     * Función para recorrer e imprimir una lista completa de personas.
     * Recibe un arreglo de estructuras y su tamaño, y llama a imprimirPersona por cada elemento.
     */
    void imprimirLista(struct Persona lista[], int tamano) {
        int i;
        for (i = 0; i < tamano; i++) {
            imprimirPersona(lista[i]);
        }
    }