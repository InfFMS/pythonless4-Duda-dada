# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
def number_to_words(num):
    if num==1:
        return 'один'
    if num==2:
        return 'два'
    if num==3:
        return 'три'
    if num==4:
        return 'четыре'
    if num==5:
        return 'пять'
    if num==6:
        return 'шесть'
    if num==7:
        return 'семь'
    if num==8:
        return 'восемь'
    if num==9:
        return 'девять'
    if num==10:
        return 'десять'
    if num==11:
        return 'одиннадцать'
    if num==12:
        return 'двенадцать'
    if num==13:
        return 'тринадцать'
    if num==14:
        return 'четырнадцать'
    if num==15:
        return 'пятнадцать'
    if num==16:
        return 'шестнадцать'
    if num==17:
        return 'семнадцать'
    if num==18:
        return 'восемнадцать'
    if num==19:
        return 'девятнадцать'
    if num==20:
        return 'двадцать'
    if num==30:
        return 'тридцать'
    if num==40:
        return 'сорок'
    if num==50:
        return 'пятьдесят'
    if num==60:
        return 'шестьдесят'
    if num==70:
        return 'семьдесят'
    if num==80:
        return 'восемьдесят'
    if num==90:
        return 'девяносто'

    return number_to_words(num // 10 * 10) + ' ' + number_to_words(num % 10)
print(number_to_words(65))
