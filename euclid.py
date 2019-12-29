def euclid(a, b):
  if b == 0:
    return a
  return euclid(b, a % b)

def extended_euclid(a, b):
  if b == 0:
    return (a, 1, 0)
  else:
    (dp, xp, yp) = extended_euclid(b, a % b)
    d, x, y = dp, yp, xp - (int(a/b) * yp)
    return (d, x, y)
