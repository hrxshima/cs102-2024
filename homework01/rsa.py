"""
Модуль для реализации алгоритма RSA шифрования и дешифрования.
"""
import random
import typing as tp

def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Алгоритм Евклида для нахождения наибольшего общего делителя.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b:
        a, b = b, a % b
    return a


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Расширенный алгоритм Евклида для нахождения мультипликативной
    обратной величины двух чисел.
    >>> multiplicative_inverse(7, 40)
    23
    """
    original_phi = phi
    x0, x1 = 0, 1

    if phi == 1:
        return 0

    while e > 1:
        q = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += original_phi

    return x1

def generate_keypair(p: int, q:int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Оба числа должны быть простыми.")
    if p == q:
        raise ValueError("p и q не могут быть равны.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk: tp.Tuple[int, int], plaintext:str) -> tp.List[int]:
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext:tp.List[int]) -> str:
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Введите простое число: "))
    q = int(input("Введите другое простое число (не то же самое): "))
    print("Генерация ваших публичных/приватных ключей . . .")
    public, private = generate_keypair(p, q)
    print("Ваш публичный ключ:", public)
    print("Ваш приватный ключ:", private)

    message = input("Введите сообщение для шифрования с вашим приватным ключом: ")
    encrypted_msg = encrypt(private, message)

    print("Ваше зашифрованное сообщение:")
    print("".join(map(str, encrypted_msg)))
    print("Расшифровка сообщения с публичным ключом", public, " . . .")
    print("Ваше сообщение:")
    print(decrypt(public, encrypted_msg))
