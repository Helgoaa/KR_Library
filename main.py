import peewee
from repository.library import Library
from ui.user_interface import Menu

if __name__ == '__main__':

    try:
        library = Library()
        library.connect()
        m = Menu(library)
        m.menu_output()
        m.handle_input()

    except peewee.InternalError as px:
        print(str(px))
