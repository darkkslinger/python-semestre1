print ("Ingrese 3 notas")
n1=float(input())
while n1<1 or n1>7:
    print ("Nota invalida. Ingrese una nota válida")
    n1=float(input())
n2=float(input())
while n2<1 or n2>7:
    print ("Nota invalida. Ingrese una nota válida")
    n2=float(input())
n3=float(input())
while n3<1 or n3>7:
    print ("Nota invalida. Ingrese una nota válida")
    n3=float(input())

promedio= round((n1*0.3)+(n2*0.4)+(n3*0.3),1)
print ("El promedio es: " ,promedio,"\n")

if promedio<4:
    print("El estudiante reprobó la asignatura")
elif promedio>4.0 and promedio<6.0:
    print("El estudiante aprobó la asignatura")
else:
    print("El estudiante aprobó con distinción")