
# Import function.
from T073_P1_load_data import *
from T073_P3_sorting_fun import *
from T073_P2_add_remove_search_dataset import *

# Global Variables
datafile = []
library = []
loop = True
loop2 = True


# User Interface For All Cases
def UI() -> None:
    """
    Provides a user with an interface and selection of commands, to load a datafile, which can have a book added to it, removed from it, books gotten from it by title, rate, author, publisher or category, find all the categories for a given book by title, and sort books either by, title, rate, publisher or author.
    Function returns None.
    >>>UI()
    The available commands are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
         T)itle R)ate A)uthor P)ublisher C)ategory
    5- GCT) Get all Categories for book Title
    6- S)ort books
         T)itle R)ate P)ublisher A)uthor
    7- Q)uit
    Please type your command:
    """
    global library
    global loop
    global loop2

    while loop == True:
        print(
            "The available commands are:" "\n1- L)oad data" "\n2- A)dd book" "\n3- R)emove book" "\n4- G)et books" "\n     T)itle R)ate A)uthor P)ublisher C)ategory" "\n5- GCT) Get all Categories for book Title" "\n6- S)ort books" "\n     T)itle R)ate P)ublisher A)uthor" "\n7- Q)uit")
        command = input("Please type your command: ")
        print()
        command = command.upper()

        if command == "L":
            library = []
            load()

        elif command == "G" and library != []:
            get()

        elif command == "S" and library != []:
            sort()

        elif command == "A" and library != []:
            add()

        elif command == "R" and library != []:
            remove()

        elif command == "GCT" and library != []:
            GCT()

        elif command == "A" or command == "R" or command == "G" or command == "GCT" or command == "S" and library == []:
            print("No file loaded\n")

        elif command == "Q":
            loop = False

        else:
            print("No such command\n")


def load() -> None:
    """
    Loads a file into the library variable and saves it, so that the user can run the other commands and obtain the information they wish from the file they loaded. Note that the library can be updated by the user through the "L" command.
    Function returns None.
    """
    global library

    while library == []:
        try:
            datafile = input("Enter the Name of the File you Wish to Load: ")
            library = book_category_dictionary(datafile)
            print("\nFile Successfully Loaded\n")
        except:
            print("\n Error, file does not exist in library.\n")


def get() -> None:
    """
    Provides the user with a means to get the categories for a single book, by inputing the title of their desired book.
    Function returns None.
    """
    global library
    global loop
    global loop2

    loop2 = True
    while loop2 == True:
        subinput1 = input("How would you like to get the number of Books? ")
        subinput1 = subinput1.upper()

        if subinput1 == "P":
            publisher = input("\nPlease type publisher name: ")
            print(get_books_by_publisher(library, publisher))
            print()
            loop2 = False

        elif subinput1 == "C":
            category = input(str("\nPlease type which category: "))
            print(get_books_by_category(library, category))
            print()
            loop2 = False

        elif subinput1 == "A":
            author = input(str("\nPlease type name of author: "))
            print(get_books_by_author(library, author))
            print()
            loop2 = False

        elif subinput1 == "R":
            rate = input("\nPlease type the rating: ")
            print(get_books_by_rate(library, int(rate)))
            print()
            loop2 = False

        elif subinput1 == "T":
            title = input(str("\nPlease type which title: "))
            print(get_books_by_title(library, title))
            print()
            loop2 = False

        elif subinput1 == "Q":
            loop = False
            loop2 = False

        else:
            print("\nNo such subcommand\n")


def sort() -> None:
    """
    Gives the user the ability to sort however, they wish, with four subcommands of title, author, publisher and rate.
    Function returns None.
    """
    global library
    global loop
    global loop2

    loop2 = True
    while loop2 == True:
        sub2_input = input("How do you want to sort? ")
        sub2_input = sub2_input.upper()
        print()

        if sub2_input == "T":
            print(sort_books_title(library))
            print()
            loop2 = False

        elif sub2_input == "R":
            print(sort_books_ascending_rate(library))
            print()
            loop2 = False

        elif sub2_input == "P":
            print(sort_books_publisher(library))
            print()
            loop2 = False

        elif sub2_input == "A":
            print(sort_books_author(library))
            print()
            loop2 = False

        elif sub2_input == "Q":
            loop = False
            loop2 = False

        else:
            print("No such subcommand\n")


def add() -> None:
    """
    Inputs the given book information by the user into the add book function.
    Function returns None.
    """
    global library

    sub2_input = input("title: ")
    sub21_input = input("author: ")
    sub22_input = float(input("rating: "))
    sub23_input = input("publisher: ")
    sub24_input = int(input("pages: "))
    sub25_input = input("category: ")
    sub26_input = input("language: ")

    library = add_book(library,
                       (sub2_input, sub21_input, sub22_input, sub23_input, sub24_input, sub25_input, sub26_input))
    print("\n", library, "\n")


def remove() -> None:
    """
    Will call the remove book function by inputted the commanded parameters from the user into the call.
    Function returns None.
    """
    global library

    sub3_input = input("Enter a category: ")
    sub2_input = input("\nEnter book title to remove: ")
    print()

    function_return = remove_book(library, sub2_input, sub3_input)
    library = function_return
    print("\n", function_return, "\n")


def GCT() -> None:
    """
    Will call the get all categories for book title function, which will print out all the categories for a title and the total number of the categories.
    Function returns None.
    """
    global library

    booktitle = input("Please type book title: ")
    print()
    print(get_all_categories_for_book_title(library, booktitle))
    print()


# Main Script
UI()
