# Número de casos de prueba
C= int(input())

# lista respuesta
listaSalida : list = list()

# Tomar los valores de los casos
for casos in range(C):
    # Tamaño del tablero
    N = int(input())
    
    # Valores del tablero
    vTab = input().split( )
    vTab = list(map(int,vTab))

    siguienteCoordenada : int = 0

    # Lista para saber si este ya se recorrió
    listaRecorridos : list = list()
    # print("listaRecorridos ",listaRecorridos)

    while(siguienteCoordenada >= 0 and siguienteCoordenada < N ):
        if (siguienteCoordenada not in listaRecorridos):
            listaRecorridos.append(siguienteCoordenada)
            # print("listaRecorridos ",listaRecorridos)

            siguienteCoordenada += vTab[siguienteCoordenada]
            # print("La siguiente coordenada es: ",siguienteCoordenada)
        else:
            # print("Me sali")
            break
    
    listaSalida.append(len(listaRecorridos))

for salidas in listaSalida:
    print(salidas)
