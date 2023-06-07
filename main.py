#Функція для шифрування тексту шифром Цезаря:
def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text
#Функція для дешифрування тексту способом Цезаря:
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text
#Функція для шифрування тексту способом Віженера
def encrypt_vigenere(plaintext, keyword):
    encrypted_text = ""
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index].upper())- ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            encrypted_text += char
    return encrypted_text
#Функція для дешифрування тексту способом Віженера
def decrypt_vigenere(ciphertext, keyword):
    decrypted_text = ""
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index].upper()) -ord('A')
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A')- shift) % 26 + ord('A'))
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            decrypted_text += char
    return decrypted_text
#Дізнаємось що саме хоче користувач:
cipher_type = input("Do you want to use Caesar or Vigenere cipher? (Enter 'c' for Caesar or 'v' for Vigenere): ")
action = input("Do you want to encrypt or decrypt text? (Enter 'e' for encrypt or 'd' for decrypt): ")
text = input("Enter text: ")
#Якщо користувач вибрав шифр Цезаря:
if cipher_type == 'c':
    shift = int(input("Enter shift value: "))
    if action == 'e':
        result = encrypt_caesar(text, shift)
        print(f"Encrypted text: {result}")
    elif action == 'd':
        result = decrypt_caesar(text, shift)
        print(f"Decryptedtext: {result}")
    else:
        print("Invalid action. Please enter 'e' for encrypt or 'd' for decrypt.")

#Якщо користувач вибрав шифр Віженера:
elif cipher_type == 'v':
    keyword = input("Enter keyword: ")

    if action == 'e':
        result = encrypt_vigenere(text, keyword)
        print(f"Encrypted text: {result}")
    elif action == 'd':
        result = decrypt_vigenere(text, keyword)
        print(f"Decrypted text: {result}")