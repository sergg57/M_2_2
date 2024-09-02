print('Введите последовательно три числа:')
first = input('Введите первое число:')
second = input('Введите второе число:')
third = input('Введите  третье число:')

print(first , second , third )

if first == second and first == third and second == third:
    print('3 - все три числа равны')
elif ((first == second and first != third and second != third) or
    (first != second and first == third and second != third) or
    (first != second and first != third and second == third)):
    print('2 - только два числа равны')
else:
    print('0 - все числа разные')


