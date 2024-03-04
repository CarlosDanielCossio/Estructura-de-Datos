class Circunferencia:
    def __init__(self, radio):
        self.a = (radio*radio)*3.1416
        
r=float(input("Ingresa el radio: "))
area = Circunferencia(r)
print("El area de su circunferencia es: ",area.a)