from random import randint

class DH_Endpoint:
    def __init__(self, p, g, private_key):
        self.p = p  # Número primo compartido
        self.g = g  # Generador
        self.private_key = private_key  # Llave privada del usuario
        self.partial_key = None  # Clave parcial generada durante el intercambio
        self.full_key = None  # Clave compartida después del intercambio

    def generate_partial_key(self):
        # Genera la clave parcial durante el intercambio
        self.partial_key = pow(self.g, self.private_key, self.p)
        return self.partial_key

    def generate_full_key(self, received_partial_key):
        # Genera la clave completa después de recibir la clave parcial del otro extremo
        self.full_key = pow(received_partial_key, self.private_key, self.p)
        return self.full_key

def generar_clave_privada():
    return randint(2, 100)  # Número aleatorio para la clave privada

def intercambio_claves():
    P = 23
    G = 9

    a = generar_clave_privada()
    b = generar_clave_privada()

    x = pow(G, a, P)
    y = pow(G, b, P)

    ka = pow(y, a, P)
    kb = pow(x, b, P)

    return ka, kb
