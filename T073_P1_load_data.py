# Written by: Firas El-Ezzi (101239531)
# Reviewed by: Dean Georgopoulos (101230584)
# Reviewed by: David Edwards (101230530)
# Reviewed by: Shivam Patel (101243851)



def book_category_dictionary(filename: str) -> dict[str:list[dict[str:str]]]:
    """
    Returns a dictionary or a list with the category being the key.
    >>>book_publisher_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'pages': 240, 'category': 'Fiction', 'language': 'English'}
    """
    book_dictionary = {}
    books = open(filename, 'r')
    next(books)
    for row in books:
        book = {}
        book.update({"title" : row.split(",")[0]})
        book.update({"author" : row.split(",")[1]})
        if row.split(",")[2] == "N/A":
            book.update({"rating" : row.split(",")[2]})
        else:
            book.update({"rating" : float(row.split(",")[2])})
        book.update({"publisher" : row.split(",")[3]})
        book.update({"pages" : int(row.split(",")[4])})
        book.update({"language" : row.split(",")[6].rstrip("\n")})
        category = row.split(",")[5]
        if category in book_dictionary:
            book_dictionary[category].append(book)
        else:
            book_dictionary[category] = [book]
    return book_dictionary