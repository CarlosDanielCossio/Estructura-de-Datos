def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Ingrese el nro del cual desea saber el factorial: "))
print("El factorial de ",n,"es: ",fact(n))