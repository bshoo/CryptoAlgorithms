#!/usr/bin/env python3
from math import ceil

def encryptotp(pt, key):
    pt=pt.upper().replace(" ","")
    key=key.upper().replace(" ","")
    if len(key) < len(pt): key = key * int(ceil((len(pt)/len(key))))
    ct=""
    for i in range(len(pt)):
        ct += chr(((ord(pt[i])+ord(key[i]))%26)+65)
    print("\nEncrypted text: ",ct)
    return ct

def decryptotp(ct,key): 
    ct=ct.upper().replace(" ","")
    key=key.upper().replace(" ","")
    if len(key) < len(ct): key = key * int(ceil((len(ct)/len(key))))
    pt=""
    for i in range(len(ct)):
        pt += chr(((ord(ct[i])-ord(key[i]))%26)+65)
    print("\nPlain text(Decypted): ",pt)

decryptotp(encryptotp("security provided using cryptographic techniques","encipherment"),"encipherment")
