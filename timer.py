import sys, os
import bext, time, keyboard
os.system("mode con cols=63 lines=15")
bext.title('Timer')

hours_first_row = 0
hours_second_row = 0

minutes_first_row = 0
minutes_second_row = 0

seconds_first_row = 0
seconds_second_row = 0
left_align = ' ' * 13

numbers = {
    0: [' __ ',
        '|  |',
        '|__|'],
    1: ['    ',
        '   |',
        '   |'],
    2: [' __ ',
        ' __|',
        '|__ '],
    3: [' __ ',
        ' __|',
        ' __|'],
    4: ['    ',
        '|__|',
        '   |'],
    5: [' __ ',
        '|__ ',
        ' __|'],
    6: [' __ ',
        '|__ ',
        '|__|'],
    7: [' __ ',
        '   |',
        '   |'],
    8: [' __ ',
        '|__|',
        '|__|'],
    9: [' __ ',
        '|__|',
        ' __|'],
}

while True:

    bext.clear()
    text = '\n' + '\n'
    text += f'{left_align} {numbers[hours_first_row][0]} {numbers[hours_second_row][0]}   {numbers[minutes_first_row][0]} {numbers[minutes_second_row][0]}   {numbers[seconds_first_row][0]} {numbers[seconds_second_row][0]} \n'
    text += f'{left_align} {numbers[hours_first_row][1]} {numbers[hours_second_row][1]} * {numbers[minutes_first_row][1]} {numbers[minutes_second_row][1]} * {numbers[seconds_first_row][1]} {numbers[seconds_second_row][1]} \n'
    text += f'{left_align} {numbers[hours_first_row][2]} {numbers[hours_second_row][2]} * {numbers[minutes_first_row][2]} {numbers[minutes_second_row][2]} * {numbers[seconds_first_row][2]} {numbers[seconds_second_row][2]} \n'
    print(text)
    print(f'{left_align} Ctrl + C aby wyłączyć')

    # Seconds
    seconds_second_row += 1
    if seconds_second_row > 9:
        seconds_second_row = 0
        seconds_first_row += 1

    # Minutes
    if seconds_first_row >= 6:
        seconds_first_row = 0
        minutes_second_row += 1
    if minutes_second_row > 9:
        minutes_second_row = 0
        minutes_first_row += 1

    # Hours
    if minutes_first_row >= 6:
        minutes_first_row = 0
        hours_second_row += 1
    if hours_second_row > 9:
        hours_second_row = 0
        hours_first_row += 1


    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('\n\nTimer, autor: Michał Pilarski, michalpilarski17@gmail.com')
        print()
        sys.exit()
