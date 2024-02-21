#!/usr/bin/env python3
'''Shashank B Sharma, PES1PG22CA184'''
from math import gcd
def rsa(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e, d = find_de(n, phi)
    print(e)
    print("Public E, N: ", e, n)
    print("Private D, N: ",d, n)
    m = 100
    print(f"M: {m}")
    c=(m**e)%n
    print("Encrpyted: ",c)
    print("Decrypted: ",(c**d)%n)
    return e, d, n

def find_de(n, phi):
    for i in range(3, n**2):
        if gcd(i, phi) == 1:
            e=i
            for j in range(2, n**2):
                if (j*e)%phi == 1:
                    d = j
                    break

    #for i in range(2,n**2):
        #print(i)
        #if (i*e)%phi == 1:
         #   d = i
          #  break
    return e, d

def encrypt(e, n):
    pt = input("Enter plain Text to encrypt ")
    ct = ""
    for i in pt:
        ct += chr((ord(i)**e)%n)
    print("Cipher Text: ",ct)
    return ct

def decrypt(d, n, ct):
    pt = ""
    for i in ct:
        pt += chr((ord(i)**d)%n)
    print("Decrypted: ",pt)

if __name__ == "__main__":
    e, d, n = rsa(13, 17)
    print(e, d, n)
    decrypt(d, n, encrypt(e, n))















