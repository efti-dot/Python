I = 1
j = 7
while(1):
    for i in range(1, 4):
        print(f"I={I} J={j}")
        j -= 1
    I += 2
    j += 3
    if I > 9:
        break