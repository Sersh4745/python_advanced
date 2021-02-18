class Book:
    def __init__(self, book_id, book_name, book_author, book_year, id_reader=None):
        self.id = book_id
        self.title = book_name
        self.author = book_author
        self.year = book_year

        # сюда будем писать id юзера,
        # который взял книгу
        self.id_reader = None

    def __repr__(self):
        return f'{self.id}) {self.title}, {self.year}'
