# Все задачи текущего блока решите с помощью генераторов списков!
__author__ = 'Сидоров Артем Андреевич'
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
new_list = list(map(lambda x: pow(x, 2), [random.randint(0, 11) for i in range(10)]))
print(new_list)
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits_1 = ['apples', 'oranges', 'pears', 'bananas', 'lemons']
fruits_2 = ['oranges', 'lemons', 'water melons', 'pears', 'peaches']
fruit_list = [i for i in fruits_1 if i in fruits_1 and i in fruits_2] 
#Размер рассматриваемого списка не важен в данных условиях
print(fruit_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random #Оставил с целью переносимости в другой файл себе
test_list = [random.randint(-20, 30) for _ in range(random.randint(1, 20))]
print(f'Базовый список {test_list}')
new_list = [i for i in test_list if i % 3 == 0 and i >= 0 and i % 4 > 0]
print(f'Новый список {new_list}')