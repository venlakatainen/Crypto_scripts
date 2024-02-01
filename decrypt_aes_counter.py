from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import binascii
import os

# find cipher when knowing 2 plaintexts and one cipher text

# encypted message

encrypted = "a7896ad1b2f7da8d40b33d1438e04a839a88b5c9a97625fe5017a5e1fb542072595d804d5ad1a3af11ea7244a39d76cde1"

# change hex numbers to decimal

encrypted_dec = []

for i in range(0,len(encrypted),2):
    encrypted_dec.append(int(encrypted[i]+encrypted[i+1],16))



plaintext = "Move the tables to the patio as soon as possible!"

# change plaintext to ascii

plaintext_ascii = [ord(ele) for sub in plaintext for ele in sub]


# message to cipher

plaintext_to_cipher = "Move the chairs to the house as soon as possible!"


# change to ascii

plaintext_cipher_ascii = [ord(ele) for sub in plaintext_to_cipher for ele in sub]


# list for xorred letters

decrypted = []

# xor new plaintext and previous xorred

for i in range(0,len(plaintext_cipher_ascii)):
    decrypted.append(hex(plaintext_cipher_ascii[i]^(plaintext_ascii[i]^encrypted_dec[i])))


print(decrypted)






