def pot(b,e):
    if(e==0):
        return 1
    else:
        return b*pot(b,e-1)
b=int(input("Ingrese la base: "))
e=int(input("Ingrese el exponente"))
print("El resultado es: ",pot(b,e))
