import hashlib
import random
import secrets
import string
import time

# Script to find partial preimage

def generate_random_string(n):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(n))


#@profile for memory usage analysis
def find_preimage(H):
    attempts = 0
    while True:
        attempts += 1
        random_string = generate_random_string(10)
        hash_value = hashlib.sha1(random_string.encode()).hexdigest()

        if hash_value[:4] == H[:4]:
            print("Random string:", random_string)
            print("hash value:", hash_value)
            print("attempts ", attempts)
            break


def find_hash_starting_zeros():

    while True:
        message = generate_random_string(10)
        message_hash = hashlib.sha1(message.encode()).hexdigest()
        if message_hash[0] == "0":
            break 
    
    return message, message_hash

plaintext1, cipher1 = find_hash_starting_zeros()

print("Original message: ", plaintext1)
print("Original message hash", cipher1)

start = time.time()
find_preimage(cipher1)
end = time.time()

print("Time used: ", end-start)
