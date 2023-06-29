def comprar():
    costo_total=0
    while True:
        precio=0
        print('Ingrese el costo de los productos que quiere comprar (sin puntos ni comas), escriba un 0 para salir')
        precio=int(input('$'))
        if precio==0:
            break
        elif precio>0:
            costo_total+=precio
            print(f'Usted lleva un costo total de: ${costo_total} pesos')
        else:
            continue
    return costo_total

def montovuelto(total,entregado):
    vuelto=entregado-total
    return vuelto

def devolver_vuelto(vuelto):
    billetes_monedas= [20000,10000,5000,2000,1000,500,100,50,10]
    lista = []
    for i in billetes_monedas:
        cantidad = vuelto // i
        if cantidad > 0:
            lista.extend([i]*cantidad)
            vuelto=vuelto%i
    return lista

def calculo_billetes_monedas(lista):
    string=[]
    billetes={
        '$20.000 pesos':lista.count(20000),
        '$10.000 pesos':lista.count(10000),
        '$5.000 pesos':lista.count(5000),
        '$2.000 pesos':lista.count(2000),
        '$1.000 pesos':lista.count(1000),
    }
    monedas={
        '$500 pesos':lista.count(500),
        '$100 pesos':lista.count(100),
        '$50 pesos':lista.count(50),
        '$10 pesos':lista.count(10)
    }
    for i,j in billetes.items():
        if j>1:
            string.append(f'{j} billetes de {i}')
        elif j==1:
            string.append(f'{j} billete de {i}')
    for i,j in monedas.items():
        if j>1:
            string.append(f'{j} monedas de {i}')
        elif j==1:
            string.append(f'{j} moneda de {i}')
    string=', '.join(string)
    return string

def cajero():
    costo_total=comprar()
    print(f'Su monto a pagar es de: ${costo_total} pesos')
    while True:
        entregado = int(input('Monto entregado: $'))
        if entregado < costo_total:
            print('Monto insuficiente')
        else:
            vuelto = montovuelto(costo_total,entregado)
            print(f'Su vuelto es ${vuelto} pesos')
            lista = devolver_vuelto(vuelto)
            print(f'Por lo que le corresponde: \n{calculo_billetes_monedas(lista)}.')
            break

cajero()
