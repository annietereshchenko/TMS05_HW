# Разработайте поиск книги в библиотеке по ее автору(часть имени)/цене/заголовку/описанию.
import xml.etree.ElementTree as ET


class Book:

    def __init__(self):
        self.id = None
        self.author = None
        self.title = None
        self.genre = None
        self.price = None
        self.publish_date = None
        self.description = None

    def __str__(self):
        return f'Author: {self.author},\n' \
               f'Title: {self.title},\n' \
               f'Genre: {self.genre},\n' \
               f'Price: {self.price},\n' \
               f'Publish date: {self.publish_date}\n'\
               f'Description: {self.description}\n'


def search(xml_str, author=None, title=None, price=None, description=None):
    root = ET.fromstring(xml_str)
    book_list = []
    for child in root:
        book = Book()

        for appt in list(child):
            if appt.tag and appt.tag == 'author':
                book.author = appt.text
            if appt.tag and appt.tag == 'title':
                book.title = appt.text
            if appt.tag and appt.tag == 'genre':
                book.genre = appt.text
            if appt.tag and appt.tag == 'price':
                book.price = appt.text
            if appt.tag and appt.tag == 'publish_date':
                book.publish_date = appt.text
            if appt.tag and appt.tag == 'description':
                book.description = appt.text
        book_list.append(book)

    list_of_filtered_books = filter(lambda book: author and author in book.author
                               or title and title in book.title
                               or book.price == price
                               or description and description in book.description, book_list)

    for book in list_of_filtered_books:
        print(book)


if __name__ == "__main__":
    with open('library.xml') as f:
        xml_string = f.read()

    search(xml_string, author='Gambardella')
    search(xml_string, title='Python')
    search(xml_string, price='36.75')
    search(xml_string, description='Computers and Code')
