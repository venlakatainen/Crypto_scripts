from Crypto.Cipher import Salsa20
import time

# use salsa20 to cipher two texts with the same nonce and key -> unsecure

# measure the time
start = time.time()

# plaintext to cipher

plaintext = b'Try to cipher this'
secret = b'*Thirty-two byte (256 bits) key*'

cipher = Salsa20.new(key=secret)
nonce = cipher.nonce
print("nonce", nonce)
msg = nonce + cipher.encrypt(plaintext)

print("message1 as cipher", msg)


# another message to cipher with different key but the same nonce.
plaintext2 = b'Try to cipher thia'
key2 = b'*twenty-one plus (128 byte) new*'
cipher2 = Salsa20.new(key=key2)
msg2 = nonce + cipher2.encrypt(plaintext2)
print("message2 as cipher", msg2)

end = time.time()
print(end - start)