from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os

def encriptacion(mensaje, llave):
    codificacion = mensaje.encode('utf-8')
    llave = urandom(16)
    cipher = Cipher(algorithms.AES(llave), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    codigo_cifrado = encryptor.update(codificacion) + encryptor.finalize()
    return codigo_cifrado

def desencriptacion(codigo_cifrado, llave):
    cipher = Cipher(algorithms.AES(llave), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    mensaje_descifrado = decryptor.update(codigo_cifrado) + decryptor.finalize()
    return mensaje_descifrado.decode('utf-8')
def generar_clave():
    clave = os.urandom(16)
    return clave

def encriptacion_des3(mensaje):
    llave = urandom(24) # 3DES utiliza claves de 24 bytes
    cipher = Cipher(algorithms.TripleDES(llave), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    mensaje = mensaje.encode('utf-8')
    codificacion = encryptor.update(mensaje) + encryptor.finalize()
    return codificacion, llave

def desencriptacion_des3(codificacion, llave):
    cipher = Cipher(algorithms.TripleDES(llave), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    mensaje = decryptor.update(codificacion) + decryptor.finalize()
    return mensaje.decode('utf-8')

def encriptacion_aes(mensaje, tamano_clave=16):
    llave = urandom(tamano_clave)
    cipher = Cipher(algorithms.AES(llave), modes.CFB(urandom(16)), backend=default_backend())
    encryptor = cipher.encryptor()
    mensaje = mensaje.encode('utf-8')
    codificacion = encryptor.update(mensaje) + encryptor.finalize()
    return codificacion, llave

def desencriptacion_aes(codificacion, llave):
    cipher = Cipher(algorithms.AES(llave), modes.CFB(urandom(16)), backend=default_backend())
    decryptor = cipher.decryptor()
    mensaje = decryptor.update(codificacion) + decryptor.finalize()
    return mensaje.decode('utf-8')
