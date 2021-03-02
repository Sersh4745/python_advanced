class Book:
    def __init__(self, id, title, author, years):
        self.id = id
        self.title = title
        self.author = author
        self.years = years

    def __repr__(self):
        return f'{self.id}) {self.title}, {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def get_books_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                dataList = line.strip().split(',')
                self.add_book(Book(int(dataList[0]), dataList[1],
                                   dataList[2], int(dataList[3])))

    def add_book(self, obj_book):
        self.books.append(obj_book)

    def get_all_book(self):
        return self.books