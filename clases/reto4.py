name1 = input("Ingrese nombre del paciente 1: ")
edad1 = int(input("Ingrese la edad del paciente 1: "))
if edad1<=0 or edad1>=200:
    print ("Edad invalida. Ingrese una edad válida. 'número positivo y sin decimales'")
    edad1 = int(input("Ingrese la edad del paciente 1: "))
peso1 = float(input("Ingrese el peso del paciente 1: "))
if peso1<=0:
    print ("Peso invalido. Ingrese un peso válido")
    peso1 = float(input("Ingrese el peso del paciente 1: "))
estatura1 = float(input("Ingrese la estatura del paciente 1: "))
if estatura1<=0:
    print ("Estatura invalida. Ingrese una estatura válida")
    estatura1 = float(input("Ingrese la estatura del paciente 1: "))
tupla_1=(name1, edad1, peso1, estatura1,"\n")

print (tupla_1,"\n")

name2 = input("Ingrese nombre del paciente 2: ")
edad2 = int(input("Ingrese la edad del paciente 2: "))
if edad2<=0 or edad2>=200:
    print ("Edad invalida. Ingrese una edad válida")
    edad2 = int(input("Ingrese la edad del paciente 2: "))
peso2 = float(input("Ingrese el peso del paciente 2: "))
if peso2<=0:
    print ("Peso invalido. Ingrese un peso válido")
    peso2 = float(input("Ingrese el peso del paciente 2: "))
estatura2 = float(input("Ingrese la estatura del paciente 2: "))
if estatura2<=0:
    print ("Estatura invalida. Ingrese una estatura válida")
    estatura2 = float(input("Ingrese la estatura del paciente 2: "))
tupla_2=(name2, edad2, peso2, estatura2,"\n")

print (tupla_2,"\n")

name3 = input("Ingrese nombre del paciente 3: ")
edad3 = int(input("Ingrese la edad del paciente 3: "))
if edad3<=0 or edad3>=200:
    print ("Edad invalida. Ingrese una edad válida")
    edad3 = int(input("Ingrese la edad del paciente 3: "))
peso3 = float(input("Ingrese el peso del paciente 3: "))
if peso3<=0:
    print ("Peso invalido. Ingrese un peso válido")
    peso3 = float(input("Ingrese el peso del paciente 3: "))
estatura3 = float(input("Ingrese la estatura del paciente 3: "))
if estatura3<=0:
    print ("Estatura invalida. Ingrese una estatura válida")
    estatura3 = float(input("Ingrese la estatura del paciente 3: "))
tupla_3=(name3, edad3, peso3, estatura3,"\n")

print (tupla_3,"\n")

print(tupla_1, tupla_2, tupla_3)