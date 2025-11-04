#include <stdio.h>
#include <stdlib.h>

// Prototipo de la función que se encargará de mostrar una figura desde un archivo.
void mostrar_figura(const char* nombre_archivo);

int main() {
    printf("--- Mostrando Figuras desde Archivos ---\n\n");

    // Se invoca la función para leer y mostrar cada uno de los archivos de texto.
    // Se especifica la ruta relativa a la carpeta "figuras".
    mostrar_figura("figuras/cuadrado.txt");
    mostrar_figura("figuras/rectangulo.txt");
    mostrar_figura("figuras/triangulo.txt");

    printf("Ejecucion finalizada. Presiona una tecla para salir.\n");
    system("pause");

    return 0;
}

/*
 * Abre, lee y muestra el contenido de un archivo de texto en la consola.
 * Recibe como parámetro una cadena de caracteres con la ruta y el nombre
 * del archivo que se va a procesar.
 */
void mostrar_figura(const char* nombre_archivo) {
    // Se declara un puntero de tipo FILE para manejar el flujo del archivo.
    FILE *archivo;
    // Se declara una variable para almacenar cada caracter leído.
    int caracter;

    // Se intenta abrir el archivo especificado en modo de solo lectura ("r").
    archivo = fopen(nombre_archivo, "r");

    // Se verifica si la apertura del archivo fue exitosa.
    // Si fopen() devuelve NULL, significa que el archivo no se pudo encontrar o abrir.
    if (archivo == NULL) {
        printf("Error: No se pudo abrir el archivo '%s'\n\n", nombre_archivo);
        // Se termina la ejecución de esta función si hay un error.
        return;
    }

    printf("Contenido de '%s':\n", nombre_archivo);

    // Se inicia un bucle para leer el archivo caracter por caracter.
    // El bucle se detiene cuando fgetc() alcanza el final del archivo (EOF).
    while ((caracter = fgetc(archivo)) != EOF) {
        // Se imprime en la consola el caracter que se acaba de leer.
        putchar(caracter);
    }
    printf("\n\n");

    // Se cierra el flujo del archivo para liberar los recursos del sistema.
    fclose(archivo);
}