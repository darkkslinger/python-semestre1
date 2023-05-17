print ("Ingrese 3 lados de un triangulo", "\n")
a=float(input())
b=float(input())
c=float(input())
print()
sp= (a+b+c)/2
area=round(((sp*(sp-a)*(sp-b)*(sp-c))**0.5),2)
if a==b and b==c:
    print ("Es equilatero")
elif a==b or a==c or b==c:
    print ("Es isosceles")
else:
    print ("Es Escaleno")

print (f"el área es: {area }")