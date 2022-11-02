#
# Камень, ножницы, бумага – мини-игра, в которую можно играть в одиночку с компьютером.
#

import random

print('###Камень, ножницы, бумага###')

game_list = ['Камень', 'Ножницы', 'Бумага']  # Список значений игры

repeat = 'Да'

# Цикл повтора игры
while repeat == 'Да':
    com_num = random.choice(game_list)  # Ход компьютера, рандомный выбор значения из списка

    player_num = input('\nВведите один из вариантов - Камень, Ножницы, Бумага: ')  # Ввод значения игроком

    # Условия определение победителя
    if com_num == player_num:
        print('Ничья!')
    elif (com_num == 'Камень' and player_num == 'Ножницы') or (com_num == 'Ножницы' and player_num == 'Бумага') or (com_num == 'Бумага' and player_num == 'Камень'):
        print('Выиграл компьютер\n')
    elif (com_num == 'Ножницы' and player_num == 'Камень') or (com_num == 'Бумага' and player_num == 'Ножницы') or (com_num == 'Камень' and player_num == 'Бумага'):
        print('Выиграл кожаный ублюдок!\n')

    # Определение продолжения игры
    repeat = input('Введите "Да" если хотите продолжить: ')

print('Игра окончена')