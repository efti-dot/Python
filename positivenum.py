# -*- coding: utf-8 -*-
"""positiveNum.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SlRyWvjw5KLA5S69r_5vBrhX6ozSlNMQ
"""

count = 0
for i in range(6):
    nums = float(input())
    if(nums>0):
       count+=1
print(f'{count} valores positivos')