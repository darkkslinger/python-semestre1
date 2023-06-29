def obtener_numeros(cantidad):
    numeros = []
    for i in range (cantidad):
        numero=float(input(f"ingrese el numero {i+1}: "))
        numeros.append(numero)
    return numeros

def sumanumeros(n):
    suma= sum(n)
    return suma

def sumapar(n):
    suma = 0
    for num in n:
        if num%2==0:
            suma+=num
    return suma

def sumainpar(n):
    suma = 0
    for num in n:
        if num%2!=0:
            suma+=num
    return suma

c_n = int(input("¿Cuántos números desea operar?: "))
nums = obtener_numeros(c_n) 
print(f"La suma de todos los números es: {sumanumeros(nums)}")
print(f"La suma de todos los números pares es: {sumapar(nums)}")
print(f"La suma de todos los números impares es: {sumainpar(nums)}")