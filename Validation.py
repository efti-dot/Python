count = 0
l = []
while X==2:
    a = input()
    if a>0 or a<10:
        l.append(a)
        count += 1
    else:
        print("nota invalida")

print(f"media = {((int(l[0])+int(l[1]))/2)}")