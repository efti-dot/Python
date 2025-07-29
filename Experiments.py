N = int(input())
x = 0
C = 0
R = 0
S = 0
for i in range(N):
    a, b = input().split()
    a = int(a)
    if 1<= a <=15:
        x = x + a
        if b == 'C':
            C += a
        elif b == 'R':
            R += a
        elif b == 'S':
            S += a

print(f"Total: {x} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {C*100/x:.2f} %")
print(f"Percentual de ratos: {R*100/x:.2f} %")
print(f"Percentual de sapos: {S*100/x:.2f} %")