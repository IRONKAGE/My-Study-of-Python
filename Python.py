                            # №1 - Знайомство з Phyton


# https://www.python.org/downloads/

# print("Привіт, світе")


                            # №2 - Розрахунки та змінні


# print(8 * 3.57)
# print(10 * 365)
# print(20 + 3650)
# print(3 * 52)
# print(3670 - 156)

# print(5 + 30 * 20)
# print((5 + 30) * 20)
# print(((5 + 30) * 20) / 10)
# print(5 + 30 * 20 / 10)

# fred = 100
# print(fred)
# fred = 200
# print(fred)
# fred = 200
# john = fred
# print(john)
# кількість_монет = 200
# print(кількість_монет)

# print(20 + 10 * 365)
# print(3 * 52)
# print(3670 - 156)
# print(20 + 10 * 365 - 3 * 52)
# знайдені_монети = 20
# чарівні_монети = 10
# вкрадені_монети = 3
# print(знайдені_монети + чарівні_монети * 365 - вкрадені_монети * 52)
# вкрадені_монети = 2
# print(знайдені_монети + чарівні_монети * 365 - вкрадені_монети * 52)
# чарівні_монети = 13
# print(знайдені_монети + чарівні_монети * 365 - вкрадені_монети * 52)


                            # №3 - Стрічки, списки, кортежі та словники


# fred = "Чому у горили великі ніздрі? Бо в них великі пальці!"
# fred = 'Що рожеве й пухнасте? Рожевий пух!!'
# fred = '''Як динозаври сплачують рахунки?
# Тиранощзаврячими чеками!'''
# print(fred)

# просто_стрічка = '''Він сказав: "Там в'ється бур'ян дерев'яним п'ядесталом."'''
# print(просто_стрічка)
# стрічка_з_одинарними_лапками = 'Він сказав: "Там в\'ється бур\'ян дерев\'яним п\'ядесталом."'
# print(стрічка_з_одинарними_лапками)
# стрічка_з_подвійними_лапками = "Він сказав: \"Там в'ється бур'ян дерев'яним п'ядесталом.\""
# print(стрічка_з_подвійними_лапками)

# мій_рахунок = 1000
# повідомлення = 'Мені вдалося здобути %s очок'
# print(повідомлення % мій_рахунок)

# жарт = '%s: пристрій для знаходження меблів у темряві'
# частина_тіла_1 = 'коліно'
# частина_тіла_2 = 'гомілка'
# print(жарт % частина_тіла_1)
# print(жарт % частина_тіла_2)

# числа = 'Що число %s сказало числу %s? Гарний пояс!!!'
# print(числа % (0,8))

# print(10 * 'а')

# пробіли = ' ' * 25
# print('%s Задуплянський провулок, 12' % пробіли)
# print('%s Далека глушина' % пробіли)
# print('%s село Західні Хропаки' % пробіли)
# print()
# print()
# print('Шановний пане,')
# print()
# print('Хочу Вам повідомити, що з даху туалету надворі')
# print('злетіла черепиця.')
# print('Напевно, в усьому винен вчорашній сильний вітер.')
# print()
# print('З повагою,')
# print('Мальколм Дітерінг')

# print(1000 * 'брудний сніг ')

# список_чарівника = "павукові лапки, жаб\'ячий палець, око тритона, крило кажана, масло зі слизняка, луска змії"
# print(список_чарівника)
# список_чарівника = ['павукові лапки', 'жаб\'ячий палець', 'око тритона', 'крило кажана', 'масло зі слизняка', 'луска змії']
# print(список_чарівника)
# print(список_чарівника [2])
# список_чарівника = ['павукові лапки', 'жаб\'ячий палець', 'око тритона', 'крило кажана', 'масло зі слизняка', 'луска змії']
# список_чарівника[2] = 'язик равлика'
# print(список_чарівника)
# print(список_чарівника[2:5])

# деякі_числа = [1, 2, 5, 10, 20]
# деякі_рядки = ['Масло', 'масляне']
# числа_та_рядки = ['Скільки', 'буде', 6, 'на', 8, '?']
# print(числа_та_рядки)

# числа = [1, 2, 3, 4]
# стрічки = ['Я', 'забив', 'палець', 'і', 'він', 'тепер', 'болить']
# мій_список = [числа, стрічки]
# print(мій_список)

# список_чарівника = ['павукові лапки', 'жаб\'ячий палець', 'око тритона', 'крило кажана', 'масло зі слизняка', 'луска змії']
# список_чарівника[2] = 'язик равлика'
# список_чарівника.append('ведмежа відрижка')
# список_чарівника.append('мандрагора')
# список_чарівника.append('болиголов')
# список_чарівника.append('болотний газ')
# print(список_чарівника)
# del список_чарівника [5]
# print(список_чарівника)
# del список_чарівника [8]
# del список_чарівника [7]
# del список_чарівника [6]
# print(список_чарівника)

# список1 = [1, 2, 3, 4]
# список2 = ['Я', 'перечепився', 'упав', 'і', 'забився']
# print(список1+список2)

# список1 = [1, 2, 3, 4]
# список2 = ['Я', 'з\'їв', 'шоколадку', 'і', 'настрій', 'в', 'порядку']
# список3 = список1 + список2
# print(список3)

# список1 = [1, 2]
# print(список1 * 20)

# фібоначчі = (0, 1, 1, 2, 3)
# print(фібоначчі[3])
# фібоначчі[0] = 4

# улюблений_спорт = [ 'Ральф Вільямс, футбол',
                    # 'Майкл Тіппетт, баскетбол',
                    # 'Едвард Ельгар, бейсбол',
                    # 'Ребекка Кларк, нетбол',
                    # 'Етель Сміт, бадмінтон',
                    # 'Френк Брідж, реґбі']
# print(улюблений_спорт)

# улюблений_спорт = { 'Ральф Вільямс' : 'футбол',
                    # 'Майкл Тіппетт' : 'баскетбол',
                    # 'Едвард Ельгар' : 'бейсбол',
                    # 'Ребекка Кларк' : 'нетбол',
                    # 'Етель Сміт' : 'бадмінтон',
                    # 'Френк Брідж' : 'реґбі'}
# print(улюблений_спорт['Ребекка Кларк'])
# del улюблений_спорт['Етель Сміт']
# print(улюблений_спорт)
# улюблений_спорт['Ральф Вільямс'] = 'хокей на льоду'
# print(улюблений_спорт)

# улюблений_спорт = { 'Ребекка Кларк' : 'нетбол',
                    # 'Майкл Тіппетт' : 'баскетбол',
                    # 'Ральф Вільямс' : 'хокей на льоду',
                    # 'Едвард Ельгар' : 'бейсбол',
                    # 'Френк Брідж' : 'реґбі'}
# улюблені_кольори = {'Малколм Вернер' : 'рожевий горошок',
                    # 'Джеймс Бекстер' : 'помаранчеві смужки',
                    # 'Сью Лі' : 'фіолетові візерунки',}
# улюблений_спорт + улюблені_кольори


    # Д/З №1 - Улюблене
# улюбленні_хоббі = [  'програмування',
                    # 'малювання',
                    # 'читання',
                    # 'паяння',
                    # 'ігри']
# ігри = улюбленні_хоббі
# улюблена_їжа = [    'картопля',
                    # 'м\'ясо',
                    # 'морозиво']
# їжа = улюблена_їжа
# улюблене = ігри + їжа
# print(улюблене)


    # Д/З №2 - Підрахунок воїнів
# дахів = 3
# ніндзь_на_даху = 25
# тунелей = 2
# самураїв_у_тунелі = 40
# битва = дахів * ніндзь_на_даху + тунелей * самураїв_у_тунелі
# print(битва)


    # Д/З №3 - Вітання
# Вітання = 'Привіт, %s %s!'
# Імя = 'Олег'
# Прізвище = 'Гаценко'
# print(Вітання % (Прізвище, Імя))
# З книги
# ймення = 'Брандо'
# прізвище = 'Ікетт'
# print('Привіт, %s %s!' % (ймення, прізвище))


                            # №4 - Малюємо "Черепахою"


# import turtle
# t = turtle.Pen()
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )
# t.left( 90 )
# t.reset()
# t.clear()

# import turtle
# t = turtle.Pen()
# t.reset()
# t.backward( 100 )
# t.up()
# t.right( 90 )
# t.forward( 20 )
# t.left( 90 )
# t.down()
# t.forward( 100 )


    # Д/З №1 - Прямокутник
# import turtle
# t = turtle.Pen()
# t.forward( 250 )
# t.left( 90 )
# t.forward( 150 )
# t.left( 90 )
# t.forward( 500 )
# t.left( 90 )
# t.forward( 150 )
# t.left( 90 )
# t.forward( 250 )
# t.up()
# t.left( 90 )
# t.forward( 75 )


    # Д/З №2 - Трикутник
# import turtle
# t = turtle.Pen()
# t.forward( 90 )
# t.left( 120 )
# t.forward( 90 )
# t.left( 120 )
# t.forward( 90 )
# t.left( 120 ) 


    # Д/З №3 - Коробка без кутів
# import turtle
# t = turtle.Pen()
# t.forward( 100 )
# t.up()
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )
# t.down()
# t.forward( 100 )
# t.up()
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )
# t.down()
# t.forward( 100 )
# t.up()
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )
# t.down()
# t.forward( 100 )
# t.up()
# t.forward( 50 )
# t.left( 90 )
# t.forward( 50 )


                            # №5 - Якщо? та Тоді?


# вік = 26
# if вік > 20:
    # print('Оце стариган!')
    # print('Що ти тут робиш?')
    # print('Чому б тобі не зробити щось корисне?')

# вік = 26
# if вік >= 26:
    # print('Ти надто старий для моїх жартів!')

# вік = 10
# if вік == 10:
    # print('Що брунатне й шоколадне? Шоколад!')

# print("Хочеш почути брудний жарт?")
# вік = 26
# if вік == 12:
    # print("Порося впало в багнюку!")
# else:
    # print("Тсс. Це секрет.")

# вік = 11
# if вік == 10:
    # print("Як називається занадто засмагла малина?")
    # print("Ожина!")
# elif вік == 11:
    # print("Що зелена виноградина сказала синій?")
    # print("Дихай! Дихай!")
# elif вік == 12:
    # print("Що 0 сказав до 8?")
    # print("Привіт, хлопці!")
# elif вік == 13:
    # print("У якому стані може перебувати вода?")
    # print("У твердому, рідкому і газованому.")
# else:
    # print("Що?")

# вік = 11
# if вік == 10 or вік == 11 or вік == 12 or вік == 13:
    # print("Скільки буде 13 + 49 + 84 + 155 + 97? Багато!")
# else:
    # print("Що?")

# вік = 12
# if вік >= 10 and вік <= 13:
    # print("Скільки буде 13 + 49 + 84 + 155 + 97? Багато!")
# else:
    # print("Що?")

# моя_змінна = None
# print(моя_змінна)

# моя_змінна = None
# if моя_змінна == None:
    # print("Змінна моя_змінна не має значення")

# вік = 10
# if вік == 10:
    # print("Як найкраще розмовляти з монстром?")
    # print("Здалеку!")
    
# вік = '10'
# конвертований_вік = int(вік)
# if конвертований_вік == 10:
    # print("Як найкраще розмовляти з монстром?")
    # print("Здалеку!")

# вік = '10.5'
# конвертований_вік = float(вік)
# if конвертований_вік == 10.5:
    # print("Як найкраще розмовляти з монстром?")
    # print("Здалеку!")


    # Д/З №1 - Ти багатий?
# гроші = 2000
# if гроші > 1000:
    # print("Я багатий!!!")
# else:
    # print("Я не багатий!!")
    # print("Але колись може й буду...")


    # Д/З №2 - Печивко!
# печивка = 300
# if печивка < 100:
    # print("Замало печивка")
# elif печивка > 500:
    # print("Забагато печивка")
# else:
    # print("Достатньо печивка")


    # Д/З №3 - Правильне число?
# гроші = 500
# if (гроші >= 100 and гроші <= 500) or (гроші >= 1000 and гроші <= 5000):
    # print("Подумай куди мудро вкласти накоплені гроші ;)")
# else:
    # print("Збирай ще гроші...")

    # З книги
# гроші = 555
# if (100 <= гроші <= 500) or (1000 <= гроші <= 5000):
    # print("Подумай куди мудро вкласти накоплені гроші ;)")
# else:
    # print("Збирай ще гроші...")


    # Д/З №4 - Я можу подолати цих ніндзь!
# ніндзя = 9
# if ніндзя >= 50:
    # print("Це забагато!")
# elif ніндзя < 50 and ніндзя >= 30:
    # print("Буде важко, але Я впораюсь!")
# elif ніндзя < 30 and ніндзя >= 10:
    # print("Я можу подолати цих ніндзь!")
# else:
    # print("Дрібнички :)")

    # З книги
# ніндзя = 10
# if ніндзя < 10:
    # print("Я можу подолати цих ніндзь!")
# elif ніндзя < 30:
    # print("Буде важко, але Я впораюсь!")
# elif ніндзя < 50:
    # print("Це забагато!")


                            # №6 - Цикли та їх застосування


# print("здоров")
# for x in range(0, 5):
    # print("здоров")
# print(list(range(10, 20)))

# for x in range(0, 5):
    # print("здоров %s" % x)

# x = 0
# print("здоров %s" % x)
# x = 1
# print("здоров %s" % x)
# x = 2
# print("здоров %s" % x)
# x = 3
# print("здоров %s" % x)
# x = 4
# print("здоров %s" % x)

# список_чарівника = ["павукові лапки", "жаб\'ячий палець", "язик змії", "крило кажана", "масло зі слизняка", "ведмежа відрижка"]
# for i in список_чарівника:
    # print(i)

# список_чарівника = ["павукові лапки", "жаб\'ячий палець", "язик змії", "крило кажана", "масло зі слизняка", "ведмежа відрижка"]
# print(список_чарівника[0])
# print(список_чарівника[1])
# print(список_чарівника[2])
# print(список_чарівника[3])
# print(список_чарівника[4])
# print(список_чарівника[5])

# великі_волохаті_штани = ["великі", "волохаті", "штани"]
# for i in великі_волохаті_штани:
    # print(i)
    # print(i)

# великі_волохаті_штани = ["великі", "волохаті", "штани"]
# for i in великі_волохаті_штани:
    # print(i) #перший блок
    # for j in великі_волохаті_штани:
        # print(j) #другий блок

# знайдені_монети = 20
# чарівні_монети = 70
# вкрадені_монети = 3
# монети = знайдені_монети
# for тиждень in range(1, 53):
    # монети = монети + чарівні_монети - вкрадені_монети
    # print("Тиждень %s = %s" % (тиждень, монети))

# for сходинка in range(0, 20):
    # print(сходинка)

# сходинка = 0
# while сходинка < 10000:
    # print(сходинка)
    # if втомився == True:
        # break
    # elif погана_погода == True:
        # break
    # else:
        # сходинка = сходинка + 1

# x = 45
# y = 80
# while x < 50 and y < 100:
    # x = x + 1
    # y = y + 1
    # print(x, y)

# while True:
    # тут багато коду
    # тут багато коду
    # тут багато коду
    # if якесь_значення == True:
        # break


    # Д/З №1 - Цикл 'Привіт'
# for x in range(0, 20):
    # print("привіт %s" % x)
    # if x < 9:
        # break


    # Д/З №2 - Парні числа
# for вік in range(2, 26 + 1, 2):
    # print("Парне число %s" % вік)


    # Д/З №3 - Мої п'ять улюблених інгредієнтів
# інгрідієнти = ["ковбаса","сир","цибуля","помідор","соус"]
# x = 1
# for i in інгрідієнти:
    # print ("%s %s" %(x, i))
    # x = x + 1


    # Д/З №4 - Твоя вага на місяці
# вага = 75
# вік = 26
# for вік in range(26, 26 + 16):
    # print ("Вік %s Вага на місяці %s" %(вік, вага * 0.165))
    # вага += 1


                            # №7 - Повторне використання коду за допомогою функцій та модулів


# list(range(0, 5))
# list(range(0, 1000))

# def скажи_привіт(як_мене_звати):
    # print("Привіт, %s" % як_мене_звати)
# скажи_привіт("Мері")

# def скажи_привіт(ймення, прізвище):
    # print("Привіт, %s %s" % (ймення, прізвище))
# скажи_привіт("Мері", "Сміт")

# моє_ймення = "Олег"
# моє_прізвище = "Гаценко"
# def скажи_привіт(моє_ймення, моє_прізвище):
    # print("Привіт, %s %s" % (моє_ймення, моє_прізвище))
# скажи_привіт(моє_ймення, моє_прізвище)

# def заощадження(кишенькові, заробітки, витрати):
    # return кишенькові + заробітки - витрати
# print(заощадження(10, 10, 5))

# def тест_змінних():
    # перша_змінна = 10
    # друга_змінна = 20
    # return перша_змінна * друга_змінна
# print(тест_змінних())

# ще_одна_змінна = 100
# def тест_змінних_2():
    # перша_змінна = 10
    # друга_змінна = 20
    # return перша_змінна * друга_змінна * ще_одна_змінна
# print(тест_змінних_2())

# def будівництво_корабля(бляшанки):
    # всього_бляшанок = 0
    # for тиждень in range(1, 53):
        # всього_бляшанок = всього_бляшанок + бляшанки
        # print("Тиждень %s = %s бляшанок" % (тиждень, всього_бляшанок))
# будівництво_корабля(2)

# import time
# print(time.asctime())

# import sys
# print(sys.stdin.readline())

# def дурний_жарт_про_вік(вік):
    # if вік >= 10 and вік <= 13:
        # print("Скільки буде 13 + 49 + 84 + 155 + 97? Багато!")
    # else:
        # print("Що?")
# дурний_жарт_про_вік(12)

# import sys
# def дурний_жарт_про_вік():
    # print("Скільки тобі років?")
    # вік = int(sys.stdin.readline())
    # if вік >= 10 and вік <= 13:
        # print("Скільки буде 13 + 49 + 84 + 155 + 97? Багато!")
    # else:
        # print("Що?")
# дурний_жарт_про_вік()


    # Д/З №1 - Вага на місяці
# def вага_на_місяці(вага):
    # вік = 26
    # for вік in range(26, 26 + 16):
        # print ("Вік %s Вага на місяці %s" %(вік, вага * 0.165))
        # вага += 1
# вага_на_місяці(90)

# def вага_на_місяці(вага, приріст):
    # for рік in range(1, 16):
        # вага = вага + приріст
        # вага_на_місяці = вага * 0.165
        # print("Рік %s твоя вага %s" % (рік, вага_на_місяці))
# вага_на_місяці(75, 1)


    # Д/З №2 - Вага на місяці й роки
# def вага_на_місяці(вага, приріст, роки):
    # роки += 1
    # for рік in range(1, роки):
        # вага = вага + приріст
        # вага_на_місяці = вага * 0.165
        # print("Рік %s твоя вага %s" % (рік, вага_на_місяці))
# вага_на_місяці(75, 1, 25)


    # Д/З №3 - Програма вирахування ваги на місяці
# import sys
# def вага_на_місяці():
    # print("Введіть свою вагу, приріст у вазі та кількість проведених років на місяці")
    # вага = int(sys.stdin.readline())
    # приріст = int(sys.stdin.readline())
    # роки = int(sys.stdin.readline())
    # роки += 1
    # for рік in range(1, роки):
        # вага = вага + приріст
        # вага_на_місяці = вага * 0.165
        # print("Рік %s твоя вага %s" % (рік, вага_на_місяці))
# вага_на_місяці()


                            # №8 - Як кориистуватись класами й об'єктами???


# class Предмети:
    # pass
# class Неживі(Предмети):
    # pass
# class Живі(Предмети):
    # pass
# class Тротуари(Неживі):
    # pass
# class Тварини(Живі):
    # pass
# class Ссавці(Тварини):
    # pass
# class Жирафи(Ссавці):
    # pass
# Реджинальд = Жирафи()

# def це_нормальна_функція():
    # print("Я нормальна функція")
# це_нормальна_функція()

# class ЦеМійДурнийКлас:
    # def це_функція_класу():
        # print('Я функція класу')
    # це_функція_класу()
    # def це_теж_функція_класу():
        # print('Я теж функція класу. Бачиш?')
    # це_теж_функція_класу()

# class Предмети:
    # pass
# class Неживі(Предмети):
    # pass
# class Живі(Предмети):
    # pass
# class Тварини(Живі):
    # def дихати(self):
        # pass
    # def рухатися(self):
        # pass
    # def харчуватися_їжею(self):
        # pass

# class Ссавці(Тварини):
    # def годувати_дитинчат_молоком(self):
        # pass
# class Жирафи(Ссавці):
    # def їсти_листя_з_дерев(self):
        # pass
# Реджинальд = Жирафи()
# Реджинальд.рухатися()
# Реджинальд.їсти_листя_з_дерев()
# Гарольд = Жирафи()
# Гарольд.рухатися()

# class Тварини(Живі):
    # def дихати(self):
        # print("Дихає")
    # def рухатися(self):
        # print("Рухається")
    # def харчуватися_їжею(self):
        # print("Харчується їжею")

# class Ссавці(Тварини):
    # def годувати_дитинчат_молоком(self):
        # print("Годує дитинчат")

# class Жирафи(Ссавці):
    # def їсти_листя_з_дерев(self):
        # print("Їсть листя")
# Реджинальд = Жирафи()
# Гарольд = Жирафи()
# Реджинальд.рухатися()
# Гарольд.їсти_листя_з_дерев()

# import turtle
# Avery = turtle.Pen()
# Kate = turtle.Pen()
# Avery.forward(50)
# Avery.right(90)
# Avery.forward(20)

# Kate.left(90)
# Kate.forward(100)

# Jacob = turtle.Pen()
# Jacob.left(180)
# Jacob.forward(80)

# Ben = turtle.Pen()
# Ben.right(90)
# Ben.forward(125)

# class Предмети:
    # pass
# class Неживі(Предмети):
    # pass
# class Живі(Предмети):
    # pass
# class Тварини(Живі):
    # def дихати(self):
        # print("Дихає")
    # def рухатися(self):
        # print("Рухається")
    # def харчуватися_їжею(self):
        # print("Харчується їжею")
# class Ссавці(Тварини):
    # def годувати_дитинчат_молоком(self):
        # print("Годує дитинчат")
# class Жирафи(Ссавці):
    # def їсти_листя_з_дерев(self):
        # print("Їсть листя")
# Реджинальд = Жирафи()
# Реджинальд.дихати()
# Реджинальд.харчуватися_їжею()
# Реджинальд.годувати_дитинчат_молоком()
# Реджинальд.рухатися()

# class Жирафи(Ссавці):
    # def шукати_їжу(self):
        # self.рухатися()
        # print("Я знайшов їжу")
        # self.харчуватися_їжею()
    # def їсти_листя_з_дерев(self):
        # self.харчуватися_їжею()
    # def танцювати(self):
        # self.рухатися()
        # self.рухатися()
        # self.рухатися()
        # self.рухатися()
# Реджинальд = Жирафи()
# Реджинальд.танцювати()

# class Жирафи:
    # def __init__(self, плями):
        # self.жирафові_плями = плями
# Освальд = Жирафи(100)
# Гертруда = Жирафи(150)
# print(Освальд.жирафові_плями)
# print(Гертруда.жирафові_плями)


    # Д/З №1 - Танець жирафи
# class Предмети:
    # pass
# class Неживі(Предмети):
    # pass
# class Живі(Предмети):
    # pass
# class Тварини(Живі):
    # def дихати(self):
        # print("Дихає")
    # def рухатися(self):
        # print("Рухається")
    # def харчуватися_їжею(self):
        # print("Харчується їжею")
# class Ссавці(Тварини):
    # def годувати_дитинчат_молоком(self):
        # print("Годує дитинчат")
# class Жирафи(Ссавці):
    # def їсти_листя_з_дерев(self):
        # print("Їсть листя")
    # def шукати_їжу(self):
        # self.рухатися()
        # print("Я знайшов їжу")
        # self.харчуватися_їжею()
    # def ліву_ногу_вперед(self):
        # print("Ліва нога уперед")
    # def ліву_ногу_назад(self):
        # print("Ліва нога назад")
    # def праву_ногу_вперед(self):
        # print("Права нога уперед")
    # def праву_ногу_назад(self):
        # print("Права нога назад")
    # def танцювати(self):
        # self.ліву_ногу_вперед()
        # self.ліву_ногу_назад()
        # self.праву_ногу_вперед()
        # self.праву_ногу_назад()
        # self.ліву_ногу_назад()
        # self.праву_ногу_назад()
        # self.праву_ногу_вперед()
        # self.ліву_ногу_вперед()
# Реджинальд = Жирафи()
# Реджинальд.танцювати()


    # Д/З №2 - Черепаша виделка
# import turtle
# Avery = turtle.Pen()
# Kate = turtle.Pen()
# Jacob = turtle.Pen()
# Ben = turtle.Pen()

# Avery.forward(150)
# Avery.left(90)
# Avery.forward(100)
# Avery.right(90)
# Avery.forward(100)

# Kate.forward(170)
# Kate.left(90)
# Kate.forward(50)
# Kate.right(90)
# Kate.forward(50)

# Jacob.forward(170)
# Jacob.right(90)
# Jacob.forward(50)
# Jacob.left(90)
# Jacob.forward(50)

# Ben.forward(150)
# Ben.right(90)
# Ben.forward(100)
# Ben.left(90)
# Ben.forward(100)


                            # №9 - Вбудовані функції мови Python


# print(abs(10))
# print(abs(-10))

# кроки = -3
# if abs(кроки) > 0:
    # print('Персонаж рухається')

# кроки = -3
# if кроки < 0 or кроки > 0:
    # print('Персонаж рухається')

# print(bool(0))
# print(bool(1))
# print(bool(1123.23))
# print(bool(-500))

# print(bool(None))
# print(bool(''))
# print(bool('a'))
# print(bool('  '))
# print(bool('Що найважче карате-свинці? Мати біле кімоно!'))

# мій_дурний_список = []
# print(bool(мій_дурний_список))
# мій_дурний_список = ['д', 'у', 'р', 'н', 'и', 'й']
# print(bool(мій_дурний_список))

# рік = input('Рік народження: ')
# if not bool(рік.rstrip()):
    # print('Ти маєш ввести рік свого народження')

# dir(['список'])
# dir(1)
# попкорн = 'Я люблю попкорн!'
# dir(попкорн)
# help(попкорн.upper)

# eval('10*5')
# eval('''if True:
    # print('це точно не вийде')''')
# твоє_обчислення = input('Введи обчислення: ')
# eval(твоє_обчислення)

# моя_маленька_програма = '''print('шинка') 
# print('бутерброд')'''
# exec(моя_маленька_програма)

# float('12')
# float('123.456789')
# твій_вік = input('Введи свій вік: ')
# вік = float(твій_вік)
# if вік > 13:
    # print('Ти на %s років застарий' % (вік - 13))

# int(123.456)
# int('123')
# int('123.456')

# len('це пробна стрічка')
# список_істот = ['єдиноріг', 'циклоп', 'фея', 'ельф', 'дракон', 'троль']
# print(len(список_істот))
# словник_ворогів = {'Бетмен' : 'Джокер', 'Супермен' : 'Лекс Лютор', 'Спайдермен' : 'Зелений Гоблін'}
# print(len(словник_ворогів))
# фрукт = ['яблуко', 'банан', 'апельсин', 'манго']
# for x in range(len(фрукт)):
    # print("фрукт під номером", x, "це", фрукт[x])
# фрукт = ['яблуко', 'банан', 'апельсин', 'манго']
# кількість = len(фрукт)
# for x in range(0, кількість):
    # print("фрукт під номером %s це %s" % (x, фрукт[x]))

# числа = [5, 4, 10, 30, 22]
# print(max(числа))
# стрічка = "s, t, r, i, n, g, S, T, R, I, N, G"
# print(max(стрічка))
# print(max(10, 300, 450, 50, 90))
# числа = [5, 4, 10, 30, 22]
# print(min(числа))
# вгадай_це_число = 61
# здогади_гравців = [12, 15, 70, 45]
# if max(здогади_гравців) > вгадай_це_число:
    # print("Ха! Ви всі програли")
# else:
    # print("Ви виграли")

# for x in range(0, 5):
    # print(x)
# print(list(range(0, 5)))
# рахуй_по_два = list(range(0, 30, 2))
# print(рахуй_по_два)
# зворотній_відлік = list(range(40, 10, -2))
# print(зворотній_відлік)

# мій_список_чисел = list(range(0, 500, 50))
# print(мій_список_чисел)
# print(sum(мій_список_чисел))

# test_file = open("C:\\Users\\IRONKAGE\\Desktop\\test.txt")
# text = test_file.read()
# print(text)
# test_file = open("C:\\Users\\IRONKAGE\\Desktop\\test.txt" , 'w')
# test_file.write("це мій тестовий файл")
# test_file = open("C:\\Users\\IRONKAGE\\Desktop\\test.txt" , 'w')
# test_file.write("Що зелене й голосне? Жаба з рупором!")
# test_file.close()
# test_file = open("C:\\Users\\IRONKAGE\\Desktop\\test.txt")
# print(test_file.read())


    # Д/З №1 - Загадковий код
# a = abs(10) + abs(-10)
# print(a)
# b = abs(-10) + -10
# print(b)


    # Д/З №2 - Приховане повідомлення
# не_зрозуміла_стрічка = "Це якщо не ти дуже це хороший читаєш спосіб то заховати щось повідомлення негаразд"
# print(dir("не_зрозуміла_стрічка"))
# print(help(не_зрозуміла_стрічка.split))
# зрозуміла_стрічка = не_зрозуміла_стрічка.split()
# for x in range(0, len(зрозуміла_стрічка), 2):
    # print(зрозуміла_стрічка[x])

    
    # Д/З №3 - Копіювання файла
# test_file = open("C:\\Users\\IRONKAGE\\Desktop\\test.txt")
# create_file = test_file.read()
# test_file.close()
# test_file = open("C:\\Users\\IRONKAGE\\Desktop\\test2.txt", 'w')
# test_file.write(create_file)
# test_file.close()
# import shutil
# shutil.copy("test.txt", "test3.txt")


                            # №10 - Корисні модулі в мові Python


# import turtle
# t = turtle.Pen()

# class Тварина:
    # def __init__(self, вид, кількість_ніг, забарвлення):
        # self.вид = вид
        # self.кількість_ніг = кількість_ніг
        # self.забарвлення = забарвлення
# Гаррі = Тварина("Гіпогриф", 6, "рожевий")
# import copy
# Гаррі = Тварина("Гіпогриф", 6, "рожевий")
# Гаррієт = copy.copy(Гаррі)
# print(Гаррі.вид)
# print(Гаррієт.вид)
# Гаррі = Тварина("Гіпогриф", 6, "рожевий")
# Керрі = Тварина("Химера", 4, "в зелені крапочки")
# Біллі = Тварина("Велетень", 0, "з візерунком")
# Мої_тварини = [Гаррі, Керрі, Біллі]
# Більше_тварин = copy.copy(Мої_тварини)
# print(Більше_тварин[0].вид)
# print(Більше_тварин[1].вид)
# Мої_тварини [0].вид = "Упир"
# print(Мої_тварини[0].вид)
# print(Більше_тварин[0].вид)
# Саллі = Тварина("Сфінкс", 4, "Піщаний")
# Мої_тварини.append(Саллі)
# print(len(Мої_тварини))
# print(len(Більше_тварин))
# Більше_тварин = copy.deepcopy(Мої_тварини)
# Мої_тварини[0].вид = "Змій"
# print(Мої_тварини[0].вид)
# print(Більше_тварин[0].вид)

# import keyword
# print (keyword.iskeyword('if'))
# print (keyword.iskeyword('ozwald'))
# print (keyword.kwlist)

# import random
# print(random.randint(1, 100))
# print(random.randint(100, 1000))
# print(random.randint(1000, 5000))

# import random
# число = random.randint(1, 100)
# while True:
    # print('Вгадай число між 1 і 100')
    # здогад = input()
    # i = int(здогад)
    # if i == число:
        # print('Правильний здогад')
        # break
    # elif i < число:
        # print('Бери вище')
    # elif i > число:
        # print('Бери нижче')
        
# import random
# Десерти = ['Морозивко', 'Млинці', 'Шоколадне тістечко', 'Печиво', 'Цукерка']
# print(random.choice(Десерти))

# import random
# Десерти = ['Морозивко', 'Млинці', 'Шоколадне тістечко', 'Печиво', 'Цукерка']
# random.shuffle(Десерти)
# print(Десерти)

# import sys
# sys.exit()
# print(exit)

# import sys
# v = sys.stdin.readline()
# Той, хто сміється останнім, думає найповільніше
# print(v)

# import sys
# v = sys.stdin.readline(12)
# Той, хто сміється останнім, думає найповільніше
# print(v)

# import sys
# sys.stdout.write("Що каже риба, коли врызаэться в стыну? Припливли!")

# import sys
# print(sys.version)

# import time
# print(time.time())
# def Багато_чисел(Макс):
    # T1 = time.time()
    # for x in range(0, Макс):
        # print(x)
        # T2 = time.time()
        # print('Знадобилося %s секунд' % (T2 - T1))
# Багато_чисел(1000)

# import time
# print(time.asctime())
# import time
# T1 = (2007, 5, 27, 10, 30, 48, 6, 0, 0)
# print(time.asctime(T1))
# T2 = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
# print(time.asctime(T2))

# import time
# print(time.localtime())
# T = time.localtime()
# Рік = T[0]
# Місяць = T[1]
# print(Рік)
# print(Місяць)

# import time
# for x in range(1, 61):
    # print(x)
    # time.sleep(1)

# import pickle
# Дані_гри = {
    # 'Позиція': 'Пн23 Сх 45',
    # 'Кишені': ['Ключі', 'Складний ножик', 'Гладкий камінець'],
    # 'Ранець': ['Мотузка', 'Молоток', 'Яблуко'],
    # 'Гроші': 158.50
# }
# Файл = open('save.dat', 'wb')
# pickle.dump(Дані_гри, Файл)
# Файл.close()
# Збережений_файл = open('save.dat', 'rb')
# Завантажені_дані_гри = pickle.load(Збережений_файл)
# Збережений_файл.close
# print(Завантажені_дані_гри)


    # Д/З №1 - Скопійовані машини
# import copy
# class Машина:
    # pass
# Машина_1 = Машина()
# Машина_1.Колеса = 4
# Машина_2 = Машина_1
# Машина_2.Колеса = 3
# print(Машина_1.Колеса)
# Машина_3 = copy.copy(Машина_1)
# Машина_3.Колеса = 6
# print(Машина_1.Колеса)


    # Д/З №2 - Збережені улюблені речі
# import pickle
# Улюблені_речі = {
    # 'Планшети': ['Surface Pro 2017', 'iPad Pro 12" 2018', 'Galaxy Tab S6'],
    # 'Автомобілі': ['Tesla', 'BMW'],
    # 'Книга': 'Біблія'
# }
# Файл = open('favorites.dat', 'wb')
# pickle.dump(Улюблені_речі, Файл)
# Файл.close()
# Збережений_файл = open('favorites.dat', 'rb')
# Завантажені_дані_улюбленного = pickle.load(Збережений_файл)
# Збережений_файл.close
# print(Завантажені_дані_улюбленного)


                            # №11 - І знову малювання "ЧЕРЕПАХОЮ"


# import turtle
# t = turtle.Pen()
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.reset()
# for x in range(1, 5):
    # t.forward(50)
    # t.left(90)

# import turtle
# t = turtle.Pen()
# for x in range(1, 9):
    # t.forward(100)
    # t.left(225)
# t.reset()
# for x in range(1, 38):
    # t.forward(100)
    # t.left(175)
# t.reset()
# for x in range(1, 20):
    # t.forward(100)
    # t.left(95)
# t.reset()
# for x in range(1, 19):
    # t.forward(100)
    # if x % 2 == 0:
        # t.left(175)
    # else:
        # t.left(225)

# import turtle
# import time
# t = turtle.Pen()
# t.color(1, 0, 0)
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(20)
# t.left(90)
# t.forward(20)
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(60)
# t.left(90)
# t.forward(20)
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(20)
# t.end_fill()
# t.color(0, 0, 0)
# t.up()
# t.forward(10)
# t.down()
# t.begin_fill()
# t.circle(10)
# t.end_fill()
# t.setheading(0)
# t.up()
# t.forward(90)
# t.right(90)
# t.forward(10)
# t.setheading(0)
# t.begin_fill()
# t.down()
# t.circle(10)
# t.end_fill()
# time.sleep(15)

# import turtle
# import time
# t = turtle.Pen()
# t.color(1, 1, 0)
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# time.sleep(5)

# import turtle
# import time
# t = turtle.Pen()
# def Моє_коло(червоний, зелений, синій):
    # t.color(червоний, зелений, синій)
    # t.begin_fill()
    # t.circle(50)
    # t.end_fill()
# Моє_коло(0, 1, 0)
# Моє_коло(0, 0.5, 0)
# Моє_коло(1, 0, 0)
# Моє_коло(0.5, 0, 0)
# Моє_коло(0, 0, 1)
# Моє_коло(0, 0, 0.5)
# Моє_коло(0.9, 0.75, 0)
# Моє_коло(1, 0.7, 0.75)
# Моє_коло(1, 0.5, 0)
# Моє_коло(0.9, 0.5, 0.15)
# Моє_коло(0, 0, 0)
# Моє_коло(1, 1, 1)
# time.sleep(5)

# import turtle
# import time
# t = turtle.Pen()
# def Мій_квадрат(сторона):
    # for x in range(1, 5):
        # t.forward(сторона)
        # t.left(90)
# Мій_квадрат(50)
# t.reset()
# Мій_квадрат(25)
# Мій_квадрат(50)
# Мій_квадрат(75)
# Мій_квадрат(100)
# Мій_квадрат(125)
# time.sleep(5)

# t.reset()
# t.begin_fill()
# Мій_квадрат(50)
# t.end_fill()
# t.reset()
# import turtle
# import time
# t = turtle.Pen()
# def Мій_квадрат(сторона, заповнити):
    # if заповнити == True:
        # t.begin_fill()
    # for x in range(1, 5):
        # t.forward(сторона)
        # t.left(90)
    # if заповнити == True:
        # t.end_fill()
# Мій_квадрат(50, True)
# Мій_квадрат(150, False)
# time.sleep(5)

# import turtle
# import time
# t = turtle.Pen()
# for x in range(1, 19):
    # t.forward(100)
    # if x % 2 == 0:
        # t.left(175)
    # else:
        # t.left(225)
# t.reset()
# def Моя_зірка(промінь, заповнити):
    # if заповнити == True:
        # t.begin_fill()
    # for x in range(1, 19):
        # t.forward(промінь)
        # if x % 2 == 0:
            # t.left(175)
        # else:
            # t.left(225)
    # if заповнити == True:
        # t.end_fill()
# t.color(0.9, 0.75, 0)
# Моя_зірка(120, True)
# t.color(0, 0, 0)
# Моя_зірка(120, False)
# time.sleep(5)


    # Д/З №1 - Малювання восьмикутника
# import turtle
# import time
# t = turtle.Pen()
# def Мій_восьмикутник(сторона):
    # for x in range(1, 9):
        # t.forward(сторона)
        # t.left(45)
# Мій_восьмикутник(50)
# time.sleep(5)


    # Д/З №2 - Малювання зафарбованого восьмикутника
# import turtle
# import time
# t = turtle.Pen()
# def Мій_восьмикутник(сторона, заповнити):
    # if заповнити == True:
        # t.begin_fill()
    # for x in range(1, 9):
        # t.forward(сторона)
        # t.left(45)
    # if заповнити == True:
        # t.end_fill()
# t.color(0.7, 0.7, 0.7)
# Мій_восьмикутник(50, True)
# t.color(1, 0, 0)
# Мій_восьмикутник(50, False)
# time.sleep(5)


    # Д/З №3 - Ще одна функція малювання зірки
# import turtle
# import time
# t = turtle.Pen()
# def Моя_зірка(промінь, вершин):
    # кут = 360 / вершин
    # for x in range(0, вершин):
        # t.forward(промінь)
        # t.left(180 - кут)
        # t.forward(промінь)
        # t.right(180-(кут * 2))
# t.color(1, 0.7, 0.7)
# Моя_зірка(50, 5)
# time.sleep(5)


                            # №12 - Як покращити графіку з "TKINTER"


# from tkinter import *
# tk = Tk()
# btn = Button(tk, text = "Клацни мене")
# btn.pack()
# import turtle
# t = turtle.Pen()
# from turtle import *
# t = Pen()
# def Здоров():
    # print('Здоровенькі були')
# from tkinter import *
# tk = Tk()
# btn = Button(tk, text = "Клацни мене", command=Здоров)
# btn.pack()
# input('Натисніть ENTER для виходу')


# def Людина(ширина, висота):
    # print('Моя ширина %s см, моя висота %s см' % (ширина, висота))
# Людина(50, 180)
# Людина(висота=180, ширина=50)

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# canvas.create_line(0, 0, 500, 500)
# import turtle
# turtle.setup(width=500, height=500)
# t = turtle.Pen()
# t.up()
# t.goto(-250, 250)
# t.down()
# t.goto(250, -50)
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_rectangle(10, 10, 50, 50)
# input('Натисніть ENTER для виходу')
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_rectangle(10, 10, 300, 50)
# input('Натисніть ENTER для виходу')
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_rectangle(10, 10, 50, 300)
# input('Натисніть ENTER для виходу')

# from tkinter import *
# import random
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# def random_rectangle(width, height):
    # X1 = random.randrange(width)
    # Y1 = random.randrange(height)
    # X2 = X1 + random.randrange(width)
    # Y2 = Y1 + random.randrange(height)
    # canvas.create_rectangle(X1, Y1, X2, Y2)
# random_rectangle(400, 400)
# for x in range(0, 100):
    # random_rectangle(400, 400)
# input('Натисніть ENTER для виходу')

# from tkinter import *
# import random
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# def random_rectangle(width, height, fill_color):
    # X1 = random.randrange(width)
    # Y1 = random.randrange(height)
    # X2 = X1 + random.randrange(width)
    # Y2 = Y1 + random.randrange(height)
    # canvas.create_rectangle(X1, Y1, X2, Y2, fill=fill_color)
# random_rectangle(400, 400, 'green')
# random_rectangle(400, 400, 'red')
# random_rectangle(400, 400, 'blue')
# random_rectangle(400, 400, 'orange')
# random_rectangle(400, 400, 'yellow')
# random_rectangle(400, 400, 'pink')
# random_rectangle(400, 400, 'purple')
# random_rectangle(400, 400, 'violet')
# random_rectangle(400, 400, 'magenta')
# random_rectangle(400, 400, 'cyan')
# random_rectangle(400, 400, '#FFD800')
# print('%x' % 15)
# print('%02x' % 15)
# from tkinter import colorchooser
# colorchooser.askcolor()
# c = colorchooser.askcolor()
# random_rectangle(400, 400, c[1])
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_arc(10, 20, 200, 100, extent=180, style=ARC)
# canvas.create_arc(10, 20, 200, 100, extent=180, style=CHORD)
# canvas.create_arc(10, 20, 200, 100, extent=180, style=PIESLICE)
# canvas.create_arc(10, 20, 200, 80, extent=45, style=ARC)
# canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
# canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
# canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
# canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="black")
# canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", outline="black")
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_text(150, 100, text='Жив собі хлопець у Молдові,')
# canvas.create_text(130, 120, text='Катався кругом на корові,', fill='red')
# canvas.create_text(150, 150, text='Така-от, каже, біда,', font=('Times', 15))
# canvas.create_text(200, 200, text='І зовсім вона не одна:', font=('Helvetica', 20))
# canvas.create_text(220, 250, text='Тата возять', font=('Courier', 22))
# canvas.create_text(220, 300, text='дві курки здорові!', font=('Courier', 26))
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# My_image = PhotoImage(file='demo.gif')
# canvas.create_image(0, 0, anchor=NW, image=My_image)
# input('Натисніть ENTER для виходу')

# import time
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=200)
# canvas.pack()
# canvas.create_polygon(10, 10, 10, 60, 50, 35)
# for x in range(0, 60):
    # canvas.move(1, 5, 0)
    # tk.update()
    # time.sleep(0.05)
# input('Натисніть ENTER для виходу')
# import time
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_polygon(10, 10, 10, 60, 50, 35)
# for x in range(0, 60):
    # canvas.move(1, 5, 5)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, -5, -5)
    # tk.update()
    # time.sleep(0.05)
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=700, height=400)
# canvas.pack()
# canvas.create_polygon(10, 10, 10, 60, 50, 35)
# def move_triangle(event):
    # canvas.move(1, 5, 0)
    # if event.keysym == 'Up':
        # canvas.move(1, 0, -3)
    # elif event.keysym == 'Down':
        # canvas.move(1, 0, 3)
    # elif event.keysym == 'Left':
        # canvas.move(1, -3, 0)
    # else:
        # canvas.move(1, 3, 0)
# canvas.bind_all('<KeyPress-Return>', move_triangle)
# canvas.bind_all('<KeyPress-Up>', move_triangle)
# canvas.bind_all('<KeyPress-Down>', move_triangle)
# canvas.bind_all('<KeyPress-Left>', move_triangle)
# canvas.bind_all('<KeyPress-Right>', move_triangle)
# input('Натисніть ENTER для виходу')

# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=700, height=400)
# canvas.pack()
# canvas.create_polygon(10, 10, 10, 60, 50, 35)
# canvas.move(1, 5, 0)
# My_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')
# canvas.move(My_triangle, 5, 0)
# canvas.itemconfig(My_triangle, fill='blue')
# canvas.itemconfig(My_triangle, outline='red')
# input('Натисніть ENTER для виходу')


    # Д/З №1 - Заповнити екран трикутниками
# from tkinter import *
# import random
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# colors = ['red', 'blue', 'yellow', 'pink', 'green', 'orange', 'black', 'white']
# def random_triangle(width, height):
    # X1 = random.randrange(width)
    # Y1 = random.randrange(height)
    # Z1 = random.randrange(width)
    # X2 = random.randrange(width)
    # Y2 = random.randrange(height)
    # Z2 = random.randrange(height)
    # color = random.choice(colors)
    # canvas.create_polygon(X1, Y1, Z1, X2, Y2, Z2, fill=color, outline='black')
# for x in range(0, 100):
    # random_triangle(400, 400)
# input('Натисніть ENTER для виходу')


    # Д/З №2 - Трикутник, який рухається
# import time
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_polygon(10, 10, 10, 60, 50, 35)
# for x in range(0, 60):
    # canvas.move(1, 5, 0)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, 0, 5)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, -5, 0)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, 0, -5)
    # tk.update()
    # time.sleep(0.05)
# input('Натисніть ENTER для виходу')

    # Д/З №3 - Фото, яке рухається
# import time
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=800, height=650)
# canvas.pack()
# My_image = PhotoImage(file='demo.gif')
# canvas.create_image(300, 300, anchor=NW, image=My_image)
# for x in range(0, 60):
    # canvas.move(1, -5, 0)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, 0, -5)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, 5, 0)
    # tk.update()
    # time.sleep(0.05)
# for x in range(0, 60):
    # canvas.move(1, 0, 5)
    # tk.update()
    # time.sleep(0.05)
# input('Натисніть ENTER для виходу')


                            # №13-№14 - Гра "СКОК"


# from tkinter import *
# import random
# import time

# class Ball:
    # def __init__(self, canvas, paddle, score, color):
        # self.canvas = canvas
        # self.paddle = paddle
        # self.score = score
        # self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # self.canvas.move(self.id, 245, 100)
        # starts = [-3, -2, -1, 1, 2, 3]
        # random.shuffle(starts)
        # self.x = starts[0]
        # self.y = -3
        # self.canvas_height = self.canvas.winfo_height()
        # self.canvas_width = self.canvas.winfo_width()
        # self.hit_bottom = False

    # def hit_paddle(self, pos):
        # paddle_pos = self.canvas.coords(self.paddle.id)
        # if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            # if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # self.x += self.paddle.x
                # self.score.hit()
                # return True
            # return False

    # def draw(self):
        # self.canvas.move(self.id, self.x, self.y)
        # pos = self.canvas.coords(self.id)
        # if pos[0] <= 0:
            # self.x = 3
        # if pos[1] <= 0:
            # self.y = 1
        # if pos[2] >= self.canvas_width:
            # self.x = -3
        # if pos[3] >= self.canvas_height:
            # self.hit_bottom = True
        # if self.hit_paddle(pos) == True:
            # self.y = -3
        # print(self.canvas.coords(self.id))

# class Paddle:
    # def __init__(self, canvas, color):
        # self.canvas = canvas
        # self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # self.canvas.move(self.id, 200, 300)
        # self.x = 0
        # self.canvas_width = self.canvas.winfo_width()
        # self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # self.started = False
        # self.canvas.bind_all('<Button-1>', self.start_game)

    # def draw(self):
        # self.canvas.move(self.id, self.x, 0)
        # pos = self.canvas.coords(self.id)
        # if pos[0] <= 0:
            # self.x = 0
        # elif pos[2] >= self.canvas_width:
            # self.x = 0

    # def turn_left(self, evt):
        # self.x = -2
    
    # def turn_right(self, evt):
        # self.x = 2
        
    # def start_game(self, evt):
        # self.started = True

# class Score:
    # def __init__(self, canvas, color):
        # self.score = 0
        # self.canvas = canvas
        # self.id = canvas.create_text(450, 10, text=self.score, fill=color)

    # def hit(self):
        # self.score += 1
        # self.canvas.itemconfig(self.id, text=self.score)

# tk = Tk()
# tk.title("Гра")
# tk.resizable(0, 0)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()

# score = Score(canvas, 'green')
# paddle = Paddle(canvas, 'blue')
# ball = Ball(canvas, paddle, score, 'red')
# game_over = canvas.create_text(250, 170, text='КІНЕЦЬ ГРИ', state='hidden')

# while 1:
    # if ball.hit_bottom == False and paddle.started == True:
        # ball.draw()
        # paddle.draw()
    # if ball.hit_bottom == True:
        # time.sleep(0.1)
        # canvas.itemconfig(game_over, state='normal')
    # tk.update_idletasks()
    # tk.update()
    # time.sleep(0.01)