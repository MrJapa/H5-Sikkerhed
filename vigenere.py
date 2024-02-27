import unittest

def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key[i % key_length].upper()) - 65
            if plain_text[i].isupper():
                cipher_text += chr((ord(plain_text[i]) + shift - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(plain_text[i]) + shift - 97) % 26 + 97)
        else:
            cipher_text += plain_text[i]
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ""
    key_length = len(key)
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key[i % key_length].upper()) - 65
            if cipher_text[i].isupper():
                plain_text += chr((ord(cipher_text[i]) - shift - 65) % 26 + 65)
            else:
                plain_text += chr((ord(cipher_text[i]) - shift - 97) % 26 + 97)
        else:
            plain_text += cipher_text[i]
    return plain_text

def main():
    key = "KEY"
    plain_text = "Hello, World!"
    cipher_text = vigenere_encrypt(plain_text, key)
    print("Cipher text: ", cipher_text)
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print("Decrypted text: ", decrypted_text)

class TestVigenere(unittest.TestCase):
    def test_vigenere(self):
        self.assertEqual(vigenere_encrypt("Hello, World!", "KEY"), "Rijvs, Ambpb!")
        self.assertEqual(vigenere_decrypt(vigenere_encrypt("Hello, World!", "KEY"), "KEY"), "Hello, World!")

if __name__ == "__main__":
    main()
    #unittest.main()