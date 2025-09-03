// Unidad 1 - Actividad Complementaria 1
// Guillermo Jair Montiel Juárez

#include <stdio.h>

int main() {
    int edad;  // variable entera de edad

    // Pedir la edad al usuario
    printf("Ingrese su edad: ");
    scanf("%d", &edad);

    // Condición para saber si debe jubilarse
    if (edad > 59) { // Si la edad es mayor a 59 se jubila
        printf("Debes jubilarte\n");
    } else { // Si la edad es menor o igual a 59 no se jubila
        printf("Tienes que seguir trabajando\n");
    }

    return 0; // Fin
}
