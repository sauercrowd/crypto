# RSA
import random

def get_random_relative_prime(phi_n):
  potential_e = random.randint(0, phi_n-1)
  if euclid(potential_e, phi_n) == 1:
    return potential_e
  return get_random_relative_prime(phi_n)

# generate keys, returns (e, d, n)
def rsa():
  p = 23
  q = 7
  phi_n = (q-1) * (p-1)
  e = get_random_relative_prime(phi_n)
  (_, d, _) = extended_euclid(e, phi_n)
  if d < 0:
    d = d % phi_n
  if d == e:
    return rsa()
  return (e, d , q*p)

def encrypt(message, e, n):
  while message > 0:
    m_part = message % (n-1)
    c_part =  (m_part ** e ) % n
    yield c_part
    message = int(message/(n-1))

def decrypt(c_parts, d, n):
  i = 0
  result = 0
  for c_part in c_parts:
    m_part = (c_part ** d) % n
    result += m_part * ((n-1)**i)
    i+=1
  return result

e, d, n = rsa()
print(e, d, n)

m = 1234567890
ciphertext = list(encrypt(m, e, n))
recovered_m = decrypt(ciphertext, d, n)
print(m, ciphertext, recovered_m)
