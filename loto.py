import random
class  bingo_bag:
    def __init__(self):
        self.max_num = [i for i in range(1, 91)]
        self.num = ''
    def num_step(self):
        '''
        Достаем бочонок, возвращаем его номер и удаляем из общей последовательности
        '''
        self.num = random.choice(self.max_num)
        self.max_num.remove(self.num)
        return self.num #self - храним значение выпавшего бочонка для работы с карточкой
    def left_chip(self):
        '''
        Возвращаем количество оставших бочонков
        '''
        return f'Осталось бочонков {len(self.max_num)}'
    def check_bag(self):
        '''
        Проверка пустого мешка
        '''
        if len(self.max_num) == 0:
            self.check = False
            return self.check
    
class bingo_card:
    def __init__(self):
        '''
        Создаем игровое поле из прочерков и последовательность для создания карточки
        '''
        self.play_area = [['-' for _ in range(9)] for __ in range(3)]
        self.range = [i for i in range(1, 91)]
        self.range_sample = random.sample(self.range, 15)
        self.range_sample2 = self.range_sample[:]
        self.card_row = []
    def game_area(self):
        '''
        Создаем 3 ряда из случайных сортированных последовательностей по 5 значений (без повторений) 
        '''
        
        for i in range(3):#В этом цикле печатаем 3 ряда случайных чисел
            self.rand_pattern = ['-', '-', '-', '-', '-', ' ', ' ', ' ', ' ']
            rand_seq = sorted(random.sample(self.range_sample, 5))
            for elem in rand_seq:#В этом цикле удаляем числа из последовательности, чтобы не было дублей
                self.range_sample.remove(elem)
            random.shuffle(self.rand_pattern)
            for i in range(len(self.rand_pattern)):#меняем прочерки на цифра из последовательности
                if self.rand_pattern[i] == '-':
                    self.rand_pattern[i] = rand_seq[0]
                    rand_seq.remove(rand_seq[0])        
            self.card_row.append(self.rand_pattern)
        return self.card_row

    def del_num(self, number):#удаляем число
        for i in range(len(self.card_row)):
            for el in range(len(self.card_row[i])):
                if self.card_row[i][el] == number:
                    self.card_row[i][el] = '-'
                else:
                    pass
        return self.card_row
    def check_card(self, number):#проверяем наличие номера бочонка
        if number in self.range_sample2:
            return True
        else:
            return False
    def condition_win(self):
        a = 0#Зачеркнуты все цифры
        for row in self.card_row:
            for el in row:
                if str(el).isdigit() == True:
                    a += 1
                else:
                    pass
        if a > 0:
            return False
        else:
            return True
    def print_card(self):
        '''
        Печатаем карточку
        '''
        for row in self.card_row:
            for el in row:
                print(el, end=' ')
            print()
        print(22*'*')
#Создаем объекты
bag = bingo_bag()
player = bingo_card()
comp = bingo_card()
#Создаем игровые карты
player.game_area()
comp.game_area()
que = input('Готовы сыграть в лото?: y/n ---- ')
if que == 'y':
    print('****Ваша  карточка****')
    player.print_card()
    print('**Карточка противника**')
    comp.print_card()
    while True:#Главный цикл
        bag.num_step()
        print(f'Выпавший бочонок {bag.num} {bag.left_chip()}')
        print('[1] - Зачеркнуть цифру')
        print('[2] - Продолжить')
        q_game = input('Выберите вариант: 1 или 2?  ')
        #блок проверки игрока:
        if q_game == '1':
            if player.check_card(bag.num) == True:
                player.del_num(bag.num)
            elif player.check_card(bag.num) == False:
                print('Ты проиграл - в твоей карточке нет такого номера!')
                break
        if q_game == '2':
            if player.check_card(bag.num) == True:
                print('Ты проиграл - в твоей карточке есть эта цифра!')
                break
            elif player.check_card(bag.num) == False:
                pass
        #блок проверки компьютера:
        if comp.check_card(bag.num) == True:
                comp.del_num(bag.num)
        print('****Ваша  карточка****')
        player.print_card()
        print('**Карточка противника**')
        comp.print_card()
        #Проверяем - все ли зачеркнуто
        if player.condition_win() == True and comp.condition_win() == False:
            print('Вы победили!')
            break
        elif player.condition_win() == False and comp.condition_win() == True:
            print('Скайнет, с*ка!')
            break
        else:
            print('Играем дальше!')
        