
'''
Eingabe: Eine Sequenz von n Zahlen A = 〈a1, a2, ..., an〉 und ein Wert v

Ausgabe: Ein Index i mit v = A[i], falls v in A vorkommt, und den speziellen Wert NIL,
wenn der Wert in v nicht in A vorkommt.

Schreiben Sie ein Programm in Pseudocode für die lineare Suche, die eine Sequenz nach v durchsucht.
Implementieren Sie den Algorithmus anschließend in einer Programmiersprache Ihrer Wahl.
'''

from random import randint, random

n = randint(0,100)

A = [] * n
for i in range(n):
    A.append(randint(0,1000))

v = A[0]

print(f"n={n}")
print(f"v={v}")
print(f"A={A}")

def lineare_suche(A,v):
    i = 0
    while i < len(A):
        if A[i] == v:
            return i
        i += 1
    return "NIL"

print(lineare_suche(A,v))