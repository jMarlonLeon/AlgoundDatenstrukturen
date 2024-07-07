'''
Gegeben sei eine Hashtabelle der Größe 𝑚 = 1000 
und eine zugehörige Hashfunktion  h(𝑘) = ⌊𝑚 (𝑘 𝐴 mod 1)⌋ mit 𝐴 = (√5 − 1)/2. 
Berechnen Sie die Slots, auf die die Schlüssel 61, 62, 63, 64 und 65 abgebildet werden.
'''

from math import sqrt

GROESSE = 1000

hashtabelle = [ [] for _ in range(GROESSE)]

schluessel = [61,62,63,64,65]

def hashfunktion(schluessel):
    A = (sqrt(5)-1)/2
    hashwert = GROESSE *((schluessel * A) % 1)
    return int(hashwert)

def einfuegen(schluessel):
    index = hashfunktion(schluessel)
    hashtabelle[index].append(schluessel)
    print(schluessel,f"im Slot {index} eingefuegt")

def ausgeben():
    for i in range(GROESSE):
        if hashtabelle[i] != []:
            print(f"Slot{i} = {hashtabelle[i]}")

for x in schluessel:
    einfuegen(x)

ausgeben()