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
        while k <= longString - 1:
            # print("BIEN",k)
            temp = actualString[k+1]
            actualString[k+1] = actualString[k]
            actualString[k] = temp
            k +=2 
        # print("1",actualString)
        # Aca ya actualString tiene a M*
        w = 0
        while w <= int((longString)/2):
            # print(longString)
            # print(w)
            tempH = actualString[longString -1 - w]
            actualString[longString- 1 - w] = actualString[w]
            actualString[w] = tempH
            # print("Ult",actualString[longString -1 - w])
            # print("First",actualString[w])
            w += 1
        # print("2",actualString)
        actualString = "".join(actualString)
        print(actualString)
    else:
        # Parte cuando la cadena tiene carácteres pares
        k = 1
        while k <= longString - 1:
            # print("BIEN",k)
            temp = actualString[k+1]
            actualString[k+1] = actualString[k]
            actualString[k] = temp
            k +=2 
        # print("1",actualString)
        # Aca ya actualString tiene a M*
        w = 0
        while w <= int((longString)/2):
            # print(longString)
            # print(w)
            tempH = actualString[longString -1 - w]
            actualString[longString- 1 - w] = actualString[w]
            actualString[w] = tempH
            # print("Ult",actualString[longString -1 - w])
            # print("First",actualString[w])
            w += 1
        # print("2",actualString)
        actualString = "".join(actualString)
        print(actualString)


    # o i n a m _ c e n e _ e n v i 6 _ _ 8 t e e n a g