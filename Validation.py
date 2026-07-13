count = 0
l = []
while True:
    a = int(input())
    if 0 <= a <= 10:
        count += 1
        l.append(a)
        if count==2:
            print(f"media = {((int(l[0])+int(l[1]))/2)}")
            while True:
                print("novo calculo (1-sim 2-nao)")
                print("okay!")
                X = int(input())
                if X == 1:
                    count = 0
                    l = []
                    break
                elif X == 2:
                    exit()
    else:
        print("nota invalida")

