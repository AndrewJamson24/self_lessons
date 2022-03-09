import sys
 
def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key [ i % len(key) ]
            i += 1
        else:
            padded_key += ' '


    return padded_key

def _encrypt_decrypt_char(plaintext_char,key_char, mode = 'encrypt'):
    
    if plaintext_char.isalpha():
        first_alpha_letter = "A"
            
        old_char_pos = ord(plaintext_char) - ord(first_alpha_letter)
        key_char_pos = ord(key_char.lower()) - ord('a')

        if mode == 'encrypt':
            new_char_pos = (old_char_pos + key_char_pos) % 26
        else:
            new_char_pos = (old_char_pos - key_char_pos + 26) % 26
        
        return chr(new_char_pos + ord(first_alpha_letter))
    return plaintext_char

def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext,key)
    for plaintext_char , key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char , key_char in zip(ciphertext,padded_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char,key_char, mode ='decrypt')
    return plaintext



def menu():
    while True:
        choice = input("""
            1.Criptarea
            2.Decriptarea
            3.Iesire
            
        Alegeti Obtiunea:  """)

        if choice == "1":
            plaintext = input("Introduceti un mesaj: ").upper().replace(" ","")
            key = input("Introduceti o cheie: ")
            ciphertext = encrypt(plaintext, key).upper()
            print(f'Textul criptat: {ciphertext}')
        elif choice == "2":
            plaintext = input("Introduceti un mesaj: ").upper().replace(" ","")
            key = input("Introduceti o cheie: ")
            decrypted_plaintext = decrypt(plaintext,key).upper()
            print(f'Textul Decriptat: {decrypted_plaintext}')
        elif choice == "3":
            print("Iesire...")
            sys.exit()
      
        

menu()

