from book import Book
from reader import Reader
from library import Library


def main():

    library = Library()
    library.init_from_files('hw.2/books_availible.txt', 'hw.2/reader_list.txt')
    #reader_1 = Reader(1, 'Ivan', 'Ivanov', 30)
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
              "0. Выход" + "\n")

        choice = int(input("Enter Choice: "))
        if choice == 1:
            library.print_all_books()

        if choice == 2:
            library.print_list_books_available()

        if choice == 3:
            library.print_list_books_not_available()

        elif choice == 4:
            request_book_id = input('Введите ID книги: ')
            request_name_id = input('Введите ID читателя: ')
            library.give_book(request_book_id, request_name_id)

        elif choice == 5:
            request2_book_id = input('Введите ID книги: ')
            request2_name_id = input('Введите ID читателя: ')
            library.return_book(request2_book_id,request2_name_id)

        elif choice == 6:
            id = input('Введите ID Книги: ')
            name = input('Введите название Книги: ')
            author = input('Введите Автора Книги: ')
            year = input('Введите год Книги: ')
            add_b = [id, name, author, year]

            library.add_book(add_b)
        elif choice == 7:
            request3_book_id = input('Введите ID книги которую хотите удалить: ')
            library.remove_book(request3_book_id)

        elif choice == 8:
            id_r = input('Введите ID читателя: ')
            name_r = input('Введите имя читателя: ')
            surname = input('Введите фамилию: ')
            age = input('Введите возвраст: ')
            add_r = [id_r, name_r, surname, age]

            library.add_reader(add_r)
        elif choice == 0:
            exit()


if __name__ == '__main__':
    main()
