import PySimpleGUI as sg
import random


def form():
    # Графический интерфейс
    layout_column = [
        [sg.Text('Генератор паролей', justification='center', font=("Verdana", 20, "bold"))],
        [sg.Text('Введите количество символов в пароле: ', font=("Verdana", 8)), sg.Input(key='len', size=(3, 1))],
        [sg.Text('Новый пароль: ', font=("Verdana", 8)), sg.Input(key='passwd', size=(25, 1))],
        [sg.Submit('Выполнить'), sg.Cancel('Отмена')]
    ]

    # Установка позиции элементов
    layout = [[sg.Column(layout_column, element_justification='center')]]

    # Инициализация объекта окна
    window = sg.Window('Генератор паролей', layout, grab_anywhere=True)

    # Цикл работы графического интерфейса
    while True:
        event, values = window.read()
        if event == 'Выполнить':
            window.Element("passwd").Update(submit_button(values['len']))  # Вызов действия кнопки выполнить
        if event in (None, 'Exit', 'Отмена'):  # Выход из цикла
            break  # Закрытие программы


# Функция создания случайного пароля
def submit_button(length):
    if length.isdigit():  # Проверка на введенное число
        simbols = [chr(i) for i in range(33, 127)]  # Генерация символов ASCII от 33 до 126
        return ''.join(random.choice(simbols) for _ in range(int(length)))  # Генерация пароля с рандомным выбором
    else:  # Обработка неверного ввода
        return ''


if __name__ == '__main__':
    form()
