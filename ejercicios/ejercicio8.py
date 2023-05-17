
while True:
    mes=str(input("Ingrese mes del año: "))
    if mes == "diciembre" or mes == "enero" or mes == "febrero":
        print("El mes", mes,  "corresponde a la estacion verano")
        break
    elif mes == "marzo" or mes == "abril" or mes == "mayo":
        print("El mes", mes,  "corresponde a la estacion otoño")
        break
    elif mes == "junio" or mes == "julio" or mes == "agosto":
        print("El mes", mes,  "corresponde a la estacion invierno")
        break
    elif mes == "septiembre" or mes == "octubre" or mes == "noviembre":
     print("El mes", mes,  "corresponde a la estacion primavera")
     break
    else:
       print ("Mes Invalido")