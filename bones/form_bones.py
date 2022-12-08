import random
import PySimpleGUI as sg
import bones

data = [
    #     ['Данила', 10],
    #         ['Сергей', 50],
    # ['Сергей', 50],
    # ['Сергей', 50],
    # ['Сергей', 50],
]

data_table = [

]

count_players = 0

headings = ['Имя', 'Очки']

# Графический интерфейс
layout_column = [
    [sg.Text('Кости 1000', justification='center', font=("Verdana", 20, "bold"))],
    [sg.Button('Добавить игрока', key='-ADD_PLAYER-')],
    [sg.Table(values=data, headings=headings, max_col_width=10,
              auto_size_columns=True,
              num_rows=2,
              display_row_numbers=True,
              justification='center',
              key='-TABLE-')],
    # [sg.Text('Слово: ', font=("Verdana", 8)), sg.Text(key='word')],
    # [sg.Text('Ошибки: (0)', key='mis', font=("Verdana", 8)), sg.Text(key='mistake')],
    # [sg.Text('Буква: ', font=("Verdana", 8)), sg.Input(key='letter', size=(2, 1))],
    # [sg.Output(size=(88, 6), key='out')],
    # [sg.Button('Проверка буквы'), sg.Button('Новое слово')]
]

# Установка позиции элементов
layout = [
    [sg.Column(layout_column, element_justification='center')]
]

# Инициализация объекта окна
window = sg.Window('1000', layout, grab_anywhere=True)

# Цикл работы графического интерфейса
while True:
    event, values = window.read()

    if event == "-ADD_PLAYER-":
        if count_players < 2:
            data.append(bones.add_player())
            data_table.append([data[-1].name, data[-1].point])
            count_players += 1
            if count_players == 2:
                window.Element('-ADD_PLAYER-').Update(visible=False)
            window.Element('-TABLE-').Update(data_table)

    if event in (None, 'Exit', 'Отмена'):  # Выход из цикла
        break  # Закрытие программы
