# Módulo Semana 2

## Primer punto

![PrimerPuntoModulo2](../Ticademia/imagenes/1.png)

```python
N = int(input()) # Lee el número de elementos que se ingresarán
L = input().split( ) # Lee una lista de números separados por espacio y los guarda en una lista de cadenas de texto

sum = int(L[-1]) # Inicializa la variable sum con el último elemento de la lista L convertido a un entero

for i in range(1,N): # Recorre la lista L en orden inverso, desde el penúltimo elemento hasta el primero
    c = N - i - 1 # Calcula el índice del elemento actual en la lista L
    sum += int(L[c]) # Suma el elemento actual a la variable sum
    print(sum) # Muestra la suma acumulada hasta el momento en cada iteración del bucle
```

## Segundo punto

![SegundoPuntoModulo2](../Ticademia/imagenes/2_1.png)
![SegundoPuntoModulo2](../Ticademia/imagenes/2_2.png)

```python
N = int(input())


listSo = input().split(",")
listLar = input().split(",")
listIs = input().split(",")

countSo = 0
countLar = 0
countIs = 0

for i in range(N):
    sum = int(listSo[i]) + int(listLar[i]) + int(listIs[i])

    if sum % 2 == 0: 
        if int(listSo[i]) % 2 == 0:
            countSo += 1
        if int(listLar[i]) % 2 == 0:
            countLar += 1
        if int(listIs[i]) % 2 == 0:
            countIs += 1
    else:
        if int(listSo[i]) % 2 != 0:
            countSo += 1
        if int(listLar[i]) % 2 != 0:
            countLar += 1
        if int(listIs[i]) % 2 != 0:
            countIs += 1

print("SO:{}, LAR:{}, IS:{}".format(countSo,countLar,countIs))
```

## Tercer punto

![TercerPuntoModulo2](../Ticademia/imagenes/2_1.png)
![TercerPuntoModulo2](../Ticademia/imagenes/2_2.png)