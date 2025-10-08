a = []

while(1):
    a = input().split(" ")
    M, N = int(a[0]), int(a[1])

    while(1):
        if M == 0 or N == 0:
            break
        else:
            if M>N:
                M, N = N, M
            sum = 0
            for i in range (M, N+1):
                print(i)
