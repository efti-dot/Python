# -*- coding: utf-8 -*-
"""Banknotes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SlRyWvjw5KLA5S69r_5vBrhX6ozSlNMQ
"""

a = int(input())
print(a)

n100 = a // 100
a = a % 100
print(f"{n100} nota(s) de R$ 100,00")

n50 = a // 50
a = a % 50
print(f"{n50} nota(s) de R$ 50,00")

n20 = a // 20
a = a % 20
print(f"{n20} nota(s) de R$ 20,00")

n10 = a // 10
a = a % 10
print(f"{n10} nota(s) de R$ 10,00")

n5 = a // 5
a = a % 5
print(f"{n5} nota(s) de R$ 5,00")

n2 = a // 2
a = a % 2
print(f"{n2} nota(s) de R$ 2,00")

n1 = a // 1
print(f"{n1} nota(s) de R$ 1,00")