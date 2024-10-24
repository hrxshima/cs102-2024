def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    
    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():  # Проверяем, что символ является буквой
            shift = ord(k_char.upper()) - ord('A')  # Сдвиг на основе ключа
            base = ord('A') if p_char.isupper() else ord('a')
            encrypted_char = chr((ord(p_char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += p_char  # Не изменяем не-буквенные символы
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else: plaintext += char  
    return plaintext
