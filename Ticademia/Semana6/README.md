# Módulo Semana 2

## Primer punto

![PrimerPuntoModulo2](/Semana6/imagenes/1.png)

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

![SegundoPuntoModulo2](/imagenes/2_1.png)
![SegundoPuntoModulo2](/imagenes/2_2.png)

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

![TercerPuntoModulo2](/imagenes/3_1.png)
![TercerPuntoModulo2](/imagenes/3_2.png)

```python

C = int(input())
cadString = list()

for i in range(C):
    cadString.append(input().split( ))

for j in range(len(cadString)):
    longString = len(cadString[j])
    
    actualString = cadString[j]

    if (longString % 2 == 0):
        # Parte cuando la cadena tiene carácteres impares
        k = 0
    else:
        # Parte cuando la cadena tiene carácteres pares
        k = 1
        
    while k <= longString - 1:
        actualString[k], actualString[k+1] = actualString[k+1], actualString[k]
        k +=2 
    w = 0
    while w <= int((longString-1)/2):
        actualString[w], actualString[longString-1-w] = actualString[longString-1-w], actualString[w]
        w += 1
    actualString = "".join(actualString)
    print(actualString)

```


# Cuarto punto

![CuartoPuntoModulo2](/imagenes/4_1.png)

```python

N = int(input())
listValues = input().split(", ")

newArray = []

lendlist = int((len(listValues))/2)

if (N-1) % 2 == 0:
    lendlist = lendlist + 1
else:
    lendlist = lendlist

for i in range(lendlist):
    if (N - i -1) == i:
        newArray.append(listValues[N - i -1])
    else:
        newArray.append(listValues[i])
        newArray.append(listValues[N - i -1])
    i += 2
 
newArray = "".join(newArray).replace(" ","")
print(newArray)
```

# Quinto punto
