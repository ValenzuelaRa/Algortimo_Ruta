columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
filas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

matriz = [
    [-3, -3, 2, -3, 3, -2, -2, 1, 2, 0, 2, 0, 1],
    [2, 3, 'I', -1, -1, 3, 2, 0, -3, -3, 2, 2, 1],
    [1, -3, -3, 2, 3, 1, 3, 3, 2, 1, -2, -2, 3],
    [0, 0, 3, 0, 3, -3, -2, -3, 0, 2, 2, 1, 1],
    [2, -1, -1, -3, 3, 3, 0, -3, 1, -2, 2, 0, 1],
    [0, 3, -1, 1, -1, -2, 2, -2, 2, -1, -2, -3, 0],
    [0, 3, 2, 0, 1, 1, 2, 3, -1, -3, 0, 0, -2],
    [3, 3, -3, -2, 3, -3, -1, -3, 3, -2, 2, -2, -1],
    [-2, -2, 1, 0, -1, 0, 3, 0, 0, -2, 2, -3, -1],
    [-3, 3, 0, -1, -3, 1, 2, -3, 2, -3, 0, 2, -2],
    [-3, -3, -3, 3, -2, 0, -2, -3, 1, 0, 1, -1, -2],
    [-1, 0, 1, 2, 1, 0, 'F', 0, -3, 3, 3, -2, -1],
    [1, -3, 1, 0, 1, 2, 3, 1, -2, 3, 3, 0, 3]
]


def matriz_13(matriz, columnas, filas):
   
    print("   ", end="")
    for col in columnas:
        print(f"  {col} ", end="")
    print()
    
    
    for i, fila in enumerate(matriz):
        print(f"{filas[i]:2} ", end="")  
        for valor in fila:
            print(f"{valor:3} ", end="") 
        print()


matriz_13(matriz, columnas, filas)


def preanalisis(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

I = preanalisis(matriz, 'I')
F = preanalisis(matriz, 'F')

print(f'Inicio (I): {I}, Fin (F): {F}')