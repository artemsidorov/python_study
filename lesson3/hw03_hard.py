# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
zp = {}
hours = {}
with open('C:\\Users\\Артем\\Desktop\\lesson03\\home_work\\data\\workers', encoding="utf-8") as doc:
    for i in doc:
        data = i.strip().split()
        zp[str(data[0]) +' ' + str(data[1])] = [data[i] for i in range(2, len(data))]

with open('C:\\Users\\Артем\\Desktop\\lesson03\\home_work\\data\\hours_of', encoding="utf-8") as doc:
    for i in doc:
        data = i.strip().split()
        hours[str(data[0]) +' ' + str(data[1])] = [data[2]]

for i in zp.keys():
    if i in hours.keys():
        zp.update({i: zp[i] + hours[i]})

for i in zp.keys():
    if zp[i][0] == 'Зарплата':
        continue
    else:
        norma_zp = int(zp[i][0])
        norma_chasov = int(zp[i][2])
        virabotka = int(zp[i][3])
        if norma_chasov > virabotka:
            obshaya_zp = round(norma_zp - (norma_chasov - virabotka) * norma_zp / norma_chasov, 2)
        elif norma_chasov < virabotka:
            obshaya_zp = round(norma_zp + abs(norma_chasov - virabotka) * 2 * norma_zp / norma_chasov, 2)
        else:
            obshaya_zp = norma_zp
    zp.update({i: zp[i] + [obshaya_zp]})
print(zp)
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
'''
dop_list = []
with open('C:\\Users\\Артем\\Desktop\\lesson03\\home_work\\data\\fruits.txt', encoding="utf-8") as doc:
    for i in doc:
        if i.strip() == '':
            pass
        else:
            dop_list.append(i.strip())
a_z = list(map(chr, range(ord('А'), ord('Я')+1)))

for i in a_z:
    fruits_w = []
    for fruit in dop_list:
        if fruit[0] == i:
            fruits_w.append(fruit)
    my_file = open(f'C:\\Users\\Артем\\Desktop\\lesson03\\home_work\\data\\fruits_{i}.txt', 'w')
    for fruit in fruits_w:
        my_file.write(fruit + '\n')
    my_file.close()
'''      
        