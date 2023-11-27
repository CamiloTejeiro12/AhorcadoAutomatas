from database import conectar, listar_registros, insertar_registro, actualizar_registro, eliminar_registro, seleccionar_registro_aleatorio, dividir_registro_aleatorio

# main.py
# from utils import seleccionar_registro_aleatorio, dividir_registro_aleatorio

# Resto del código de main.py...


"""
# Llamar a la función para seleccionar un registro aleatorio
registro_aleatorio = seleccionar_registro_aleatorio()

if registro_aleatorio:
    print("Registro Aleatorio:")
    print(registro_aleatorio)
else:
    print("No se pudo seleccionar un registro aleatorio.")
"""

# Llamar a la función para dividir un registro aleatorio
id_registro, palabra, pista = dividir_registro_aleatorio()


# """
class AhorcadoAutomata:
    def __init__(self, palabra_secreta, intentos_maximos):
        self.palabra_secreta = palabra_secreta.upper()
        self.estado_actual = "EN_JUEGO"
        self.intentos_maximos = intentos_maximos
        self.intentos_restantes = intentos_maximos
        self.letras_adivinadas = set()
        self.pista = ""

    def procesar_entrada(self, letra):
        letra = letra.upper()

        if letra in self.letras_adivinadas:
            self.estado_actual = "LETRA_REPETIDA"
        elif letra in self.palabra_secreta:
            self.letras_adivinadas.add(letra)
            if all(l in self.letras_adivinadas for l in self.palabra_secreta):
                self.estado_actual = "GANADOR"
        else:
            self.intentos_restantes -= 1
            if self.intentos_restantes <= 0:
                self.estado_actual = "PERDEDOR"

    def establecer_pista(self, pista):
        self.pista = pista

    def obtener_estado_actual(self):
        return self.estado_actual

    def obtener_estado_palabra(self):
        estado_palabra = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                estado_palabra += letra + " "
            else:
                estado_palabra += "_ "
        return estado_palabra.strip()

    def obtener_intentos_restantes(self):
        return self.intentos_restantes


# Ejemplo de uso:
palabra_secreta = palabra
intentos_maximos = 6
automata_ahorcado = AhorcadoAutomata(palabra_secreta, intentos_maximos)

# Configurar una pista (opcional)
# pista = "Lenguaje de programación con indentación"
automata_ahorcado.establecer_pista(pista)

while automata_ahorcado.obtener_estado_actual() == "EN_JUEGO":
    print("Pista:", pista)
    print("Estado actual de la palabra:",
          automata_ahorcado.obtener_estado_palabra())
    print(
        f"Intentos restantes: {automata_ahorcado.obtener_intentos_restantes()}")
    letra = input("Adivina una letra: ")
    automata_ahorcado.procesar_entrada(letra)

# Imprimir el resultado final
estado_final = automata_ahorcado.obtener_estado_actual()
if estado_final == "GANADOR":
    print(f"La palabra es '{palabra_secreta}'.")
    print("¡Felicidades! ¡Has adivinado la palabra!")
elif estado_final == "PERDEDOR":
    print(
        f"Lo siento, has agotado todos tus intentos. La palabra era '{palabra_secreta}'.")
elif estado_final == "LETRA_REPETIDA":
    print("Ya has adivinado esa letra antes.")

# """
