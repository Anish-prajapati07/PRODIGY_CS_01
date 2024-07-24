def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted = shifted - 26
                elif shifted < ord('a'):
                    shifted = shifted + 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted = shifted - 26
                elif shifted < ord('A'):
                    shifted = shifted + 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext
def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha()
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted = shifted - 2
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted = shifted - 2
            plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext
