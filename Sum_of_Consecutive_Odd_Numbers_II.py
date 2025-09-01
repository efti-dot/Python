N = int(input())
sum = 0
for i in range(N):
    a = input().split(" ")
    X, Y = int(a[0]), int(a[1])
    for j in range(X, Y+1):
        if j%2 != 0:
            sum += j
    
print(sum)
