"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Jordi Antonio Vazquez Lopez
Fecha: 07/11/25
"""


def limpiar_pantalla():
    
    """
    Imprimo varias líneas en blanco para evitar
    que el jugador 2 vea la palabra introducida.
    """

    print("\n" * 50)


def solicitar_palabra():

    """
    Solicita una palabra al jugador 1.

    La palabra debe tener al menos 5 caracteres y contener solo letras.

    Returns
    -------

    str
        La palabra en mayúsculas.
    """

    palabra = input("Jugador 1, introduce una palabra (mínimo 5 letras): ")
    
    while len(palabra) < 5 or not palabra.isalpha():
        
        if len(palabra) < 5:
            print("Error: debe tener al menos 5 letras.")

        elif not palabra.isalpha():
            print("Error: solo se permiten letras (sin números ni símbolos).")

        palabra = input("Introduce otra palabra: ")

    return palabra.upper()


def solicitar_letra(letras_usadas):

    """
    Solicita una letra al jugador 2.

    La letra debe ser una única letra, no haber sido usada antes y debe pertenecer al alfabeto.

    Parameters
    ----------

    letras_usadas : list
        Lista de letras usadas.

    Returns
    -------

    str
        La letra en mayúsculas.
    """

    letra = input("Introduce una letra: ").upper()

    while (len(letra) != 1 or not letra.isalpha() or letra in letras_usadas):

        if len(letra) != 1:
            print("Error: introduce solo una letra.")
        
        elif not letra.isalpha():
            print("Error: solo se permiten letras (sin números ni símbolos).")
        
        elif letra in letras_usadas:
            print("Ya usaste esa letra.")
        
        letra = input("Introduce otra letra: ").upper()
   
    return letra


def mostrar_estado(palabra_oculta, intentos, letras_usadas):

    """
    Muestra el estado del juego.

    Parameters
    ----------
    palabra_oculta : str
        La palabra con guiones bajos y letras adivinadas.

    intentos : int
        Número de intentos restantes.

    letras_usadas : list
        Lista de letras usadas.
    """

    print("\nIntentos restantes:", intentos)

    print("Palabra:", " ".join(palabra_oculta))

    print("Letras usadas:", ", ".join(letras_usadas))

    print("-" * 20)


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):

    """
    Va mostrando poco a poco la palabra oculta.

    Parameters
    ----------

    palabra : str
        La palabra completa.

    palabra_oculta : str
        La palabra con guiones bajos y letras descubiertas.

    letra : str
        La letra que el jugador ha puesto.

    Returns
    -------

    str
        La palabra con las letras correctas reveladas.
    """

    nueva_palabra = list(palabra_oculta)

    for i, letras in enumerate(palabra):
        
        if letras == letra:
            nueva_palabra[i] = letra

    return "".join(nueva_palabra)


def jugar():

    """
    Ejecuta el juego del ahorcado.

    Gestiona el juego, incluyendo los intentos,
    las letras usadas y la comprobación de victoria o derrota.
    """

    print("=== JUEGO DEL AHORCADO ===\n")

    INTENTOS_MAXIMOS = 5

    palabra = solicitar_palabra()

    limpiar_pantalla()

    palabra_oculta = "_" * len(palabra)

    intentos = INTENTOS_MAXIMOS

    letras_usadas = []

    juego_terminado = False

    print("Jugador 2: adivina la palabra.\n")

    while intentos > 0 and not juego_terminado:

        mostrar_estado(palabra_oculta, intentos, letras_usadas)

        letra = solicitar_letra(letras_usadas)

        letras_usadas.append(letra)

        if letra in palabra:

            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)

            print("La letra está en la palabra.")
            
            if "_" not in palabra_oculta:
                juego_terminado = True

        else:
            intentos -= 1
            print("Esa letra no está en la palabra.")

    if "_" not in palabra_oculta:
        print("\n¡Ganaste, suuuuuuuu! La palabra era:", palabra)

    else:
        print("\nPerdiste nuuuuu :(. La palabra correcta era:", palabra)


def main():

    """
    Inicia el juego y permite al usuario decidir si quiere volver a jugar.
    """

    jugar()

    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    
    if jugar_otra_vez.lower() == 's':
        main()


if __name__ == "__main__":
    main()
