# pinata.py
# Juego para simular que se rompe una piñata.

import random # Para funciones aleatorias
import os # Para limpiar la pantalla de la terminal

# Lista de premios.
PREMIOS = [
    "una bolsa de paletas", "un carrito de fricción", "un trompo de colores",
    "un yoyo", "una muñeca pequeña", "un paquete de chicles",
    "una pelota de plástico", "un chocolate grande", "una flauta de juguete",
    "un set de calcomanías", "nada... ¡casi le dabas!",
    "nada... ¡más fuerte la próxima vez!", "nada... ¡solo salió polvo!"
]

def mostrar_arte_ganador(premio):
    """Muestra el arte del burrito roto"""
    print(r"""
    
    ███████╗███████╗██╗     ██╗ ██████╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗
    ██╔════╝██╔════╝██║     ██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
    █████╗  █████╗  ██║     ██║██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗
    ██╔══╝  ██╔══╝  ██║     ██║██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║
    ██║     ███████╗███████╗██║╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║
    ╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
                     ★ ･ﾟ✧*:･ﾟ✧ ¡FELICIDADES! ✧ﾟ･: *✧ﾟ･ ★

          \o/
           |
          / \
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣰⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⣿⣄⣀⣀⣀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢰⣿⣿⠋⣠⡈⣻⣿⣿⣶⡀⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣍⡉⠛⠁⠀
                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⢀⣤⠈⠛⠛⠋⣿⣿⣿⠟⠛⠛⠛⠀⠀
                     ⠀⠀⠀⠀⢀⣄⠐⣿⣿⣿⣿⠿⣿⣿⣿       ⣿⣄⣉⣁⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⠀⢰⣿⣿⣦⡈⠛⠋⣁⣤⡈           ⠙⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
                     ⠀⠀⢀⠙⣿⠿⠿⣿⣶⣿⣿⢿⣿⣦⣤⣶⣿⣷⣄⣉⣁⣤⠀⠀⠀⠀⠀⠀⠀⠀
                          o * \+/ * +
                         + $ o * o

    Rompiste la piñata y obtuviste: {}
    """.format(premio))

def mostrar_arte_perdedor():
    """Muestra el arte del burrito intacto con tu cartel personalizado."""
    print(r"""

    ███╗   ███╗ █████╗ ██╗      █████╗     ███████╗██╗   ██╗███████╗██████╗ ████████╗███████╗
    ████╗ ████║██╔══██╗██║     ██╔══██╗    ██╔════╝██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
    ██╔████╔██║███████║██║     ███████║    ███████╗██║   ██║█████╗  ██████╔╝   ██║   █████╗
    ██║╚██╔╝██║██╔══██║██║     ██╔══██║    ╚════██║██║   ██║██╔══╝  ██╔══██╗   ██║   ██╔══╝
    ██║ ╚═╝ ██║██║  ██║███████╗██║  ██║    ███████║╚██████╔╝███████╗██║  ██║   ██║   ███████╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

         o/|
         | |彡彡彡
        / \|
                                       ja ja
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣰⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⣿⣄⣀⣀⣀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢰⣿⣿⠋⣠⡈⣻⣿⣿⣶⡀⠀
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣍⡉⠛⠁⠀
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⢀⣤⠈⠛⠛⠋⣿⣿⣿⠟⠛⠛⠛⠀⠀
               ⠀⠀⠀⠀⢀⣄⠐⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣷⣶⣿⣄⣉⣁⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⢰⣿⣿⣦⡈⠛⠋⣁⣤⡈⠻⡿⠟⠋⠙⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⢀⠙⣿⠿⠿⣿⣶⣿⣿⢿⣿⣦⣤⣶⣿⣷⣄⣉⣁⣤⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⣼⣦⣤⣴⣦⠙⠛⢉⣠⣄⠈⠻⠟⢉⣀⠙⠿⣿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⣿⡟⢀⣿⣿⣷⣾⣿⣿⣿⣿⣦⣴⣿⠿⠿⣦⣠⣴⣿⡀⠀⠀⠀⠀⠀⠀⠀
               ⠀⢸⣿⡇⠈⢿⠏⠙⣿⠀⠉⠉⠉⠉⠁⠀⠀⠀⢻⣿⠛⠿⡇⠀⠀⠀⠀⠀⠀⠀
               ⠀⠈⠉⠀⣦⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⢰⣦⣄⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    La piñata sigue intacta...
    """)

# Función para determinar el premio basado en los golpes dados.
def obtener_premio(golpes):
    """Determina si el jugador gana un premio basado en el número de golpes."""
    probabilidad = golpes * 5 # Cada golpe incrementa la probabilidad en un 5%. Si llega a 100% o más, siempre gana.
    # Si el número aleatorio entre 1 y 100 es menor o igual a la probabilidad, gana un premio.
    if random.randint(1, 100) <= probabilidad:
        premios_reales = [p for p in PREMIOS if "nada" not in p] # Filtra los premios que no tienen la palabra "nada"
        return random.choice(premios_reales) # Elige un premio al azar
    else: # Si no gana, devuelve un mensaje de "nada"
        mensajes_nada = [p for p in PREMIOS if "nada" in    p]
        return random.choice(mensajes_nada) # Elige un mensaje de "nada" al azar

# Función para jugar una ronda completa.
def jugar_una_ronda():
    """Ejecuta una ronda completa del juego."""
    print("\n¡Dale con ganas a la piñata!")
    
    golpes_usuario = 0 # Inicializa la variable de golpes del usuario en 0.
    # Bucle para asegurar que el usuario ingrese un número válido de golpes.
    while True:
        try:
            entrada = input("¿Cuántos golpes le quieres dar a la piñata? ")
            golpes_usuario = int(entrada)
            if golpes_usuario > 0:
                break
            else:
                print("¡Necesitas darle al menos un golpe! Inténtalo de nuevo.")
        except ValueError:
            print("Eso no es un número. Por favor, escribe cuántos golpes quieres dar.")

    premio_obtenido = obtener_premio(golpes_usuario) # Determina el premio.

    os.system('cls' if os.name == 'nt' else 'clear') # Limpia la pantalla de la terminal.

    # Muestra el arte correspondiente según si ganó o no.
    if "nada" in premio_obtenido:
        mostrar_arte_perdedor()
        print(premio_obtenido)
    else:
        mostrar_arte_ganador(premio_obtenido)

def main():
    """Función principal que controla el flujo del juego."""
    print("""
+===================================================================+
|                                                                   |
|     *** ¡BIENVENIDO AL JUEGO DE LA PIÑATA! *** |
|                                                                   |
|     *** ¡Dale golpes y trata de romperla! *** |
|     *** ¡Puedes ganar increibles premios! *** |
|                                                                   |
+===================================================================+
    """)
    # Inicia el juego y permite jugar hasta que el usuario decida salir.
    while True:
        jugar_una_ronda()
        
        # Bucle para validar la respuesta del usuario.
        while True:
            respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
            if respuesta == "s" or respuesta == "n":
                break  # Si la respuesta es 's' o 'n', salimos de este bucle.
            else:
                # Si no, mostramos un error y el bucle se repite.
                print("Respuesta no válida. Por favor, solo responde 's' o 'n'.")
        
        if respuesta == "n":
            break # Si la respuesta fue 'n', terminamos el juego.

    print("""
+===================================================================+
|                                                                   |
|     *** ¡GRACIAS POR JUGAR! *** |
|     *** ¡Hasta la proxima! *** |
|                                                                   |
+===================================================================+
    """)

# Se llama a la función principal para iniciar el juego.
main()