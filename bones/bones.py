import random

list_gamers = []


def random_generator_qube(count):
    for i in range(count):
        yield random.randint(1, 6)


def conditions(number, sum_number):
    sumN = 0

    if sum_number == 3:
        sumN = number * 10
    if sum_number == 4:
        sumN = number * 20
    if sum_number == 5:
        sumN = number * 30

    return sumN


def roll_cube(count):
    qube_list = list(random_generator_qube(count))  # Создание списка выброшенных кубиков

    all_sum_points = 0

    # Цикл перебора кубиков для подсчета суммы
    for number in range(1, 7):
        sum_number = 0

        for q in qube_list:  # Подсчет количества кубиков определенного значения
            if number == q:
                sum_number += 1

        sum_points = 0

        if sum_number > 0:  # Подсчет количества очков
            if number == 1:  # Количество очков в кубиках со значением 1
                if sum_number < 3:
                    sum_points += sum_number*10
                else:
                    sum_points += 100
            elif number == 5:  # Количество очков в кубиках со значением 5
                if sum_number < 3:
                    sum_points += sum_number*5
                else:
                    sum_points += conditions(number, sum_number)
            else:  # Количество очков в кубиках со всеми остальными значениями
                sum_points += conditions(number, sum_number)

        # Подсчет общей суммы броска
        all_sum_points += sum_points

    return qube_list, all_sum_points


def minimum(roll, sum_all_rol):
    minn = [50, 450, 950]
    if roll >= minn[0]:
        return roll, minn[0]


def add_player():
    return Gamers(input('Введите имя игрока: '))


class Gamers:
    def __init__(self, nm):
        self.name = nm
        self.point = 0

    def add_point(self, pn):
        self.point += pn

    def display_info(self):
        print(f"Имя: {self.name}\nКоличество очков: {self.point}")


if __name__ == '__main__':
    # инициализация
    print(1)










# amount = input('Введите количество игроков: ')
#
# # Новая игра
# # Создание игроков
# dict_players = {input('Введите имя игрока: '): 0 for a in range(int(amount))}
# print(dict_players)

# Бросок первого игрока

# print(f"Бросок первого игрока: {''.join(n)}")
