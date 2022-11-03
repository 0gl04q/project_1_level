import PySimpleGUI as sg
import random


def form_game():
    # Графический интерфейс
    layout_column = [
            [sg.Text('Генератор MadLibs', justification='center', font=("Verdana", 20, "bold"))],
            [sg.Text('[name] - Данил, Сергей, Петр, ', font=("Verdana", 8)), sg.InputText(key='name', size=(42, 1))],
            [sg.Text('[professional] - Программист, Бульдозерист, Хакер,', font=("Verdana", 8)), sg.InputText(key='professional', size=(25, 1))],
            [sg.Text('[friend] - Витя, Саня, Коля,', font=("Verdana", 8)), sg.InputText(key='friend',)],
            [sg.Multiline(key="text", size=(68, 30))],
            [sg.Submit('Выполнить'), sg.Cancel('Отмена')]
    ]

    # Установка позиции элементов
    layout = [[sg.Column(layout_column, element_justification='center')]]

    # Инициализация объекта окна
    window = sg.Window('MadLibs', layout, grab_anywhere=True)

    # Цикл работы графического интерфейса
    while True:
        event, values = window.read()
        if event == 'Выполнить':
            window.Element("text").Update(submit_button(values))  # Вызов действия кнопки выполнить
        if event in (None, 'Exit', 'Отмена'):  # Выход из цикла
            break  # Закрытие программы


def submit_button(vals):  # Действие кнопки выполнить
    # Начальный список
    sp = {
        'name': ['Данил', 'Сергей', 'Петр'],
        'professional': ['Программист', 'Бульдозерист', 'Хакер'],
        'friend': ['Витя', 'Саня', 'Коля'],
    }

    # Получение текста
    text = vals['text']

    # Добавление новых позиций в список
    for val in vals:
        if vals[val] != '' and val != 'text':
            sp[val] = sp[val] + vals[val].split(',')

    # Обход списка со смешными словами
    for val in sp:
        while text.find(f'[{val}]') != -1:  # Цикл для вставки случайных слов на каждую вставку
            text = text.replace(f'[{val}]', random.choice(sp[f'{val}']), 1)

    return text


if __name__ == '__main__':
    form_game()
