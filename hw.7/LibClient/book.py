class Book:
    def __init__(self, book_id: int, book_name: str,
                 book_author: str, book_year: int):

        self.id = book_id
        self.title = book_name
        self.author = book_author
        self.year = book_year

        self.id_reader = None

    def __repr__(self):
        return f'{self.id}, {self.title}, {self.year}'