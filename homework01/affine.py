def encrypt_affine(plaintext, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)

    def affine_encrypt_char(char, a, b):
        if char.lower() not in alphabet:
            return char
        x = alphabet.index(char.lower())
        encrypted_index = (a * x + b) % m
        encrypted_char = alphabet[encrypted_index]
        if char.isupper():
            return encrypted_char.upper()
        return encrypted_char


    ciphertext = "".join(affine_encrypt_char(char, a, b) for char in plaintext)
    return ciphertext

# Пример использования
plaintext = "Hello, world!"
a = 5
b = 8
ciphertext = encrypt_affine(plaintext, a, b)
print(ciphertext)