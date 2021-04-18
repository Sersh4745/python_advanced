from book import Book
from reader import Reader
from library import Library


def main():

    while True:
        print("\n"
              " ====== Меню =======" + "\n"
                "1. Показать все книги" + "\n"
                "2. Показать книги в наличии" + "\n"
                "3. Показать книги не в наличии" + "\n"
                "4. Взять книгу" + "\n"
                "5. Вернуть книгу" + "\n"
                "6. Добавить книгу" + "\n"
                "7. Удалить книгу" + "\n"
                "8. Добавить читетеля" + "\n"
                "9. Показать читателей" + "\n"
                "0. Выход" + "\n")

        choice = int(input("Enter Choice: "))
        if choice == 1:
            lib.print_all_books()

        if choice == 2:
            lib.print_list_books_available()

        if choice == 3:
            lib.print_list_books_not_available()

        elif choice == 4:
            request_book_id = input('Введите ID книги: ')
            if not request_book_id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue
            request_name_id = input('Введите ID читателя: ')
            if not request_name_id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue

            lib.give_book(int(request_book_id), int(request_name_id))

        elif choice == 5:
            request2_book_id = input('Введите ID книги: ')
            if not request2_book_id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue
            request2_name_id = input('Введите ID читателя: ')
            if not request2_name_id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue

            lib.return_book(int(request2_book_id), int(request2_name_id))

        elif choice == 6:
            id = input('Введите ID Книги: ')
            if not id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue
            name = input('Введите название Книги: ')
            author = input('Введите Автора Книги: ')
            year = input('Введите год Книги: ')
            if not year.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue

            lib.add_book(Book(int(id), name, author, int(year)))

        elif choice == 7:
            request3_book_id = input('Введите ID книги которую хотите удалить: ')
            if not request3_book_id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue

            lib.remove_book(int(request3_book_id))

        elif choice == 8:
            id = input('Введите ID читателя: ')
            if not id.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue
            name = input('Введите имя читателя: ')
            surname = input('Введите фамилию: ')
            age = input('Введите возвраст: ')
            if not age.isnumeric():
                print('Ошибка, вы ввели не число!')
                continue

            lib.add_reader(Reader(int(id), name, surname, int(age)))
        elif choice == 9:
            lib.print_all_readers()

        elif choice == 0:
            exit()


if __name__ == '__main__':
    lib = Library()
    # if not lib.init_from_files():
    #     lib.init_from_files('books_availible.txt', 'reader_list.txt')
    lib.init_from_files('books_availible.txt', 'reader_list.txt')
    main()
