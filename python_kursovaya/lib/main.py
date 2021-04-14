from .book import Book
from .reader import Reader
from .library import Library


def main():
    lib = Library()
    # library.init_from_files('hw.2/books_availible.txt', 'hw.2/reader_list.txt')
    # reader_1 = Reader(1, 'Ivan', 'Ivanov', 30)
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


# if __name__ == '__main__':
#     lib = Library()
#     # if not lib.init_from_files():
#     #     lib.init_from_files('books_availible.txt', 'reader_list.txt')
#     lib.init_from_files('books_availible.txt', 'reader_list.txt')
#     main()





#
# from flask import Flask, render_template, make_response, request, session
#
# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = 'this is a very very secret key'
#
#
# @app.route('/')
# def home():
#     if request.cookies.get('name'):
#         return f'<h1>Home Page. Hello, {request.cookies.get("name")}</h1>'
#     return 'Home Page'
#
#
# @app.route('/cookie/')
# def cookie():
#     res = make_response(f'<h1>Home Cookie</h1>')
#     res.set_cookie('name', 'Ivan', max_age=60 * 2)
#     return res
#
#
# @app.route('/delete-cookie/')
# def delete_cookie():
#     res = make_response(f'<h1>Cookie deleted</h1>')
#     res.set_cookie('name', '', max_age=0)
#     return res
#
#
# @app.route('/visit/')
# def visits():
#     if 'visit' in session:
#         session['visit'] = session.get('visit') + 1
#     else:
#         session['visit'] = 1
#     return f'Count visits = {session.get("visit")}'
#
#
# @app.route('/delete-visit/')
# def delete_visits():
#     session.pop('visit', 'None')
#     return 'Visits deleted'
#
#
# if __name__ == '__main__':
#     app.run()

# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello, World!'
#
#
# def index():
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run()

#
# from flask import Flask, render_template, url_for
# from jinja2 import Environment, FileSystemLoader, select_autoescape
# # from flask_sqlalchemy import SQLALchemy
# from sqlalchemy import create_engine
# from library import Library
# # e = create_engine('postgresql://postgres:133113zz@localhost:5432/postgres')
# # app = Flask(__name__)
# # db = SQLALchemy(e)
# app = Flask(__name__)
#
#
# @app.route('/')
# @app.route('/home')
# def index():
#     return render_template("index.html")
#
#
# @app.route('/about')
# def about():
#     return render_template("about.html")
#
#
# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return "User page: " + name + "-" + str(id)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)