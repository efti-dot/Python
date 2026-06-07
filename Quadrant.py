while True:
    a = input().split(" ")
    x, y = int(a[0]), int(a[1])
    print(x,y)
    if x==0 or y ==0:
        break
    elif x>0 & y>0:
        print("primeiro")
    elif x>0 & y<0:
        print("quarto")
    elif x<0 & y<0:
        print("terceiro")
    else:
        print("segundo")