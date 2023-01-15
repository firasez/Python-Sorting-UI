# Group Memebers: Firas El-Ezzi (101239531), Dean Georgopoulos (101230584), David Edwards (101230530), Shivam Patel (101243851)

# Import
from T073_P1_load_data import book_category_dictionary

# Constants:
TOTAL_TESTS = 3
FOUR_TESTS = 4
TOTAL_TEST = 2


# Function 1, Written by: Firas El-Ezzi (101239531) (Has been corrected for error)
def add_book(book_dic: dict, tuple: tuple) -> str:
    """
    The function returns the updated dictionary with the newly added book and prints a message stating, “The book has been added correctly” or “There was an error adding the book”.
    Note: The parameter for the function is that every index of the book information like category or rate must be filled in to add the book to the dictionary.
    >>>add_book(book_category_dictionary('google_books_dataset.csv'),("1","2","3","4","5",8.0,90))
    "The book has been added correctly."
    >>> add_book(book_category_dictionary('google_books_dataset.csv'),("","","","","2","k","2.0"))
    "There was an error adding the book. Book not found."
    >>>"Test if book added correctly:",add_book(book_category_dictionary('google_books_dataset.csv'),("madam","f","f","f","f",5.0,100))
    "The book has been added correctly."
    """
    if tuple == ("", "", "", "", "", "", ""):
        print("There was an error adding the book")
        return book_dic

    category = tuple[5]
    book_add = {'title': tuple[0], 'author': tuple[1], 'rating': tuple[2], 'publisher': tuple[3], 'pages': tuple[4],
                'language': tuple[6]}

    if category in book_dic:
        book_dic[category] += [book_add]
        print("The book has been added successfully")
        return book_dic

    else:
        book_dic.update({category: [book_add]})
        print("The book has been added successfully")
        return book_dic

    # Function 2, Written by: Firas El-Ezzi (101239531)


def remove_book(book_dict: dict, title: str, category: str) -> str:
    """
    The function returns the updated dictionary excluding the removed book and prints a message stating, “The book has been removed correctly” or “There was an error removing the book. Book not found.”
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'),"Bring Me Back", "Fiction")
    "The book has been removed correctly"
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'),"Kill Me Please", "Wish")
    "There was an error removing the book. Book not found"
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'),"Lionking", "Fiction")
    "There was an error removing the book. Book not found"
    """

    check = 0
    if category in book_dict:
        for i in book_dict[category]:
            if title in i["title"]:
                book_dict[category].remove(i)
                check = 1
    if check == 1:
        print("Removing book", title, "category", category)
        print("The book has been removed correctly")
        return book_dict
    else:
        print("Removing book", title, "category", category)
        print("There was an error removing the book. Book not found")
        return book_dict


# Function 3, Written by: Dean Georgopoulos (101230584)
def get_books_by_category(book_dict: dict, category: str) -> int:
    """
    Returns the number of books in the selected category, from the case 1 "T073_P1_load_data" module.
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"), "Legal")
    1
    book 1 : The Guardians: The explosive new thriller from international bestseller John Grisham by John Grisham
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"), "Fiction")
    39
    """
    book_lst = []
    total = 0
    for book in book_dict[category]:
        book_lst += [(book["title"] + " by " + book["author"])]
    print(book_lst)
    book_lst = list(tuple(book_lst))
    total = len(book_lst)
    print("The category", category, "has", total, "books. This is the list of books:")
    book_counter = 1
    for book in book_lst:
        print("book", str(book_counter), ":", book)
        book_counter += 1
    return total


# Function 4, Written by: Dean Georgopoulos (101230584)
def get_books_by_rate(book_dict: dict, rate: int) -> int:
    """
    Will return al books and information of the book that has a rate greater to or equal to and less then one unit higher than the inputted rate.
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 2)
    0
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 3)
    8
    """
    total_books = 0
    rate_lst = []
    for category in book_dict:
        for book in book_dict[category]:
            if book["rating"] != "N/A":
                if book["rating"] >= rate and book["rating"] < (rate + 1):
                    rate_lst += [book["title"] + " by " + book["author"]]
    rate_lst = list(dict.fromkeys(rate_lst))
    print("There are", total_books, "books whose rate is between", str(rate), "and", str(rate + 1),
          "books. This is the list of books:")
    book_counter = 0
    for num in rate_lst:
        total_books += 1
        book_counter += 1
        print("book", str(book_counter), ":", num)
    return total_books


# Function 5, Written by: David Edwards (101230530)
def get_books_by_title(book_dict: dict, title: str) -> int:
    """
    Returns the number of books with the matching title, from the case 1 "T073_P1_load_data" module.
    >>>get_books_by_title(T073_P1_load_data.book_category_dictionary("google_books_dataset.csv"), "Deadpool Kills the Marvel Universe")
    1
    >>>get_books_by_title(T073_P1_load_data.book_category_dictionary("google_books_dataset.csv"), "To Kill A Mocking Bird")
    0
    >>>get_books_by_title(T073_P1_load_data.book_category_dictionary("google_books_dataset.csv"), "How To Win Friends and Influence People")
    1
    """
    book_lst = []
    total = 0
    for category in book_dict:
        for book in book_dict[category]:
            if title == book["title"]:
                if book not in book_lst:
                    book_lst.append(book)
                    total += 1
                print("The book,", title, "has been found")
    if total > 1:
        book_lst = tuple(book_lst)
    if total < 1:
        print("The book,", title, "has NOT been found")
    return total


# Function 6, Written by: David Edwards (101230530)
def get_books_by_author(book_dict: dict, author: str) -> int:
    """
    Returns the number of books with the matching author, from the case 1 "T073_P1_load_data" module.
    >>>get_books_by_author(T073_P1_load_data.book_category_dictionary("google_books_dataset.csv"), "George R.R. Martin")
    2
    >>>get_books_by_author(T073_P1_load_data.book_category_dictionary("google_books_dataset.csv"), "Barbara Allan")
    4
    >>>get_books_by_author(T073_P1_load_data.book_category_dictionary("google_books_dataset.csv"), "Stravos Papadopoulos")
    0
    """
    book_lst = []
    total = 0
    finalbook_lst = []
    for category in book_dict:
        for book in book_dict[category]:
            if author == book["author"]:
                book_lst.append(book)

                [finalbook_lst.append(x) for x in book_lst if x not in finalbook_lst]
    total = len(finalbook_lst)
    print("The author", author, "has published the following books:")
    for i in range(len(finalbook_lst)):
        print("Book", i + 1, ":", finalbook_lst[i]["title"], "rate:", finalbook_lst[i]["rating"])
    return total


# Function 7, Written by Shivam Patel (101243851)
def get_books_by_publisher(book_dict: dict, publisher: str) -> int:
    """
    Returns the number of books published by the publisher, from the case 1 "T073_P1_load_data" module.
    >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Penguin UK")
    1
    >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"HarperCollins UK")
    12
    >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Kensington Publishing Corp.")
    2
    >>>get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Marvel Entertainment")
    6
    """
    book_lst = []
    total = 0
    finalbook_lst = []

    for category in book_dict:
        for book in book_dict[category]:
            if publisher == book["publisher"]:
                book_lst.append(book)
                [finalbook_lst.append(x) for x in book_lst if x not in finalbook_lst]
    total = len(finalbook_lst)
    print("The publisher", publisher, "has published the following books:")
    for i in range(len(finalbook_lst)):
        print("book", i + 1, ":", finalbook_lst[i]["title"], "by", finalbook_lst[i]["author"])

    return total


# Function 8, Written by: Shivam Patel(101243851)
def get_all_categories_for_book_title(book_dict: dict, title: str) -> int:
    """
    Returns the number of books based on the title, from the case 1 "T073_P1_load_data" module.
    >>>get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Final Option: The best one yet")
    4
    >>>get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Total Control")
    4
    >>>get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"No One Is Too Small to Make a Difference")
    1
    >>>get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"The Magic of Thinking Big")
    2
    """
    category_lst = []
    total = 0

    for category in book_dict:
        for book in book_dict[category]:
            if title == book["title"]:
                category_lst.append(category)
                total += 1
    print("The book title", title, "belongs to the following categories:")
    for i in range(len(category_lst)):
        print("category", i + 1, ":", category_lst[i])

    return total