while True:
    a = input().split(" ")
    M, N = int(a[0]), int(a[1])
    if M == 0 or N == 0:
        break
    else:
        if M>N:
            M, N = N, M
        sum = 0
        for i in range (M, N+1):
            sum = sum + i
            print(i, end=" ")
        print(f"Sum={sum}")