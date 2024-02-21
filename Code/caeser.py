#!/usr/bin/env python3

try:
    p = input("Enter text to encrypt: ")
    k = int(input("\nEnter key: "))
    dct = {chr(i):chr((((i-65)+k)%26)+65) for i in range(65, 91)}
    dct[' ']=' '
    strng = ""
    for i in p:
        strng += dct[i.upper()]
    print("Ciphre text: ",strng)
except Exception as e:
    print("Wrong input ",e.__doc__)
