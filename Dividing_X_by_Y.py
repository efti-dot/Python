N = int(input())
for i in range(N):
    Pair = input().split(" ")
    X, Y = int(Pair[0]), int(Pair[1])
    if Y==0:
        print("divisao impossivel")
    else:
        result = X/Y
        print(f"{result:.1f}")
