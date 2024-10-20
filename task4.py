# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def nod(a, b):
    if a== 0 or b== 0:
        return max(a, b)
    return nod(max(a, b) % min(a, b), min(a, b))


b=int(input())
a=int(input())
print("НОД:", nod(a, b))
