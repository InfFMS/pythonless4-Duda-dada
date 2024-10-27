# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def rec(n):
    if n==1:
        return ""
    for i in range(2,n//2+1):
        if n%i== 0:
            return str(i) + "*" +rec(n/ i)
    return str(n)
print(rec(int(input())))






