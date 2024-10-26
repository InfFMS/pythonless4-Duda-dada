# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
side1=int(input())
side2=int(input())
side3=int(input())
def is_valid_triangle(side1,side2,side3):
    side_min=min(side1,side2,side3)
    side_max=max(side1,side2,side3)
    if side1+side2+side3-side_max >side_max:
        return True
    else:
        return False
print(is_valid_triangle(side1, side2, side3))