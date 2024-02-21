#!/usr/bin/env python3

def encrypt(pt, depth=1):
    print(f"Plain text(Depth:{depth}): ",pt)
    pt=pt.upper().replace(" ","")
    for i in range(depth):
        ct = pt[::2]+pt[1::2]
        pt=ct
    print("Encrypted: ",ct)
    return ct


def decrypt(ct, depth=1):
    print("Ct: ",ct)
    for i in range(depth):
        pt = ""
        len2 = int(len(ct)/2)
        for j in range(len2):
            try:
                pt += ct[0+j]+ct[len2+j]
            except:
                break
        ct = pt
    print("Decrypted: ",pt)    


decrypt(encrypt("security at risk",4),4)
