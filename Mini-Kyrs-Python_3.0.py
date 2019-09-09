# UNIT 1
# print('Hello, Python')
# a = 1 + 2 + 3 + \
# from django.views.decorators.http import condition
    # 4 + 5
# print(a)
# a = {1 + 2 + 3 + 
    # 4 + 5}
# print(a)

# my_aweosome_variable - Snacke case
# myAweosomeVariable - Camel case

# def myFunc():
    # IndentationError
    
# my_var = 2

# a, b, c = 1, 'some', True

# py = 2
# py = 3

# import sys d = 2 e = int(2) 
# print(sys.getsizeof(d)) 
# print(sys.getsizeof(e))

# d = [5, 10, 15, 20, 25, 30, 35, 40]
# type(d)
# isinstance(d, list)




# UNIT 2
# age = int(input("What's your age? - "))
# roles = ['user', 'admin']
# role = input("Яка твоя роль? - ")

# if age > 18 and role in roles:
#     if role == 'admin':
#         print("Привіт, {}, як ти почуваєшся {}?")
# else:
#     print("you")

# print("This site used cookies")

# age = int(input("Скільки тобі років? - "))

# if age < 7:
#     print("Ти дитина")
# elif age < 17:
#     print("Ти підліток")
# elif age >= 17:
#     print("Ти дорослий")

# genre = ['pop', 'rock', 'jazz']

# print(len(genre))

# for i in range(len(genre)):
#     print("I like", genre[i])

# while True:
#     num = int(input("Enter an integer: "))
#     print("The double of, num", "is", 2 * num)




# UNIT 3
# '''docstring''' - коментар до конкретної функції (фіункції, класи, файли, пакети)

# def greet(name):
#     """Тут інформація про дану функцію"""
#     print("Hello, " + name + ". Good morning!")
    
# # greet('Taras')
# # print(greet.__doc__) # інфа про функцію
# y = greet('Taras') # буде Hello, Taras. Good morning!
# print(y)

# def greet(first, second, *args, **kwargs):
#     print(first) # виведе перше значення
#     print(second) # виведе друге значення
#     print(args) # виведе всі значення
#     print(kwargs) # виведе ключові слова
    
# print(greet("Monica", "Luke", "Steve", "John", name = "Tom", surname = "Adams"))

# def calc_factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x-1))

# num = 26
# print("Факторіал числа ", num, "є", calc_factorial(num))

# def calc_factorial(x):
#     f = 1
#     for i in range(x):
#         f *= i + 1

# num = 6
# print(calc_factorial(num))

# lambda arguments: expression
# double = lambda x: x * 2 # для тимчасових результатів
# print(double(5))
# # те ж саме написано нижче
# def new_double(x):
#     return x * 2
# print(new_double(5))

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# def my_filter(x):
#     return x % 2 == 0
# new_list = list(filter(my_filter, my_list))
# print(new_list)
# те саме нижче
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(filter(lambda x:(x % 2 == 0), my_list))
# print(new_list)

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x:(x % 2 == 0), my_list))

# for list in range(15):
#     print('=^.^=')




# UNIT 4
# l = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(l)

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# l = [x, y, z]
# print(l[2][0])

# Slice
# l = ['c', 'r', 'o', 'c', 'o', 'd', 'i', 'l', 'e']
# l2 = l
# l[0] = 'C'
# print('l2:', l2)
# new_l = l[:]
# print('new_l id:', id(l))
# print('new_l id:', id(new_l))
# print(l[:])
# print(new_l)

# odd = [1, 2, 3]
'''extend ==  concatonation (+)'''

'''методи - змінють об'єкт
функції - повертають новий об'єкт'''

'''pop = del - видалення елементів'''

'''index - знаходить першим у списку потрібний елемент
count - показує кількість елементів'''

'''List Comprehension - покращення списку'''
# pow2 = [2 ** x for x in range(10)]
# print(pow2)

# pow2 = []
# for x in range(10):
#     pow.append(2 ** x)
    
'''переслухати 1:40 - 1:45 - про кортеж та id'''

'''discard - видалення елементів для set'''

'''frozenset - не змінювальний список'''

# squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(squares.items())
# print(list(squares.values()))
# print(list(squares.keys()))
# squares.setdefault(5, 25)
# squares.setdefault(6, 36)
# squares.setdefault(7)
# print(squares)
# for key, value in squares.items():
#     print(f'key: {key}\tvalue: {value}')




# UNIT 5
'''парадигми програмувань
OOP - об'єсено орієнтовне програмування
функціональне програмування'''

'''об'єкт - аналог словників'''

'''об'єкт може підтримувати:
1 . атрибути
2. поведінки'''

'''DRY OOP
1. наслідування - з іншого класу
2. інкапсуляція обмеження доступу
3. поліморфізм - назвати однаково об'єкти у різних класах'''

'''class - трафаретка (Class Parrot:)
object - те що зробили за допомогою трафаретки (obj = Parrot()) - екзесиляри класу
__class__ - об'єкт класу - для того щоб створювати інші об'єкти
methods - функції (def)
Inheritance - наслідування, створення нового класу, наслідуючи елементи з іншого класу не змінюючи ті класи
Encapsulation - Інкапсуляція, захищена змінна/поле, _ - (для програміста) або __ - (для програми, через клас) - перед назвою змінної c.__maxprice = 1000 -> c.set_max_price(1000)
Polymorphism - Поліморфізм, спільний інтерфейс для різних типів данних -> створення функції -> запуск методу -> Отримуємо різні результати'''

'''set та get - дозволяють змінювати інкапсульовані данні'''

'''MRO - унаслідування'''

# def repeat_str(repeat, string):
    # return(repeat * string)
# print(repeat_str(4, 'a'))
# print(repeat_str(3, 'hello '))
# print(repeat_str(2, 'abc'))

# def repeat_str(repeat, string):
    # return(repeat * string)
# repeat_str(4, 'a')
# repeat_str(3, 'hello ')
# repeat_str(2, 'abc')