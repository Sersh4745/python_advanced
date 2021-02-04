from os import name
import sys
import book
import copy
class Library:
      def __init__(self,list_books,list_books_all,absence_list):
            self.availabl_books = list_books
            self.list_all = list_books_all
            self.abcence_list = absence_list

      def displayAvailablebooks(self):
            """Ф-ция показывает книги в 
            наличии на данный момент"""
            print("================================")
            print("Книги в наличии:")
            print("================================")
            for book in self.availabl_books:
                  book = book.rstrip().split('$!$')
                  print(' '.join(book))

      def display_abcence_books(self):
            """Ф-ция показывает книги которые на руках у читателя"""
            print("================================")
            print("Книги Не в наличии или удалены:")
            print("================================")
            for book in self.abcence_list:
                  book = book.rstrip().split('$!$')
                  print(' '.join(book))

      def display_all_books(self):
            """Ф-ция показывает общий список книг"""
            print("================================")
            print("Общий список книг")
            print("================================")
            for book in self.list_all:
                  book = book.rstrip().split('$!$')
                  print(' '.join(book))

      def return_book(self,take_book):
            """Ф-ция возврата книг в список книг 
            которые в наличии"""
            print("Для возврата книги")
            for i in self.abcence_list:
                  book = i.rstrip().split('$!$')
                  if ''.join(book[0:1]) == take_book: #  Находим соответствие нашему id
                        print("Поздравляем, вы вернули эту книгу")
                        self.abcence_list.remove(i)
                        self.availabl_books.append(i)

      def lendBook(self,take_book):
            """Ф-ция позволяет взять книгу"""
            for i in self.availabl_books:
                  book = i.rstrip().split('$!$')
                  if ''.join(book[0:1]) == take_book: #  Находим соответствие нашему id
                        print("Поздравляем, вы взяли эту книгу")
                        self.availabl_books.remove(i)
                        self.abcence_list.append(i)
      
      def del_book(self,take_book):
            """Ф-ция позволяет удалить книгу книгу"""
            for i in self.availabl_books:
                  book = i.rstrip().split('$!$')
                  if ''.join(book[0:1]) == take_book: #  Находим соответствие нашему id
                        print("Поздравляем, вы удалили эту книгу")
                        self.availabl_books.remove(i) #  удаляем со списока "в наличии"
                        self.list_all.remove(i) #  удаляем со списока "общий"

      def addBook(self,returnedBook):
            """Ф-ция позволяет добавить книгу книгу"""
            self.availabl_books.append(returnedBook) #  добавляем в список "в наличии"
            self.list_all.append(returnedBook)  #  добавляем в список "общий"
            print("Книжка добавлена") 