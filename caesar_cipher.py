def caesar_cipher(text, key, mode):
    result = []
    for char in text:
        if char.isalpha():
            shift = key % 26
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            else:
                raise ValueError("Mode should be 'encrypt' or 'decrypt'.")
            result.append(shifted_char)
        else:
            result.append(char)
   return ''.join(result)
  def main():
    while True:
        print("Choose an option:")
        print("e for Encrypt a message")
        print("d for Decrypt a message")
        print("x fore Exit")
        choice = input("Enter your choice what you want to do (e, d or x): ")
        if choice == 'e':
            plaintext = input("Enter the message to encrypt: ").strip()
            key = int(input("Enter the encryption key (an integer): "))
            encrypted_message = caesar_cipher(plaintext, key, 'encrypt')
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            ciphertext = input("Enter the message to decrypt: ").strip()
            key = int(input("Enter the decryption key (an integer): "))
            decrypted_message = caesar_cipher(ciphertext, key, 'decrypt')
            print(f"Decrypted message: {decrypted_message}")
        elif choice == 'x':
            print("Exit")
            break
        else:
            print("Invalid choice. Please enter e, d, or x.")
if __name__ == "__main__":
    main()
