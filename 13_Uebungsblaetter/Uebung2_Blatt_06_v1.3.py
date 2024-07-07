
'''
Geben Sie einen rekursiven Algorithmus an, der eine Preorder-Traversierung 
auf einem Baum mit n Knoten in Zeit 𝛩(𝑛) ausführt.
'''

class binärbaum:
    def __init__(self, wert):
        self.wert = wert
        self.links = None
        self.rechts = None

baum = binärbaum(10)
baum.links = binärbaum(4)
baum.rechts = binärbaum(17)
baum.links.links = binärbaum(1)
baum.links.rechts = binärbaum(5)
baum.rechts.links = binärbaum(16)
baum.rechts.rechts = binärbaum(21)

def preorder(baum):
    if baum is not None:
        print(baum.wert)
        preorder(baum.links)
        preorder(baum.rechts)
    else:
        return
    
preorder(baum)