#!/usr/bin/env python3

import numpy as np

k = []
for i in input("Enter word key to for play fair: ").upper():
    if i not in k: k.append(i)

if "J" in k:
    if "I" in k:
        k.remove("K")
    else:
        k[k.index("J")] = "I"
alpha = [chr(i) for i in range(65,91) if i!=74]

for i in k:
    try:
        alpha.remove(i)
    except:
        continue
matrix = np.array(k+alpha).reshape(5,5)
print(matrix)

'''
def encrypt(plain):
  plain = list(plain.upper().strip())
  while(" " in plain):
    plain.remove(" ")
  i=0
  enc = ""
  while(i<len(plain)):
    a=plain[i]
    b=plain[i+1]
    if a==b:
      b="X"
      i+=1
    else:
      i+=2
     
'''


def play(pt, matrix):
    d2 = []
    i = 0
    n = len(pt)
    while i<n:
        if i==n-1:
            d2.append(pt[i]+"X")
            break
        elif pt[i]!=pt[i+1]:
            d2.append(pt[i]+pt[i+1])
            i+=2
        else:
            d2.append(pt[i]+"X")
            i+=1
    ct = ""
    import numpy as np
    for i in d2:
        index1 = np.where(matrix == i[0])
        index2 = np.where(matrix == i[1])
        if index1[0] == index2[0]:
            ct += matrix[index1[0], (index1[1]+1)%5][0]
            ct += matrix[index2[0], (index2[1]+1)%5][0]
        elif index1[1] == index2[1]:
            ct += matrix[(index1[0]+1)%5, index1[1]][0]
            ct += matrix[(index2[0]+1)%5, index2[1]][0]
        else:
            ct += matrix[index1[0], index2[1]][0]
            ct += matrix[index2[0], index1[1]][0]
    return ct



pt = input("Enter text to encrypt ").upper().replace(" ","").replace("J","I")
ct = play(pt, matrix)
print(ct)
print("Decrypted: ",play(ct, matrix))












