import PySimpleGUI as sg
import random


def form_game():
    layout_column = [
            [sg.Text('Генератор MadLibs', justification='center', font=("Verdana", 20, "bold"))],
            [sg.Text('[name] - Данил, Сергей, Петр, ', font=("Verdana", 8)), sg.InputText(key='name', size=(42, 1))],
            [sg.Text('[professional] - Программист, Бульдозерист, Хакер,', font=("Verdana", 8)), sg.InputText(key='professional', size=(25, 1))],
            [sg.Text('[friend] - Витя, Саня, Коля,', font=("Verdana", 8)), sg.InputText(key='friend',)],
            [sg.Multiline(key="text", size=(68, 30))],
            [sg.Submit('Выполнить'), sg.Cancel('Отмена')]
    ]

    layout = [[sg.Column(layout_column, element_justification='center')]]

    window = sg.Window('My new window', layout, grab_anywhere=True)

    while True:
        event, values = window.read()
        if event == 'Выполнить':
            submit_button(values)
        if event in (None, 'Exit', 'Отмена'):
            break


def submit_button(vals):
    sp = {
        'name': ['Данил', 'Сергей', 'Петр'],
        'professional': ['Программист', 'Бульдозерист', 'Хакер'],
        'friend': ['Витя', 'Саня', 'Коля'],
    }

    text = vals['text']
    for val in vals:
        if vals[val] != '' and val != 'text':
            sp[val] = sp[val] + vals[val].split(',')
        if val == 'text':
            for val_1 in vals:
                if val_1 != 'text':
                    text = text.replace(f'[{val_1}]', random.choice(sp[f'{val_1}']).strip())

    print(text)


if __name__ == '__main__':
    form_game()
