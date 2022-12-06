import os

def draw_ui(strings_ui: str):
    print(strings_ui)


def clear():
    clear_console = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear_console()


def get_int():
    user_input = None
    while True:
        try:
            user_input = int(input('Введите целое число.\n')) 
            return user_input
        except:
            print(f'{user_input} - не целое число.')

def get_sting():
    user_input = None
    while True:
        try:
            user_input = str(input('Нажмите Enter для возврата в меню.\n'))
            return user_input
        except Exception as e:
            print(e)
            
