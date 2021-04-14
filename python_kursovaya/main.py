from lib.library import Library
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from lib.book import Book
from lib.reader import Reader, check_password_hash
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Jjlnl343208hONo0nonlNlnfsiod'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

Library().init_from_files('lib/books_availible.txt', 'lib/reader_list.txt',)
lib = Library()

# id_current_user = 1


@login_manager.user_loader
def load_user(user_id):
    return lib.get_reader_id(user_id)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/books', methods=['GET'])
def api_get_all_books():
    return render_template('books.html', books=lib.print_all_books())


@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def api_add():
    if request.method == "POST":
        id_book = request.form.get('id')
        title_book = request.form.get('title')
        author_book = request.form.get('author')
        year_book = request.form.get('year')

        if not (title_book and author_book and year_book and id_book):
            return render_template('add_book.html', message='Введены некорректные данные')

        if not year_book.isnumeric():
            return render_template('add_book.html', message='Введен некорректный год издания')
        if not id_book.isnumeric():
            return render_template('add_book.html', message='Введен некорректный id')

        ret_msg = lib.add_book(Book(int(id_book), title_book, author_book, int(year_book)))
        return render_template('add_book.html', message=ret_msg)

    return render_template('add_book.html')


@app.route('/delete', methods=['GET', 'POST'])
@login_required
def api_delete():
    if request.method == "POST":
        id_books = [int(i) for i in request.form.keys() if i.isnumeric()]
        if len(id_books):
            message = lib.remove_book(id_books)
            return render_template('delete_book.html',
                                   books=lib.print_list_books_available(),
                                   message=message)

    return render_template('delete_book.html', books=lib.print_list_books_available())


@app.route('/return', methods=['GET', 'POST'])
@login_required
def api_return():

    if request.method == "POST":
        id_books = [int(i) for i in request.form.keys() if i.isnumeric()]
        if len(id_books):
            message = lib.return_book(id_books, current_user.get_id())
            return render_template('return.html',
                                   books=lib.print_list_books_user(current_user.get_id()),
                                   message=message)

    return render_template('return.html',
                           books=lib.print_list_books_user(current_user.get_id()))


@app.route('/take', methods=['GET', 'POST'])
@login_required
def api_take():
    if request.method == "POST":
        id_books = [int(i) for i in request.form.keys() if i.isnumeric()]
        if len(id_books):
            _, message = None, lib.give_book(id_books, current_user.get_id())
            return render_template('take_book.html',
                                   books=lib.print_list_books_available(),
                                   message=message)

    return render_template('take_book.html',
                           books=lib.print_list_books_available())


@app.route('/books_availible', methods=['GET', 'POST'])
def api_availible():
    return render_template('books.html', books=lib.print_list_books_available())


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('psw')
        name = request.form.get('name')
        surname = request.form.get('surname')
        year = request.form.get('year')

        if not (email and psw and name and surname and year):
            return render_template('register.html', message='Введены некорректные данные')
        if not year.isnumeric():
            return render_template('register.html', message='Введены некорректный год')
        if lib.get_reader_email(email) is not None:
            return render_template('register.html', message='Пользователь с таким email уже зарегестрирован')

        code = lib.add_reader(Reader(name, surname, int(year), email, psw))

        if code:
            flash('Now you can login')
            return redirect(url_for('login'))
        else:
            return render_template('register.html', message='Error user')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    message = ''
    if request.method == "POST":
        email = request.form.get('email')
        psw = request.form.get('psw')
        next_url = request.args.get('next')

        if email and psw:
            reader = lib.get_reader_email(email)
            print(email, psw)
            print(reader)
            if reader and reader.check_psw(psw):
                print(reader.check_psw(psw))
                login_user(reader)
                if next_url:
                    return
                return redirect(url_for('home'))
            else:
                message = 'Invalid username or password'

    return render_template('login.html', message=message)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
