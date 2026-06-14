vaild_count = 0
score = []
while vaild_count<2:
    i = float(input())
    if i<0 or i>10:
        print("nota invalida")
    else:
        vaild_count += 1
        score.append(i)

avg = (score[0]+score[1])/2
print(f"media = {avg:.2f}")