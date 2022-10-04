"""
Create a Library Class with below methods:
    1. Display all the books of the Library
    2. Add books to the dictionary by taking input from user
    3. Lend books to people: Capture which book is lend out to whom

"""


class Library:

    def __init__(self, lst, name):
        self.lst = lst
        self.name = name
        print(f"Welcome to {self.name} Book Library")

    def add_books(self):
        while True:
            books = input("Enter a book name or type Done when adding is completed")
            if books != "Done":
                self.lst.append(books)
                print(self.lst)
            elif books == "Done":
                print(f"All Books added to Library successfully: {self.lst}")
                break

    def display_book(self):
        print("Following books are present in Library:\n", self.lst)

    def lend_books(self):
        print("Following Books are available in Library")
        for i in range(0, len(self.lst), 1):
            dic = {self.lst[i]: i}
            print(dic)
        dic1 = {}

        while True:
            book_del = input("Enter which book you want to Lend. Type Done once all lending is done")
            if book_del == "Done":
                break
            else:
                owner = input("Whom you are lending the book")
                try:
                    self.lst.remove(book_del)
                    print("Now Library has the following books: ", self.lst)
                    dic1.update({book_del: owner})
                    dic2 = dic1.copy()
                except Exception as error:
                    print("Book Not available")

        print(f"Now the book owner is: {dic2}")


Bk = Library(["Sherlock Holmes", "Harry Potter", "As You Like It"], "Smart")


def main():
    while True:
        choice = input("Enter what you want to do: Add, Display or Lend or Close?")
        if choice == "Add":
            Bk.add_books()
        elif choice == "Display":
            Bk.display_book()
        elif choice == "Lend":
            Bk.lend_books()
        else:
            print("Library is closing!!")
            break


main()
