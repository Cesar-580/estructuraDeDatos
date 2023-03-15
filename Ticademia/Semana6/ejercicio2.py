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

