from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import binascii
import os

# datas to cipher

data1 = b'0000000000000000000000000000000000000000000000000000000000000000'
data2 = b'0000000000000000000000000000000000000000000000000000000000000000'
data3 = b'0000000000000000000000000000000000000000000000000000000000000000'

# block size
BLOCK_SIZE = 16 # Bytes


# encrypt with AES and electronic code book operation

# key
key = b"thisissecretkey1"

# initialize cipher
cipher1 = AES.new(key, AES.MODE_ECB)

ciphered_data1 = cipher1.encrypt(data1)
# print ciphered message and in hex format
print("This is AES and ECB ciphered: ")
print(ciphered_data1)
print("This is AES and ECB ciphered in hex: " + ciphered_data1.hex())
print("\n")


# encrypt with AES and CBC 


iv = b'asdertikolpasfnt'
# initialize cipher
cipher2 = AES.new(key, AES.MODE_CBC, iv)
# cipher data
ciphered_data2 = cipher2.encrypt(data2)
# print ciphered message and in hex format
print("This is AES and CBC ciphered: ")
print(ciphered_data2)
print("This is AES and CBC ciphered in hex: " + ciphered_data2.hex())
print("\n")



# encrypt with AES and CTR


# initialize cipher
ctr = Counter.new(128, initial_value=int(binascii.hexlify(iv), 16))
cipher3 = AES.new(key, AES.MODE_CTR, counter=ctr)
# cipher data
ciphered_data3 = cipher3.encrypt(data3)
# print ciphered message and in hex format
print("This is AES and CTR ciphered: ")
print(ciphered_data3)
print("This is AES and CTR ciphered in hex: " + ciphered_data3.hex())



print("data 1", len(data1))
print("data 2",  len(data2))
print("data 3",  len(data3))

print("data 1 cip", len(ciphered_data1.hex()))
print("data 2 cip", len(ciphered_data2.hex()))
print("data 3 cip", len(ciphered_data3.hex()))