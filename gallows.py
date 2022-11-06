import random
import PySimpleGUI as sg


def form():
    # Графический интерфейс
    layout_column = [
        [sg.Text('Виселица', justification='center', font=("Verdana", 20, "bold"))],
        [sg.Text('Слово: ', font=("Verdana", 8)), sg.Text(key='word')],
        [sg.Text('Ошибки: (0)', key='mis', font=("Verdana", 8)), sg.Text(key='mistake')],
        [sg.Text('Буква: ', font=("Verdana", 8)), sg.Input(key='letter', size=(25, 1))],
        [sg.Button('Проверка буквы'), sg.Button('Новое слово')]
    ]

    # Установка позиции элементов
    layout = [
        [sg.Column(layout_column, element_justification='left')]
    ]

    # Инициализация объекта окна
    window = sg.Window('Виселица', layout, grab_anywhere=True)
    word_game = ''  # Игровое слово
    word_with_underline = ''  # Визуализация подчеркивания
    mis_list = []  # Список ошибок

    # Цикл работы графического интерфейса
    while True:
        event, values = window.read()
        if event == 'Новое слово':  # Обработка нажатия кнопки "Новое слово"
            och(window)
            # Очистка переменных
            mis_list = []  # Список ошибок

            # Получение слова и подчеркиваний
            sp = new_word()
            word_game = sp[1]
            word_with_underline = sp[0]
            # Отображение подчеркиваний
            window.Element('word').Update(word_with_underline)

        # Обработка нажатия кнопки "Проверка буквы"
        if event == 'Проверка буквы' and word_game != '' and values['letter'] != '':
            # Создание списка с "подчеркиваниями" и проверкой на ошибку
            sp = check_letter(word_game, word_with_underline, values['letter'])
            word_with_underline = sp[0]

            # Обновление отображения "подчеркиваний" и поля ввода буквы
            window.Element('word').Update(str(word_with_underline))
            window.Element('letter').Update('')

            # Обработка ошибки
            if not sp[1]:
                mis_list.append(values['letter'])
                window.Element('mis').Update(f'Ошибки: ({len(mis_list)})')
                window.Element('mistake').Update(', '.join(mis_list))
                if len(mis_list) >= 6:
                    och(window)  # Очистка интерфейса
                    # Очистка переменных
                    word_game = ''  # Игровое слово
                    word_with_underline = ''  # Визуализация подчеркивания
                    mis_list = []  # Список ошибок

        if event in (None, 'Exit', 'Отмена'):  # Выход из цикла
            break  # Закрытие программы


def och(window):
    window.Element('word').Update('')
    window.Element('letter').Update('')
    window.Element('mis').Update(f'Ошибки: (0)')
    window.Element('mistake').Update('')


def new_word():
    file = open('dict_text.txt', 'r')  # Открыть файл
    list_words = [row.rstrip() for row in file]  # Создание списка слов
    random_word = random.choice(list_words)  # Выбор случайного слова
    file.close()  # Закрытие файла
    # Возврат "подчеркиваний" и случайное слово
    return ' '.join('_' for _ in range(len(random_word))), random_word


def check_letter(word, check_str, letter_ch):
    check_str = list(check_str.replace(' ', ''))  # Подготовка "подчеркиваний"
    count = -1  # счетчик позиции для отображения
    # Перебор букв в слове при условии, что отправленная нами буква присутствует в слове
    if letter_ch.upper() in word:
        for let in word:
            count += 1
            if let == letter_ch.upper():
                check_str[count] = letter_ch.upper()
        return ' '.join(check_str), True
    # Иначе возврат "подчеркиваний" с ошибкой
    else:
        return ' '.join(check_str), False


if __name__ == '__main__':
    form()
