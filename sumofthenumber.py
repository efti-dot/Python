# -*- coding: utf-8 -*-
"""sumOfTheNumber.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SlRyWvjw5KLA5S69r_5vBrhX6ozSlNMQ
"""

num = int(input("Input a number: "))
x = num // 1000
x1 = (num - x * 1000) // 100

x2 = (num - x * 1000 - x1 * 100) // 10
x3 = num - x * 1000 - x1 * 100 - x2 * 10

print("The sum of digits : ", x + x1 + x2 + x3)