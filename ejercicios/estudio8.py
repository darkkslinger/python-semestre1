#Dada una cadena de texto, contar cuántas vocales contiene.
cadena= "hola Soy Daniel".lower()
vocales=['a','e','i','o','u']
#   c_vocales=contador de vocales
c_vocales=0

for i in cadena:
    if i in vocales:
        c_vocales +=1

print("la cadena contiene" ,c_vocales, "vocales")

#cadena= str(input("ingrese una frase: ").lower())
#vocales=['a','e','i','o','u']
#  c_vocales=contador de vocales
#c_vocales=0

#for i in cadena:
    #if i in vocales:
        #c_vocales +=1

#print("la cadena contiene" ,c_vocales, "vocales")