
class Books():
    def __init__(self, book_id, book_name, book_author, book_year):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
    x = input('Enter: ')
    with open('hw.2/books_availible.txt', 'r') as f:
        file = f.readlines()
        for i in file:
            i = i.rstrip().split('$!$')
            if ''.join(i[0:1]) == x:
                book_name = ''.join(i[1:2])
                book_author = ''.join(i[2:3])
                book_year = ''.join(i[3:4])
                
           