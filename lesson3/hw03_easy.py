# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    if number > 0:
        a = 1 
    else:
        number = abs(number)
        a = -1 #Вводим коэффициент для округления отрицательных чисел
    round_number = str(number).split('.') #Разбиваем число на список из 2 элементов - целой и вещественной частей
    if int(round_number[1][ndigits]) >= 5:
        round_number = a * (int(round_number[0]) + (int(round_number[1][:ndigits]) + 1) * 10 ** (-len(round_number[1][:ndigits])))   
    # Возводим 10 в отрицательную степень количества знаков вещественной части и складываем с целой частью с учетом знака
    elif int(round_number[1][ndigits]) < 5:
        round_number = a * (int(round_number[0]) + (int(round_number[1][:ndigits])) * 10 ** (-len(round_number[1][:ndigits])))
    return(round_number)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = list(str(ticket_number))
    for i in range(len(ticket_number)):
        ticket_number[i] = int(ticket_number[i])
    if sum(ticket_number[:3]) == sum(ticket_number[3:]):
        return 'Lucky'
    else:
        return 'Unlucky'


print(lucky_ticket(123006))
print(lucky_ticket(123213))
print(lucky_ticket(436751))
