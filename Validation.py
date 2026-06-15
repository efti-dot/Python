count = 0
l = []
while True:
    a = input()
    if a>0 or a<10:
        count += 1
        l.append(a)
        if count==2:
            print("novo calculo (1-sim 2-nao)")
            X = int(input())
            if X == 1:
                continue
            else:
                break
    else:
        print("nota invalida")

print(f"media = {((int(l[0])+int(l[1]))/2)}")

