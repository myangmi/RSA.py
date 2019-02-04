def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b / gcd(a, b)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def squaremultiply(a, b):
    x = a
    newStr = b[3:] #removes first 2 rando chars. skips first binary bit because it is already initialized
    for c in newStr:
        if c == '1':
            x = (x**2)
            x = x*a
        if c == '0':
            x = x**2
    return (x)



c = int(input("Enter the Ciphertext C: "))
p = int(input("Enter the private key (p,q) \nEnter p: "))
q = int(input("Enter q: "))
n = p*q
e = int(input("Enter e: "))
phiOfN = (int)(lcm(p-1,q-1))
print("Phi of n: {0}".format(phiOfN))
d = (int)(modinv(e, phiOfN))
print("d: {0}".format(d))
dp = (d % (p-1))
dq = (d % (q-1))
qInv = modinv(q, p)
print("qInv: {0}".format(qInv))
m1 = squaremultiply(c,bin(dp)) % p
m2 = squaremultiply(c,bin(dq)) % q
h = (qInv*(m1 - m2)) % p
m = m2 + h * q

print("m: {0}".format(m))