N = int(input())
sum = 0
for i in range(N):
    a = input().split(" ")
    X, Y = int(a[0]), int(a[1])
    for j in range(X+1, Y):
        print(j)
        if j%2 != 0:
            print(j)
            sum += j
    print(sum)
