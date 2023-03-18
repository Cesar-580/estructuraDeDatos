# Número de casos de prueba
C= int(input())

listaSalida : list = list()

# M # de integrantes  N: # Monedas
for casos in range(C):
    M , N = input().split(" ")
    M , N = int(M) , int(N)
    tupla = (M,N)
    
    # Lista donde irán las denominaciones de las monedas
    vMonedas = input().split(" ")

    # Lista para almacenar las ganacias de cada integrante
    vGanacias : list = list()
    
    # for que itera sobre los integrantes para tomar cada 
    # uno de los valores que le corresponde
    for integrantes in range(M):

        # Definicion de variables para iterar dentro del while 
        # Inicio : es el número que indica el integrante 
        # Indice : es el valor sobre el cual se itera (2 o 3) 
        # Suma : es la varaible que guardará el valor de cada 
        # uno de la recompensa por participante
        inicio : int = integrantes
        indice : int = 0
        suma : int = 0


        while (integrantes+indice) < N:
            suma = suma + int(vMonedas[integrantes+indice])
            indice += M
        vGanacias.append(suma)

    maxGanancias = max(vGanacias)
    minGanancias = min(vGanacias)
    listaSalida.append(maxGanancias - minGanancias)

for salidas in listaSalida:
    print(salidas)
