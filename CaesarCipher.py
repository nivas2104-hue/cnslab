#CaesarCipher

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar_cipher(msg, k):
 cipher_text = ""
 for ch in msg:
 	if ch.isalpha():
		cipher_text += uppercase_letters[(uppercase_letters.index(ch) + k) % 26]
 	else:
 		cipher_text += ch
 print("cipher text:",cipher_text)

 plain_text = ""
 for ch in cipher_text:
 	if ch.isalpha():
 		plain_text += uppercase_letters[(uppercase_letters.index(ch) - k) % 26]
 	else:
 		plain_text += ch
 print("plain text:",plain_text)

message = input("enter the message: ").upper()
key = int(input("enter the key: "))
caesar_cipher(message, key)