def ingresar_año():
    print('--- Comprobar si el año es bisiesto ---')
    año = int(input('Ingrese el año: '))
    return año

def año_bisiesto(año):
    if año%4==0:
        print(f'El año {año} es un año bisiesto')
    else:
        print(f'El año {año} no es un año bisiesto')
        
n=ingresar_año()
año_bisiesto(n)