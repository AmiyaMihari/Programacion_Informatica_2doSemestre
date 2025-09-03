// Autor: Guillermo Jair Montiel Juárez
// Unidad 1 - Actividad Complementaria 2
// Walmart.c - Simulador de compras

#include <stdio.h>
#include <string.h>

int main() {
    // Variables para almacenar información de cada producto
    char nombreProducto[100]; //Variable de caracteres para guardar el ticket impreso del producto
    float precioProducto;
    
    // Variables para el ticket final
    float costoTotal = 0.0;
    int cantidadArticulos = 0;
    char continuar;
    
    // Variable para construir el ticket de a poco
    char ticket[2000] = "";
    char lineaProducto[100];
    
    printf("=== BIENVENID@ A WALMART ===\n");
    printf("Realice su Compra, siga las instrucciones\n\n");
    
    do {
        // Solicitar nombre del producto
        printf("Ingrese el nombre del producto: ");
        // fgets permite leer más de una palabra
        fgets(nombreProducto, sizeof(nombreProducto), stdin);
        // Eliminar salto de línea que deja fgets
        nombreProducto[strcspn(nombreProducto, "\n")] = 0;
        
        // Solicitar precio del producto con validación
        int productoValido = 0;
        do {
            printf("Ingrese el precio del producto $");
            // Comprobar si la entrada es un número válido
            if (scanf("%f", &precioProducto) == 1 && precioProducto >= 0) {
                productoValido = 1;
            // En caso de que la entrada no sea un número, mostrar un mensaje de error
            } else {
                printf("ERROR: Precio inválido. Por favor ingrese un número válido.\n");
                // Limpiar el buffer de entrada
                while (getchar() != '\n');
                precioProducto = -1; // Resetear para que pida de nuevo
            }
        } while (!productoValido);
        
        // Actualizar totales
        costoTotal += precioProducto;
        cantidadArticulos++;
        
        // Agregar esta línea al ticket
        sprintf(lineaProducto, "%-20s ........... $%.2f\n", nombreProducto, precioProducto);
        strcat(ticket, lineaProducto);
        
        printf("\nProducto agregado exitosamente!\n");
        
        // Limpiar buffer antes de leer el continuar
        while (getchar() != '\n');
        
        // Preguntar si desea continuar
        printf("¿Desea agregar otro producto? (s/n): ");
        scanf(" %c", &continuar);
        printf("\n");
        while (getchar() != '\n'); // limpiar buffer después del char
        
    } while (continuar == 's' || continuar == 'S');
    
    // Mostrar el ticket completo al final
    printf("\n");
    printf("================================\n");
    printf("          TICKET WALMART        \n");
    printf("================================\n");
    printf("%s", ticket); // Mostrar todos los productos uno a uno
    printf("--------------------------------\n");
    printf("Cantidad de artículos: %d\n", cantidadArticulos);
    printf("TOTAL A PAGAR: $%.2f\n", costoTotal);
    printf("================================\n");
    printf("¡Gracias por su compra!\n");
    
    return 0;
}