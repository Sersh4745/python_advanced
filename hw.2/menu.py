from os import name
import sys
import book
import copy
from library import Library
from reader import Reader_books
def main():
      library_all = copy.copy(book.Books.file)
      Library_absence = list()
      library = Library(book.Books.file,library_all,Library_absence)
      reader = Reader_books()
      name_reader = input("Введите имя читателя: ")
      done=False
      while done==False:
            print(""" ====== Меню =======
                  1. Показать все книги
                  2. Показать книги в наличии
                  3. Показать книги не в наличии
                  4. Взять книгу
                  5. Добавить книгу
                  6. Вернуть книгу
                  7. Удалить книгу
                  8. Выход
                  """)
            choice=int(input("Enter Choice:"))
            if choice == 1:
                        library.display_all_books()
            if choice == 2:
                        library.displayAvailablebooks()
            if choice == 3:
                        library.display_abcence_books()
            elif choice == 4:
                        library.lendBook(reader.take_book())
            elif choice == 5:
                        library.addBook(reader.returnBook())
            elif choice == 6:
                        library.return_book(reader.take_book())
            elif choice == 7:
                        library.del_book(reader.take_book())      
            elif choice == 8:
                  sys.exit()
                  
main()