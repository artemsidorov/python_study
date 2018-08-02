# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
'''
Вызывает слайс из ряда Фибоначчи с индекса элемента n по m
'''
def fibonacci(n, m):
    a = [1, 1]
    i = 1
    while True:
        if i == m:
            return a[n - 1: m - 1] 
            #Уточню: беру слайс не по индексу, а по порядку в списке m = 5 -> 6 элемент
            break
        a.append(a[i] + a[i - 1])
        i += 1

print(f'Элементы с n по m: {fibonacci(1, 9)}')
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    '''
    #Функция создает новый список и в него по очередно дописывает min значения 
    #первого списка, одновременно удаляя их
    '''
    b = []
    for i in range(len(origin_list), 0, -1):
        b.append(min(origin_list))
        origin_list.remove(min(origin_list))
    return b #лучше вернуть список, но для наглядности выведу
print(f'Увеличение списка {sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])}')

def sort_to_max(origin_list): 
    if len(origin_list) <= 1:
       return origin_list
    else:
       splitter = origin_list[len(origin_list) // 2]
    minor = [num for num in origin_list if num < splitter]
    center = [splitter] * origin_list.count(splitter)
    major = [num for num in origin_list if num > splitter]
    return sort_to_max(minor) + center + sort_to_max(major)
print(f'Увеличение списка #2 вариант {sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])}')
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_func(func, my_list):
    new_list = []
    for i in my_list:
        if func(i) == True:
            new_list.append(i)
    return new_list
print(my_func(lambda i: i ** 2 > 10, [1, 2, 3, 5, 4, 15]))
    
#Очень кривая реализация, оставлю для себя, пока не понял где ошибка в передаче анонимной функции
'''
def my_func(condition, my_list):
    new_list = []
    for object in my_list:
        if eval(condition) == True:
            new_list.append(object)
    return new_list
print(my_func('abs(object) - 5 == 0', [1, 2, -1, -2, 3, 5, -5]))
'''
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

        
