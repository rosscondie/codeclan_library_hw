from models.book import Book

book_1 = Book("Shoe Dog", "Phil Knight", "Biography", True, False)
book_2 = Book("Born to Run", "Christopher McDougall", "Memoir", False, True)
book_3 = Book("Green Lights", "Matthew McConaughey", "Philosophy/Poetry", True, False)
book_4 = Book("Fantastic Mr Fox", "Roald Dahl", "Kids", False, True)

books_list = [book_1, book_2, book_3, book_4]

def get_book_list():
    return books_list

def create_new_book(book):
    books_list.append(book)

def delete_book(index):
    books_list.pop(index)

def change_book_status(book):
    books_list.extend(book)
