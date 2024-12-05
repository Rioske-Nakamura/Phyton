A = [ int(x) for x in input( ).split(" ") ]

if A[0] * A[0] == A[1] * A[1] + A[2] * A[2]:
    pi=3
    raio = A[2]/2
    areaC = pi * raio * raio
    areaT = A[1] * A[2] /2

    print(f"AREA = {int(areaT + areaC/2)}")

else:
    print("Nao eh retangulo!")
