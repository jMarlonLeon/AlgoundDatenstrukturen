
# Naives String-Matching Algorithmus 
# T = Text
# P = gesuchtes Muster (Pattern)

def naives_string_matching(T, P):
    n = len(T) # Länge vom Text
    m = len(P) # Länge von Pattern

    for i in range(n-m+1):
        j = 0
        while j < m and T[i+j] == P[j]:
            j += 1
        if j == m:
            print(f"Pattern gefunden bei Index {i}")

def naives_string_matching_2(T, P):
    n = len(T) # Länge vom Text
    m = len(P) # Länge von Pattern

    for i in range(n-m+1):
        if T[i:i+m] == P:
            print(f"Pattern gefunden bei Index {i}")

def naives_string_matching_3(T,P):
    n = len(T) # Länge vom Text
    m = len(P) # Länge von Pattern
    gefunden = 0

    for i in range(n-m+1):
        for x in range(i,i+m):
            if T[x] != P[x-i]:
                gefunden = 0
            else:
                gefunden = 1
        if gefunden == 1:
            print(f"Pattern gefunden bei index {i}")
            return i
    return None


string="ABCDEFGHIJKL"
suche="GHI"

naives_string_matching(string, suche)
naives_string_matching_2(string, suche)
naives_string_matching_3(string, suche)