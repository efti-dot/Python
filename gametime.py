# -*- coding: utf-8 -*-
"""GameTime.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SlRyWvjw5KLA5S69r_5vBrhX6ozSlNMQ
"""

a = input().split(" ")
A, B = int(a[0]), int(a[1])

if A >= B:
    a = abs(A - 24)
    b = abs(a + B)
    print(f"O JOGO DUROU {b} HORA(S)")
else:
    print(f"O JOGO DUROU {abs(A - B)} HORA(S)")