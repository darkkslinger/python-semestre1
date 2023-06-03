#Calcular el factorial de un número dado por el usuario.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero para calcular su factorial: "))

# Verificar si el número es válido (no negativo)
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial_numero = factorial(numero)
    print(f"El factorial de {numero} es: {factorial_numero}")
