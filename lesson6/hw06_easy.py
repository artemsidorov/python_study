# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle:
    # функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.A = [x1, y1]
        self.B = [x2, y2]
        self.C = [x3, y3]
        self.AB = round(((abs(x1) - abs(x2)) ** 2 + (abs(y1) - abs(y2)) ** 2) ** 0.5, 4)
        self.BC = round(((abs(x3) - abs(x2)) ** 2 + (abs(y3) - abs(y2)) ** 2) ** 0.5, 4)
        self.CA = round(((abs(x1) - abs(x3)) ** 2 + (abs(y1) - abs(y3)) ** 2) ** 0.5, 4)
    # метод
    def per(self):
        return round(self.AB + self.BC + self.CA, 4)
    
    def half_per(self):
        half_perimetr = 0.5 * self.per()
        return round(half_perimetr, 4)
    
    def area_triangle(self):
        p = self.half_per()
        self.area = round((p * (p - self.AB) * (p - self.BC) * (p - self.CA)) ** 0.5, 4)
        return self.area
    
    def high_BC(self):#Высота треугольника по основанию BC
        high = 2 * self.area_triangle() / self.BC
        return high
    
    def high_AB(self):#Высота треугольника по основанию AB
        high = 2 * self.area_triangle() / self.AB
        return high
    
    def high_CA(self):#Высота треугольника по основанию CA
        high = 2 * self.area_triangle() / self.CA
        return high
    
triangle_1 = Triangle(0, 0, 4, 6, 10, 0)
print(triangle_1.AB, triangle_1.BC, triangle_1.CA)
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.A = [x1, y1]
        self.B = [x2, y2]
        self.C = [x3, y3]
        self.D = [x4, y4]
    #методы
    #1. Методы определения 4 сторон через вектора
    def AB(self):
        return round(((abs(self.A[0]) - abs(self.B[0])) ** 2 + (abs(self.A[1]) - abs(self.B[1])) ** 2) ** 0.5, 4)
    
    def BC(self):
        return round(((abs(self.C[0]) - abs(self.B[0])) ** 2 + (abs(self.C[1]) - abs(self.B[1])) ** 2) ** 0.5, 4)
    
    def CD(self):
        return round(((abs(self.C[0]) - abs(self.D[0])) ** 2 + (abs(self.C[1]) - abs(self.D[1])) ** 2) ** 0.5, 4)
    
    def DA(self):
        return round(((abs(self.A[0]) - abs(self.D[0])) ** 2 + (abs(self.A[1]) - abs(self.D[1])) ** 2) ** 0.5, 4)
    
    #2. Проверка признаков равнобокой трапеции
    def eql_condition(self):
        diag_1 = round(((abs(self.A[0]) - abs(self.C[0])) ** 2 + (abs(self.A[1]) - abs(self.C[1])) ** 2) ** 0.5, 4)
        diag_2 = round(((abs(self.B[0]) - abs(self.D[0])) ** 2 + (abs(self.B[1]) - abs(self.D[1])) ** 2) ** 0.5, 4)
        k1 = abs(self.A[1] - self.D[1]) / abs(self.A[0] - self.D[0])#Трапеция с параллельными сторонами BC и DA
        k2 = abs(self.B[1] - self.C[1]) / abs(self.B[0] - self.C[0])
        k3 = abs(self.A[1] - self.B[1]) / abs(self.A[0] - self.B[0])#Трапеция с параллельными сторонами AB и CD
        k4 = abs(self.C[1] - self.D[1]) / abs(self.C[0] - self.D[0])
        if k1 == k2 or k3 == k4:
            if diag_1 == diag_2:
                return 'Равнобокая трапеция'
            else: 
                return 'Неравнобокая трапеция'
        else:
            return 'Это не трапеция'
    def perimetr(self):
        return self.AB() + self.BC() + self.CD() + self.DA()
    
    def area(self):
        a = self.AB()
        b = self.BC()
        c = self.CD()
        d = self.DA()
        if self.eql_condition() == 'Равнобокая трапеция':
            return (d + b) / 2 * (c ** 2 - (a - b) ** 2 / 4) ** 0.5
        else:
            return 'Не буду считать'

trap1 = Trapezoid(0, 0, 5, 5, 10, 5, 15, 0)
print(trap1.eql_condition(), '\n', trap1.area(), '\n', trap1.perimetr())  