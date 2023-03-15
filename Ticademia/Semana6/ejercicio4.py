N = int(input())
listValues = input().split(", ")

newArray = []


# print(listValues)


lendlist = int((len(listValues))/2)
# print("Len V: ",len(listValues))
# print("Len: ",lendlist)

if (N-1) % 2 == 0:
    lendlist = lendlist + 1
else:
    lendlist = lendlist

for i in range(lendlist):
    # print("Posición i: ", i)
    # print("Posición N - i -1: ", (N - i -1), " listValues[N - i -1] ", listValues[N - i -1])
    # print("F: ", listValues[i], " Con: ", listValues[N - i -1])
    if (N - i -1) == i:
        newArray.append(listValues[N - i -1])
    else:
        newArray.append(listValues[i])
        newArray.append(listValues[N - i -1])
    
    # print("Valores agregados", newArray)
    i += 2
 
newArray = "".join(newArray).replace(" ","")
print(newArray)


# S, R, M, G, O, A, A, A
# C, R, A
# E1, E2, E3, E4, E5
# E, E, E, E, E
# N, O 