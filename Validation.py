count = 0
l = []
while count<2:
    a = input()
    if a>0 or a<10:
        count += 1
        if count == 2:
            X = int(input())
        l.append(a)
    else:
        print("nota invalida")

print(f"media = {((int(l[0])+int(l[1]))/2)}")

