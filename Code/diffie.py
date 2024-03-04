#!/usr/bin/env python3
'''Shashank B Sharma, PES1PG22CA184'''
def alpha(q):
    for i in range(2,q):
        x = set()
        for j in range(1,q):
            x.add((i**j)%q)
        if len(x)==q-1:
            return i


def generate(q, alpha, xa = None, xb = None):
    from random import randint
    if not xa:
        xa = randint(2, q)
    ya = (alpha**xa)%q
    if not xb:
        xb = randint(2, q)
    yb = (alpha**xb)%q
    keya = (yb**xa)%q
    keyb = (ya**xb)%q
    print("q: ",q)
    print("Alpha: ",alpha)
    print("Private key, Public key of A: ",xa, ya)
    print("Private key, Public key of B: ", xb, yb)
    print("Keys: ", keya, keyb)

#generate(97, alpha(97))
#generate(17, 3)
#print(alpha(37))
