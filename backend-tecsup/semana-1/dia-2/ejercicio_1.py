a = int(input("ingresa la cantidad de numeros que quieres ingresar: "))
b = []
for i in range(a):
    b.append(int(input("ingresa numero "+str(i+1)+"  ")))

print("el mayor numero es: ",max(b))
print("el menor es: ",min(b))
print("el promedio es :",str(sum(b)/len(b)))