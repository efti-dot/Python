N = int(input())
for i in range(1, N+1):
    A = int(input())
    if A>0 and A%2 == 0:
        print(f"{A} EVEN POSITIVE")
    elif A>0 and A%2 != 0:
        print(f"{A} ODD POSITIVE")
    elif A<0 and A%2 != 0:
        print(f"{A} ODD NEGATIVE")
    elif A<0 and A%2 == 0:
        print(f"{A} EVEN NEGATIVE")
    else:
        print(f"{A} NULL")