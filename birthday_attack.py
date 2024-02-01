import hashlib
import random
import secrets
import string
import time
# code edited from https://www.geeksforgeeks.org/birthday-attack-in-cryptography/

# Script to create partial birthday attack

# generate random string of length given as a parameter
def generate_random_string(n):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(n))

# birthday attack with md5 to detect partial collission for 2 first bytes
#@profile for memory analysis
def birthday_attack_md5():
    hash_dict = {}
    whole_hash = {}
    attempts = 0
 
    while True:
        attempts += 1
        random_string = generate_random_string(10)
        hash_value = hashlib.md5(random_string.encode()).hexdigest()
        
        # partial attack for 8 first chars
        hash_value_partial = hash_value[0:8]
        if hash_value_partial in hash_dict:
            print(f"Collision found after {attempts} attempts!")
            print(f"Original String 1: {hash_dict[hash_value_partial]}")
            print(f"Original String 1 whole hash: {whole_hash[hash_value_partial]}")
            print(f"Original String 2: {random_string}")
            print(f"Original String 2 whole hash: {hash_value}")
            print(f"Hash value partial: {hash_value_partial}")
            break
        
        whole_hash[hash_value_partial] = hash_value
        hash_dict[hash_value_partial] = random_string


def birthday_attack_sha1():
    hash_dict = {}
    whole_hash = {}
    attempts = 0
 
    while True:
        attempts += 1
        random_string = generate_random_string(10)
        hash_value = hashlib.sha1(random_string.encode()).hexdigest()
        
        # partial attack for 8 first chars
        hash_value_partial = hash_value[0:8]
        if hash_value_partial in hash_dict:
            print(f"Collision found after {attempts} attempts!")
            print(f"Original String 1: {hash_dict[hash_value_partial]}")
            print(f"Original String 1 whole hash: {whole_hash[hash_value_partial]}")
            print(f"Original String 2: {random_string}")
            print(f"Original String 2 whole hash: {hash_value}")
            print(f"Hash value partial: {hash_value_partial}")
            break
        
        whole_hash[hash_value_partial] = hash_value
        hash_dict[hash_value_partial] = random_string


def birthday_attack_sha3():
    hash_dict = {}
    whole_hash = {}
    attempts = 0
 
    while True:
        attempts += 1
        random_string = generate_random_string(10)
        hash_value = hashlib.sha3_224(random_string.encode()).hexdigest()
        
        # partial attack for 8 first chars
        hash_value_partial = hash_value[0:8]
        if hash_value_partial in hash_dict:
            print(f"Collision found after {attempts} attempts!")
            print(f"Original String 1: {hash_dict[hash_value_partial]}")
            print(f"Original String 1 whole hash: {whole_hash[hash_value_partial]}")
            print(f"Original String 2: {random_string}")
            print(f"Original String 2 whole hash: {hash_value}")
            print(f"Hash value partial: {hash_value_partial}")
            break
        
        whole_hash[hash_value_partial] = hash_value
        hash_dict[hash_value_partial] = random_string


start = time.time()
birthday_attack_md5()
end = time.time()

print("Time used: ", end-start)