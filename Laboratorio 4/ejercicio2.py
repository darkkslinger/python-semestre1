a=[20,22,43,12,18]
b=[17,21,25,12,22,13]
c=[11,29,20,27,23,12,22]

def valores_comun (lista1, lista2, lista3):
    lista_comun = []
    for i in lista1:
        if i in lista2 and lista3:
            lista_comun.append(i)
    return lista_comun

def concatenar (a,b,c):
    d = a + b + c
    return d

def eliminar_duplicados (lista):
    lista = list (set(lista))
    return lista

def ordenar (lista):
    lista_ordenada = lista.sort(reverse=True)
    return lista_ordenada

def reemplazar_posicion7 (lista):
    num = lista[6]
    lista.insert(num,100)
    return lista

print(f'Los valores comunes son: {valores_comun(a,b,c)}')
li=concatenar(a,b,c)
print(f'Una sola lista: {li}')
eliminar_duplicados(li)
print(f'Lista sin duplicados: {li}')
ordenar(li)
print(f'Lista ordenada: {li}')
reemplazar_posicion7(li)
print(f'Reemplzar posicion 7: {li}')