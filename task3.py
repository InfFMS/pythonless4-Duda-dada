# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

n = int(input())
count_M = 0
count_D = 0
count_C = 0
count_L = 0
count_X = 0
count_V = 0
if n//1000!=0:
    count_M = n//1000
    n-=count_M*1000
if n//500!=0:
    count_D = n//500
    n-=count_D*500
if n//100!=0:
    count_C = n//100
    n-=count_C*100
if n//50!=0:
    count_L = n//50
    n-=count_L*50
if n//10!=0:
    count_X = n//10
    n-=count_X*10
if n // 5 != 0:
        count_V = n // 5
        n -= count_V * 5
print(count_M *"M"+count_D*"D"+count_C*"C"+count_L*"l"+count_X*"X"+count_V*"V"+n*'I')
