A = int(input())

Cubos1 = A* A 

Cubos1 = Cubos1 - A
Cubos1 = Cubos1 - (A -1)
Cubos1 = Cubos1 - (A -1)
Cubos1 = Cubos1 - (A -2)

Cubos3 = 8

Cubos2 = (A* A - (4 + Cubos1) )* 3

Cubos0 = A* A*A -(Cubos1*6 + Cubos2+ Cubos3)

print(Cubos0)
print(Cubos1*6)
print(Cubos2)
print(Cubos3)