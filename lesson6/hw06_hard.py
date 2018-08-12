# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os
class Employer:
    def __init__(self, name, surname, salary, pos_, clock_norm, clock_output):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.pos_ = pos_
        self.clock_norm = int(clock_norm)
        self.clock_output = int(clock_output)
    def get_name(self):
        name = self.name + ' ' + self.surname
        return name
    def current_sal(self):
        if self.clock_norm <= self.clock_output:
            incr = round(self.salary + (self.clock_output - self.clock_norm) * self.salary / self.clock_norm, 2)
            return f'{self.get_name()} получит {incr}'
        else:
            decr = round(self.salary - abs(self.clock_output - self.clock_norm) * self.salary / self.clock_norm, 2)
            return f'{self.get_name()} получит {decr}'
with open(os.path.join(os.getcwd(), 'workers'), encoding='utf8') as workers, open(os.path.join(os.getcwd(), 'hours_of'), encoding='utf8') as hours :
    output = []
    salary_1 = []

    for line_1 in hours:
        b = line_1.strip().split()
        if b[0] == 'Имя':
            pass
        else:
            output.append(b)
    output.sort(key=lambda i: i[1])
    for line in workers:
        a = line.strip().split()
        if a[0] == 'Имя':
            pass
        else:
            salary_1.append(a)
    salary_1.sort(key=lambda i: i[1])
    print(salary_1)
    print(output)

    for i in range(len(salary_1)):
        worker = Employer(salary_1[i][0], salary_1[i][1], salary_1[i][2], salary_1[i][3], salary_1[i][4], output[i][2])
        print(worker.current_sal())
