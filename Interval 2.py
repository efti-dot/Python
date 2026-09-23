N = int(input())
In = 0
Out = 0
for i in range(1, N+1):
    A = int(input())
    if A >= 10 and A <= 20:
        In += 1
    else:
        Out += 1

print(f"{In} in")
print(f"{Out} out")

