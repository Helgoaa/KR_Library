from domain_models.actions import *
from repository.library import *
from ui.pdfView import PDFView
import ui.ui as ui


class Menu(PDFView):
    def __init__(self, library):
        super().__init__()
        self.library = library        

    def menu_output(self):
        
        print(f"Сейчас в библиотеке {self.library.count()} книг.\n"
              f"Введите '{Actions.PrintAll.value}' - для вывода всех книг\n"
              f"Введите '{Actions.PrintAt.value}' - для вывода детальной информации о книге\n"
              f"Введите '{Actions.AddBook.value}' - для добавления книги\n"
              f"Введите '{Actions.UpdateAt.value}' - для изменения данных \n"
              f"Введите '{Actions.RemoveBook.value}' - для удаления книги \n"
              f"Введите '{Actions.FindByAuthor.value}' - для поиска книги по автору\n"
              f"Введите '{Actions.FindByYear.value}' - для поиска книги по году\n"
              f"Введите '{Actions.FindByTitle.value}' - для поиска книги по названию\n"
              f"Введите '{Actions.Exit.value}' - для выхода\n"
              f"Введите '{Actions.Back.value}' - для выхода из действия\n")

    def handle_input(self):
        while True:
            user_input = get_int()
            if user_input == Actions.Exit.value:
                break
            elif user_input == Actions.AddBook.value:
                title=input('Введите название книги: ')
                if title == str(Actions.Back.value):
                    ui.get_sting()
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    self.library.add(Book(title, 
                                          year=int(input('Введите год: ')), 
                                          author=input('Введите автора: ')))
                    print('Книга добавлена!')                
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)   
                continue
            
            elif user_input == Actions.RemoveBook.value:
                index = int(input('Введите индекс книги,которую необходимо удалить: '))
                if index == Actions.Back.value:
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    self.library.remove_at(index)
                    print('Книга успешна удалена!')                         
                    ui.get_sting()
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)                   
                    continue
            
            elif user_input == Actions.FindByAuthor.value:
                author = input('Введите автора книги: ')
                if author == str(Actions.Back.value):
                    ui.get_sting()
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    res = self.library.find_by_author(author)
                    print('Найдены книги:', *res, sep='\n')
                    
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)   
                continue
            
            elif user_input == Actions.FindByYear.value:
                year = int(input('Введите год книги: '))
                if year == Actions.Back.value:
                    ui.get_sting()
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    res = self.library.find_by_year(year)
                    print('Найдены книги:', *res, sep='\n')
                
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)                
                continue
            
            elif user_input == Actions.FindByTitle.value:
                title = input('Введите название книги: ')
                if title == str(Actions.Back.value):
                    ui.get_sting()
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    res = self.library.find_by_title(title)
                    print('Найдены книги:', *res, sep='\n')
                
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)                
                continue
                
            elif user_input == Actions.PrintAt.value:
                index = int(input('Введите индекс книги для получения детальной информации: '))                
                if index == int(Actions.Back.value):
                    ui.get_sting()
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    res = self.library.get_at(index)
                    print('Детальная информация о книге: ', res)
                
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)
                
            elif user_input == Actions.UpdateAt.value:
                index = int(input('Введите индекс книги, которую необходимо редактировать: '))
                if index == Actions.Back.value:
                    ui.clear()
                    menu = self.menu_output()
                    print(menu)
                else:
                    year = int(input('Введите измененный год: '))            
                    title = input('Введедите название книги: ')
                    author = input('Введите автора: ')
                    book = Book (title, year, author)
                    self.library.update_at(index, book)
                
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)
                
            elif user_input == Actions.PrintAll.value:
                res = self.library.get_all_books()
                s = 'Список книг в библиотеке:'
                print(s, *res, sep='\n')
                
                self.create_pdf()
                self.write_to_pdf(s + '\n')
                for i in res:
                    self.write_to_pdf(i + '\n')
                self.output_pdf()
                print('Книги успешно добавлены в pdf файл')
                
                ui.get_sting()
                ui.clear()
                menu = self.menu_output()
                print(menu)

def get_int():
    user_input = None
    while True:
        try:
            user_input = int(input('Введите целое число.\n'))
            return user_input
        except:
            print(f'{user_input} - не целое число.')
            
           

