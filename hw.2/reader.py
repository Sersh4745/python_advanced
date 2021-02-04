
class Reader_books:
      def take_book(self):
            self.book=input("Введите код книги (пример 001): ")
            return self.book

      def returnBook(self):
            book_id = input("Введите код книги (пример 001): ")
            book_name = input("Введите название книги: ")
            book_author = input("Введите автора книги: ")
            book_year = input("Введите год издания книги: ")

            self.book = (f'{book_id}$!${book_name}$!${book_author}$!${book_year}\n')
            return self.book