from DiffieHellman import DH_Endpoint, intercambio_claves
from CryptoDes import encriptacion, desencriptacion, encriptacion_des3, desencriptacion_des3, encriptacion_aes, desencriptacion_aes
from Client import Client
import Server

def Comprueba(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

def GeneraNumerosPrimos():
    primos = []
    for numero in range(1001):
        if Comprueba(numero):
            primos.append(numero)
    return primos

def main():
    ka, kb = intercambio_claves()

    print('La llave secreta de A es: %d' % ka)
    print('La llave secreta de B es: %d' % kb)

    c_public = 23  # Definir el valor de la clave pública del cliente
    c_private = 33  # Definir el valor de la clave privada del cliente
    s_public = 83  # Definir el valor de la clave pública del servidor
    s_private = 77  # Definir el valor de la clave privada del servidor

    Cliente = DH_Endpoint(c_public, s_public, c_private)
    Servidor = DH_Endpoint(c_public, s_public, s_private)

    c_partial = Cliente.generate_partial_key()
    s_partial = Servidor.generate_partial_key()

    c_full = Cliente.generate_full_key(c_partial)
    s_full = Servidor.generate_full_key(s_partial)

    if c_full == s_full:
        archivo = open("mensajeentrada.txt", "r")
        mensaje = str(archivo.readline().lower())
        archivo.close()

        # DES
        llave = b'my-secret-key'
        codigo_des = encriptacion(mensaje, llave)
        desco_des = desencriptacion(codigo_des, llave) # Asegúrate de definir 'llave'
        print(f"Resultado DES: {desco_des}")

        # 3DES
        llave_3des = b'my-secret-key-3des'
        codigo_3des, llave_3des = encriptacion_des3(mensaje, llave_3des)
        desco_3des = desencriptacion_des3(codigo_3des, llave_3des)
        print(f"Resultado 3DES: {desco_3des}")

        # AES
        llave_aes = b'my-secret-key-aes'
        codigo_aes, llave_aes = encriptacion_aes(mensaje, llave_aes)
        desco_aes = desencriptacion_aes(codigo_aes, llave_aes)
        print(f"Resultado AES: {desco_aes}")

        # Cliente
        client_instance = Client()
        client_instance.run()

if __name__ == "__main__":
    main()
