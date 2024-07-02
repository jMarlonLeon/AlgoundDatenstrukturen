
def bucket_sort(feld):
    anzahl_elemente = len(feld)
    anzahl_faecher = 10
    feld_sortiert = []

    # erzeuge eine leere Liste (ein neues 'regal') mit anzahl. _faecher
    # Elementen, in der die buckets später einsortiert werden können
    regal = {x:[] for x in range(anzahl_faecher) }

    # lege Elemente der Reihe nach im richtigen Fach ab
    for feld_index in range(anzahl_elemente) :
        fach = int(anzahl_faecher*feld[feld_index])
        regal[fach].append(feld[feld_index])
    
    # sortiere die Elemente innerhalb eines Faches und füge sie dem
    # (anfangs leeren) sortierten Feld hinzu
    # (zur Sortierung wird hier der Einfachheit halber sort() genutzt)
    for fach in range (anzahl_faecher):
        regal[fach].sort()
        feld_sortiert += regal[ fach]

    return feld_sortiert

start = [3,6,1,7,5,2,9,8]
eingabe = start.copy()

print("Unsortiertes Array:", start)

sortiert = bucket_sort(eingabe)
print("Sortiertes Array:", sortiert)