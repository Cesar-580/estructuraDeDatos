N = int(input())
L = input().split( )

sum = int(L[-1])

for i in range(1,N):
    c = N - i - 1
    sum += int(L[c])
    print(sum)  

