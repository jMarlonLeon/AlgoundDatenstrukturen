'''
Ausgabe aller Knoten
Betrachten Sie das Einfügen der Schlüssel 10, 22, 31, 4, 15, 28, 17, 88, 59 in 
eine Hashtabelle mit offener Adressierung der Länge 11. 
Die Hilfshashfunktion sei h ́(𝑘) = 𝑘 mod 𝑚. 
Illustrieren Sie das Einfügen der Schlüssel mithilfe des linearen Sondierens.
'''

GROESSE = 11

hashtabelle = [None] * GROESSE

schluessel = [10,22,31,4,15,28,17,88,59]

def hash_funktion(schluessel):
    return schluessel % GROESSE

def lineare_sondierung(index, i):
    return (index + i ) % GROESSE

def einfuegen(schluessel):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = lineare_sondierung(index, i)
        if hashtabelle[probe_index] is None or hashtabelle[probe_index] == schluessel:
            hashtabelle[probe_index] = schluessel
            print("eingefuegt",schluessel,"an",probe_index)
            return True
        i+=1 
    return False

def ausgeben():
    for element in range(0,GROESSE-1):
        print(element,hashtabelle[element])

for x in schluessel:
    einfuegen(x)

print(hashtabelle)
