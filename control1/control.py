def dibujar_figura(opcion, tamaño):
    """
    Función para imprimir la figura seleccionada con un tamaño de matriz dado.
    Se utiliza '#' para el fondo y '0' para las posiciones de las figuras.
    """
    # Crear una matriz de tamaño x tamaño llena de '#'
    matriz = [['#' for _ in range(tamaño)] for _ in range(tamaño)]
    
    if opcion == 1:  # Diagonal principal (↘)
        for i in range(tamaño):
            matriz[i][i] = '0'  # Colocar '0' en la diagonal principal
    
    elif opcion == 2:  # Diagonal secundaria (↙)
        for i in range(tamaño):
            matriz[i][tamaño - i - 1] = '0'  # Colocar '0' en la diagonal secundaria
    
    elif opcion == 3:  # Ambas diagonales
        for i in range(tamaño):
            matriz[i][i] = '0'  # Diagonal principal
            matriz[i][tamaño - i - 1] = '0'  # Diagonal secundaria
        
        # Evitar duplicados en el centro de la matriz
        centro = tamaño // 2
        matriz[centro][centro] = '0'  # Colocar '0' en el centro
    
    elif opcion == 4:  # Triángulo en cruz (centrado)
        centro = tamaño // 2
        for i in range(tamaño):
            for j in range(tamaño):
                if i == centro or j == centro:
                    matriz[i][j] = '0'
    
    # Imprimir la matriz resultante
    for fila in matriz:
        print(' '.join(fila))

def mostrar_menu():
    """
    Mostrar el menú de opciones al usuario y manejar la entrada.
    """
    print("Selecciona una figura:")
    print("1. Diagonal principal (↘)")
    print("2. Diagonal secundaria (↙)")
    print("3. Ambas diagonales")
    print("4. Triángulo en cruz (centrado)")
    
    while True:
        try:
            opcion = int(input("Ingresa el número de la figura (1-4): "))
            if 1 <= opcion <= 4:
                break
            else:
                print("Por favor, selecciona un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entre 1 y 4.")
    
    tamaño = int(input("Ingresa el tamaño de la matriz (un número impar es recomendable): "))
    dibujar_figura(opcion, tamaño)

# Iniciar el programa mostrando el menú
mostrar_menu()
