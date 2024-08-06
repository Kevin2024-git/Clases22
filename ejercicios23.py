print("")
Not1 = int(input("Ingrese la primera nota: "))
print("")
Not2 = int(input("Ingrese la segunda nota: "))
print("")
Not3 = int(input("Ingrese la tercera nota: "))
print("")
Not4 = int(input("Ingrse la cuarta nota: "))
print("")

Sum = Not1 + Not2 + Not3 + Not4

Prom = Sum/4

print("Su puntuacion es de: ")
print(Prom)
print("")

if Prom <= 59:
    print("Su puntuacion lo coloca en el grupo (E)")
    print("")
elif Prom < 70:
    print("Su puntuacion lo coloca en el grupo (D)")
    print("")
elif Prom < 80:
    print("Su puntuacion lo coloca en el grupo (C)")
    print("")
elif Prom < 90:
    print("Su puntuacion lo coloca en el grupo (B)")
    print("")
elif Prom < 101:
    print("Su puntuacion lo coloca en el grupo (A)")
    print("")