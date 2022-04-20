#обо мне
name = 'Natalia'
print(type(name))
age = 27
print(type(age))
print('My name is ' + name)
print('I am ' + str(age) + ' years old')

#калькулятор
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
operation = input('Введите необходимую операцию (сложение, вычитание, умножение, деление): ')
if operation == 'сложение':
    print(a + b)
elif operation == 'вычитание':
    print(a - b)
elif operation == 'умножение':
    print(a * b)
elif operation == 'деление':
    print(a / b)
else:
    print('Неизвестная операция')

