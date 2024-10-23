# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.

side1 = int(input())
side2 = int(input())
side3 = int(input())
sum = side1 + side2
sum2 = side1 + side3
sum3 = side3 + side2
def is_valid_triangle(side1, side2, side3):
    if side3 < sum:
        print("True")
    elif side3 >= sum:
        print("False")
    elif side2< sum2:
        print ("True")
    elif side2 >= sum2:
        print("false")
    elif side3< sum3:
        print ("True")
    elif side3 >= sum3:
        print ("False")


is_valid_triangle(side1, side2, side3)