import time
inicio = time.time()


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
        # print("BIEN",k)
        actualString[k], actualString[k+1] = actualString[k+1], actualString[k]
        k +=2 
    # print("1",actualString)
    # Aca ya actualString tiene a M*
    w = 0
    #print(int((longString-1)/2))
    for w, _ in enumerate(actualString[:longString//2]):
        actualString[w], actualString[longString-1-w] = actualString[longString-1-w], actualString[w]
    #print("2",actualString)
    actualString = "".join(actualString)
    print(actualString)
        
    # i a a f g r t o i p c r
    # o i n a m _ c e n e _ e n v i 6 _ _ 8 t e e n a g



    # 3
    # o n t h p y
    # v a j a
    # a a v _ j _ o o n t h p y 


fin = time.time()
print((fin-inicio)/1000)