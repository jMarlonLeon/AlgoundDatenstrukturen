
def counting_sort(eingabefeld) :
    # Sortiert das übergebene eingabefeld u. liefer Ergebnis in neuem Feld
    anzahl_elemente = len(eingabefeld)
    groesster_wert = max(eingabefeld)
    
    # ----- initialisiere Rückgabefeld mit 0
    rueckgabefeld = [0 for zahl in range(anzahl_elemente) ]
    
    # ----- initialisiere Zählfeld mit 0
    zaehlfeld = [0 for zahl in range(groesster_wert+1) ]
    
    # ___-- zähle Vorkommnisse der einzelnen Werte im eingabefeld
    for element in range(anzahl_elemente):
        zaehlfeld[eingabefeld[element]] += 1
    
    # ----- bilde kummulative Summe
    for element in range(1, groesster_wert+1) :
        zaehlfeld[ element ] += zaehlfeld[element-1]
    
    # ----- Erstelle sortiertes Ausgabefeld
    for element in range(anzahl_elemente-1,-1, -1):
        rueckgabefeld[zaehlfeld[eingabefeld[element]]-1] = eingabefeld[ element]
        zaehlfeld[eingabefeld[element]] -= 1

# Erklärung erstelle sortiertes Ausgabefeld
# 1. zaehlfeld[eingabefeld[element]]-1 = ursprünglicher Index des Elementes im sortierten Feld
# 2. eingabefeld[ element] = Wert des Elementes
# 3. zaehlfeld[eingabefeld[element]] -= 1 = Dekrementiere den Zähler für den Wert des Elementes

    
    return rueckgabefeld


start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()

print("Unsortiertes Array:", start)

sortiert = counting_sort(eingabe)
print("Sortiertes Array:", sortiert)