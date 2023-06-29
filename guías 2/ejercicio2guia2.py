nombres=[]
while True:
    n = str(input("Ingrese nombres (Escriba 'Terminar' para terminar): "))
    nn = n.replace(" ","")
    if nn.lower() != "terminar":
        print(nn)
        nombres.append(nn)
    else:
        print("INGRESO DE NOMBRES FINALIZADO")
        break

def cantidadletras(nombres):
    letrastotal = 0
    for nombre in nombres:
        letrastotal += len(nombre)
    return(letrastotal)

letrastotal = cantidadletras(nombres)

print("Los nombres ingresados son ",nombres," y las letras totales son ",letrastotal)