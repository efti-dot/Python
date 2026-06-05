while True:
    a = input().split(" ")
    A, B = int(a[0]) , int(a[1])

    if A == B:
        break
    else:
        if A<B:
            print("Crescente")
        else:
            print("Decrescente")