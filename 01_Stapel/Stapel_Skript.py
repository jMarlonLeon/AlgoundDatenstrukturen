# LIFO

# Nutzung einer Liste als Stack
import sys

# Stack erzeugen
stack = []

# Anhängen (einfügen) über append()
stack.append('a')
stack.append('b')
stack.append('c')

# Stack ausgeben
print("Stack:", stack)

# Elemente vom Stack nehmen über pop()
temp = stack.pop()
print(temp, "vom Stack genommen")

# alle Elemente vom Stack nehmen
laenge = len(stack)

for i in range(laenge):
    temp = stack.pop()
    print(temp, "vom Stack genommen")
    print("Stack:", stack)

# Stack-Empty-Abfrage
def Stack_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    

print("Stack-Empty ?:", Stack_empty(stack))
