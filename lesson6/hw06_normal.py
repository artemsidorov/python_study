# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class School:
    def __init__(self):
        pass
    def classes_list(self, teahers):
        cl_list = set()
        for teacher in teachers:
            cl_list.update(teacher.class_list)
        return f'Список всех классов школы: {list(cl_list)}'
    
class Person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
    def get_full_name(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'#Вывод ФИО в заданном формате

class Student(Person):
    def __init__(self, name, surname, patronymic, class_id, ma, pa):
        Person.__init__(self, name, surname, patronymic)
        self.class_id = class_id
        self.ma = ma
        self.pa = pa

    
    def parents(self):
        return f'Родители {self.get_full_name()}: Мама {self.ma}, Папа {self.pa}'
    
    def lesson_list(self, teachers):
            ln_list = []
            for i, teacher in enumerate(teachers):
                if self.class_id in teacher.class_list:
                    ln_list.append(teacher.spec)
            return f'{self.get_full_name()} изучает {ln_list}'
        
        
class Teacher(Person):
    def __init__(self, name, surname, patronymic, teachers_classes, spec):
        Person.__init__(self, name, surname, patronymic)
        self.class_list = [i for i in teachers_classes.split()]
        self.spec = spec
  
class Classes:
    def __init__(self, classes_id):
        self.classes_id = classes_id
    #Вернуть список всех учеников конкретного класа
    def students_list(self, students):
        if students[0].__class__.__name__ == 'Student':
            st_list = []
            for i, student in enumerate(students):
                if student.class_id == self.classes_id:
                    st_list.append(student.get_full_name())
            return f'В классе {self.classes_id} учатся {st_list}'
        else:
            return ('These are not students')
    #Список всех учителей
    def teachers_list(self, teachers):
        if teachers[0].__class__.__name__ == 'Teacher':
            tr_list = []
            for i, teacher in enumerate(teachers):
                if self.classes_id in teacher.class_list:
                    tr_list.append(teacher.get_full_name())
            return f'В классе {self.classes_id} преподают {tr_list}'
        else:
            return ('These are not teachers')
    
    
students = [Student('Петр', 'Петров', 'Иванович', '6F', 'Елена', 'Иван'),  Student('Иван', 'Иванов', 'Петрович', '6F', 'Hope', 'Петр')]
teachers = [Teacher('Алексей', 'Смирнов', 'Юрьевич', '6F 7B 8C 9G 11H', 'math'), Teacher('Николай', 'Сидоров', 'Геннадиевич', '6F 7B 8C', 'biology')]
class1 = Classes('6F')
school = School()
print(class1.students_list(students))
print(class1.teachers_list(teachers))
print(school.classes_list(teachers))
for student in students:
    print(student.parents())
    print(student.lesson_list(teachers))
