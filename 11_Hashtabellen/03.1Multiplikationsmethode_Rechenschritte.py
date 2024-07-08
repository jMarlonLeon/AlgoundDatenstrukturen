from math import sqrt

def hashfunktion(schluessel):
    A = (sqrt(5)-1)/2
    hashwert = (schluessel * A)
    modulo = hashwert % 1
    maltausend = modulo * 1000
    inte = int(maltausend)
    print(f"Konstante A:{A}")
    print(f"schluessel * A ={hashwert}")
    print(f"ans mod 1 ={modulo}")
    print(f"ans * 1000 = {maltausend}")
    print(f"int(ans)= {inte}")
    return inte

hashfunktion(62)