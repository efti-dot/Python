N = int(input())
s = 0
for i in range(N):
    a, b = input().split()
    a = int(a)
    if 1<= a <=15:
        s = s + a

print(s)