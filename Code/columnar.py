#!/usr/bin/env python3

def encrypt(pt, key):
    print("Plain text: ",pt)
    key = [int(i) for i in key]
    cols = max(key)
    i = 0
    ct = ""
    tab = ["" for i in range(cols)]
    for letter in pt:
        tab[i] += letter
        i = (i+1)%cols
    for k in range(cols):
        x=min(key)
        ct+=tab[key.index(x)]
        key[key.index(x)]=99999
    print(tab)
    print("Encrypted: ",ct)
    return ct

encrypt("Hello","2314")
