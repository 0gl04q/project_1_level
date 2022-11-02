#
# Угадай число – компьютер выберет случайное число, а игроки должны будут по очереди угадывать число.
#

from random import randint

print('###УГАДАЙ ЧИСЛО###\n')

rand_num = randint(1, 10)
total_num = int()

print('Компьютер выбрал случайное число от 1 до 10!')

while int(total_num) != rand_num:
    total_num = input('Введите предполагаемое число: ')

    if int(total_num) == rand_num:
        print('Вы угадали!!!')
    elif int(total_num) != rand_num:
        print('Вы ошиблись!!!\n')




