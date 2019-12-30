# RSA
import random

def get_random_relative_prime(phi_n):
  potential_e = random.randint(0, phi_n-1)
  if euclid(potential_e, phi_n) == 1:
    return potential_e
  return get_random_relative_prime(phi_n)

# generate keys, returns (e, d, n)
def rsa():
  p = 47
  q = 71
  phi_n = (q-1) * (p-1)
  e = get_random_relative_prime(phi_n)
  (_, d, _) = extended_euclid(e, phi_n)
  if d < 0:
    d = d % phi_n
  if d == e:
    return rsa()
  n = q*p
  return ((e, n), (d, n))

def encrypt(message, public_key):
  (e, n) = public_key
  ciphertext = ""
  for c in message:
    ciphertext += chr((ord(c) ** e ) % n)
  return ciphertext

def decrypt(ciphertext, private_key):
  (d, n) = private_key
  message = ""
  for c in ciphertext:
    message += chr((ord(c) ** d) % n)
  return message

public_key, private_key = rsa()

m = "Hello, World!"
ciphertext = encrypt(m, public_key)
recovered_m = decrypt(ciphertext, private_key)

import base64

print("public key:", public_key[0], "private key:", private_key[0])
print("input:", m)
print("encrypted:", (base64.b64encode(str.encode(ciphertext))))
print("decrypted:", recovered_m)
