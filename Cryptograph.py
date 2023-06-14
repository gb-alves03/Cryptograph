#pip install pycryptodome
#pip install pycryptodomex

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode

key = get_random_bytes(16)
plaintext = input("Digite o texto a ser criptografado: ")
plaintext = plaintext.encode('utf-8')

encrypt_cipher = AES.new(key, AES.MODE_EAX)


def encrypt(text, cipher):
    cipher
    ciphertext = cipher.encrypt(text)
    print(b64encode(ciphertext).decode('utf-8'))
    return ciphertext


def decrypt(encrypted_text, cipher):
    decrypt_cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
    plaintext = decrypt_cipher.decrypt(encrypted_text)
    print(plaintext.decode('utf-8'))


i = False
while i != True:
    id = int(input("Digite o id da opção desejada: "))
    match(id):
        case 1:
            encrypted = encrypt(plaintext, encrypt_cipher)
        case 2:
            decrypted = decrypt(encrypted, encrypt_cipher)
        case 0:
            i = True
