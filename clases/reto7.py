def frase(a):
    p=a.split()
    print(p)
    long=len(a)
    dic={
        'palabras':p,
        'longitud':long
    }
    print(dic)
frase(input('Escriba una frase para devolver un diccionario con sus palabras y longitud: '))

