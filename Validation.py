count = 0
l = []
while True:
    a = float(input())
    if 0 <= a <= 10:
        count += 1
        l.append(a)
        if count==2:
            print(f"media = {(l[0] + l[1]) / 2:.2f}")
            while True:
                print("novo calculo (1-sim 2-nao)")
                X = int(input())
                if X == 1:
                    count = 0
                    l = []
                    break
                elif X == 2:
                    exit()
    else:
        print("nota invalida")
        print("Thank you!")

