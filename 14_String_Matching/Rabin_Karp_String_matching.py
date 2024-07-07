

#_---- Funktionsdefinition -----
def rabin_karp_matcher(text, muster, basis, prim):
    textlaenge   = len(text)
    musterlaenge = len(muster)
    hoechste_wertigkeit = (basis ** (musterlaenge-1)) & prim
    hashwert_muster = 0 # initialer Hashwert Muster
    hashwert_text   = 0 # initialer Hashwert Text
    
    # Vorverarbeitung
    for i in range (musterlaenge) :
        hashwert_muster = (basis * hashwert_muster + int(muster[i])) % prim
        hashwert_text   = (basis * hashwert_text   + int(text[i])  ) % prim
    print("Hash Muster:", hashwert_muster, "Hash Text (init):", hashwert_text)

    # Matching
    for verschiebung in range(textlaenge-musterlaenge+1):
        if hashwert_muster == hashwert_text:
            print("Hashwerte gleich bei Verschiebung", verschiebung)
            if muster == text[verschiebung:verschiebung+musterlaenge]:
                print("-->Muster tritt auf mit Verschiebung", verschiebung)
            else:
                print("--> Verschiebung", verschiebung, "ist unechter Treffer")
            if verschiebung < textlaenge-musterlaenge:
                hashwert_text = (basis * (hashwert_text - int(text[verschiebung]) * hoechste_wertigkeit) + int(text[verschiebung+musterlaenge])) % prim
                print("Hashwert Text (neu):", hashwert_text)
        else:
            print("Hashwerte ungleich bei Verschiebung", verschiebung)
            if verschiebung < textlaenge-musterlaenge:
                hashwert_text = (basis * (hashwert_text - int(text[verschiebung]) * hoechste_wertigkeit) + int(text[verschiebung+musterlaenge])) % prim
                print("Hashwert Text (neu):", hashwert_text)
            else:
                print("Ende des Textes erreicht")
    return None


muster = "31415"
text   = "2359023141526739921"
rabin_karp_matcher(text, muster, 10, 13)