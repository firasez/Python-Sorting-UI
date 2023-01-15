
#Imports
from T073_P1_load_data import book_category_dictionary

#Function 1, sort_books_title written by David Edwards (101230530)
def sort_books_title(dictionary: dict) -> list:
    """
    Returns the list of dictionaries where the category key will have a list and
    the final list is sorted in alphabetical order sorted by title.
    >>>sort_books_title(book_category_dictionary("test_1_dataset.csv"))
    [{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 416}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Mystery', 'Detective'], 'pages': 288}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'category': ['Fiction'], 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 400}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}]
    >>>sort_books_title(book_category_dictionary("test_2_dataset.csv"))
    [{'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 368}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'category': ['Psychology'], 'pages': 320}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'category': ['Business'], 'pages': 176}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': 224}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'category': ['Detective'], 'pages': 320}]
    >>>sort_books_title(book_category_dictionary("test_3_dataset.csv"))
    [{'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 224}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': 288}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'category': ['Detective'], 'pages': 288}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'category': ['Fiction'], 'pages': 208}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Adventure'], 'pages': 400}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'category': ['Thrillers'], 'pages': 208}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'category': ['Fiction'], 'pages': 624}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 144}]
    """
    lst = []
    for idx in dictionary:
        for book in dictionary[idx]:
            lst2 = []
            for idx2 in dictionary:
                for book2 in dictionary[idx2]:
                    if book["title"] == book2["title"]:
                        lst2.append(idx2)
            lst.append({'title':book['title'],'author':book['author'],'language':book['language'],'rating':book['rating'],'publisher':book['publisher'],'category': lst2,'pages':book['pages']})
    n=len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]["title"]>lst[j]["title"]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
            if lst[i]["author"]==lst[j]["author"] and lst[i]["title"]>lst[j]["title"]:
                temp2=lst[i]
                lst[i]=lst[j]
                lst[j]=temp2
    i = 0
    while i < len(lst) - 1:
            j = i + 1
            if lst[i] == lst[j]:
                lst.remove(lst[i])
            else:
                i += 1
    return lst


def sort_books_publisher(dictionary: dict) -> list:
    """
    Returns the list of dictionaries where the category key will have a list and
    the final list is sorted in alphabetical order of the name of the publisher and incase of  the
    same publisher, it will sort based on the title in alphabetical order.
    >>>sort_books_publisher(book_category_dictionary("test_1_dataset.csv")
    [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 400}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fiction'], 'pages': 416}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fiction'], 'pages': 544}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Mystery', 'Detective'], 'pages': 288}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'category': ['Fiction'], 'pages': 226}])
    >>>sort_books_publisher(book_category_dictionary("test_2_dataset.csv")
    [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': 224}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 368}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'category': ['Business'], 'pages': 176}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'category': ['Detective', 'Psychology'], 'pages': 320}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'category': ['Detective', 'Psychology'], 'pages': 320}]
    >>>sort_books_publisher(book_category_dictionary("test_3_dataset.csv")
    [{'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'category': ['Fiction'], 'pages': 208}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': 288}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Adventure'], 'pages': 400}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Thrillers'], 'pages': 224}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Thrillers'], 'pages': 208}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'category': ['Detective'], 'pages': 288}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 144}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'category': ['Fiction'], 'pages': 624}]
    """
    lst = []
    for category1 in dictionary:
        for book1 in dictionary[category1]:
            lst2 = []
            for category2 in dictionary:
                for book2 in dictionary[category2]:
                    if book1["publisher"] == book2["publisher"]:
                        lst2.append(category2)
            lst.append({'title': book1['title'], 'author': book1['author'], 'language': book1['language'],
                        'rating': book1['rating'], 'publisher': book1['publisher'], 'category': lst2,
                        'pages': book1['pages']})
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(lst[j]['publisher']) > str(lst[j + 1]['publisher']):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if str(lst[j]['publisher']) == str(lst[j + 1]['publisher']) and lst[j]['title'] > lst[j + 1]['title']:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    finalsortedlst = []
    n = len(finalsortedlst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if finalsortedlst[j]['title'] > finalsortedlst[j + 1]['title']:
                finalsortedlst[j]['title'], finalsortedlst[j + 1]['title'] = finalsortedlst[j + 1]['title'], finalsortedlst[j]['title']
    finalsortedlst.extend(lst)
    i = 0
    while i < len(finalsortedlst) - 1:
        j = i + 1
        if finalsortedlst[i] == finalsortedlst[j]:
            finalsortedlst.remove(finalsortedlst[i])
        else:
            i += 1
    return finalsortedlst


def sort_books_author(dictionary: dict) -> list:
    """
    Returns the list of dictionaries where the category key will have a list and
    the final list is sorted in alphabetical order of the name of the author and incase of  the
    same author, it will be based on the title in alphabetical order.
    >>>sort_books_author(book_category_dictionary("test_1_dataset.csv")
    [{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 416}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 400}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Mystery', 'Detective'], 'pages': 288}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'category': ['Fiction'], 'pages': 226}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}]
    >>>sort_books_author(book_category_dictionary("test_2_dataset.csv")
    [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'category': ['Detective'], 'pages': 320}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 368}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'category': ['Business'], 'pages': 176}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'category': ['Psychology'], 'pages': 320}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': 224}]
    >>>sort_books_author(book_category_dictionary("test_3_dataset.csv")
    [{'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 224}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'category': ['Thrillers'], 'pages': 208}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Adventure'], 'pages': 400}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 144}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': 288}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'category': ['Fiction'], 'pages': 624}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'category': ['Fiction'], 'pages': 208}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'category': ['Detective'], 'pages': 288}]
    """
    lst = []
    for category1 in dictionary:
        for book1 in dictionary[category1]:
            lst2 = []
            for category2 in dictionary:
                for book2 in dictionary[category2]:
                    if book1["title"] == book2["title"]:
                        lst2.append(category2)
            lst.append({'title': book1['title'], 'author': book1['author'], 'language': book1['language'],
                        'rating': book1['rating'], 'publisher': book1['publisher'], 'category': lst2,
                        'pages': book1['pages']})
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(lst[j]['author']) > str(lst[j + 1]['author']):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if str(lst[j]['author']) == str(lst[j + 1]['author']) and lst[j]['title'] > lst[j + 1]['title']:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    finalsortedlst = []
    n = len(finalsortedlst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if finalsortedlst[j]['title'] > finalsortedlst[j + 1]['title']:
                finalsortedlst[j]['title'], finalsortedlst[j + 1]['title'] = finalsortedlst[j + 1]['title'], finalsortedlst[j]['title']
    finalsortedlst.extend(lst)
    i = 0
    while i < len(finalsortedlst) - 1:
        j = i + 1
        if finalsortedlst[i] == finalsortedlst[j]:
            finalsortedlst.remove(finalsortedlst[i])
        else:
            i += 1
    return finalsortedlst


def sort_books_ascending_rate(dictionary: dict) -> list:
    """
    Sorts the inputted dictionary by making the category key of a book the list of all its categories, and then by rate in ascending order to return a list empty of dublicated books that is organized by ascending rate. Note that "N/A" is considered the lowest and that in teh case that two rates are the same, the two books of same rate will be sorted title in alphabetical order.
    >>>sort_books_ascending_rate(book_category_dictionary("test_1_dataset.csv")
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Mystery', 'Detective'], 'pages': 288}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 416}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'category': ['Fiction'], 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 400}]
    >>>sort_books_ascending_rate(book_category_dictionary("test_2_dataset.csv")
    [{'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'category': ['Business'], 'pages': 176}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 368}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'category': ['Detective'], 'pages': 320}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'category': ['Psychology'], 'pages': 320}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': 224}]
    >>>sort_books_ascending_rate(book_category_dictionary("test_3_dataset.csv")
    [{'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'category': ['Fiction'], 'pages': 208}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'category': ['Detective'], 'pages': 288}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'category': ['Fiction'], 'pages': 624}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 144}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': 288}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'category': ['Thrillers'], 'pages': 208}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 224}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Adventure'], 'pages': 400}]
    >>>sort_books_ascending_rate(book_category_dictionary("test_4_dataset.csv")
    [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics'], 'pages': 112}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'category': ['Business'], 'pages': 176}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 368}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'category': ['Detective'], 'pages': 320}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'category': ['Psychology'], 'pages': 320}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 672}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': 224}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 96}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'category': ['Fiction'], 'pages': 400}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 40}]
    """
    lst = []
    for category1 in dictionary:
        for book1 in dictionary[category1]:
            lst2 = []
            for category2 in dictionary:
                for book2 in dictionary[category2]:
                    if book1["title"] == book2["title"]:
                        lst2.append(category2)
            lst.append({'title':book1['title'],'author':book1['author'],'language':book1['language'],'rating':book1['rating'],'publisher':book1['publisher'],'category': lst2,'pages':book1['pages']})
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if str(lst[j]['rating']) > str(lst[j+1]['rating']):
                lst[j],lst[j+1] = lst[j+1],lst[j]
            if str(lst[j]['rating']) == str(lst[j+1]['rating']) and lst[j]['title'] > lst[j+1]['title']:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    finalsortedlst = []
    for i in lst[:]:
        if i['rating'] == 'N/A':
            finalsortedlst.append(i)
            lst.remove(i)
    n = len(finalsortedlst)
    for i in range(n):
        for j in range(0, n-i-1):
            if finalsortedlst[j]['title'] > finalsortedlst[j+1]['title']:
                finalsortedlst[j]['title'], finalsortedlst[j+1]['title'] = finalsortedlst[j+1]['title'], finalsortedlst[j]['title']
    finalsortedlst.extend(lst)
    i = 0
    while i < len(finalsortedlst) - 1:
        j = i + 1
        if finalsortedlst[i] == finalsortedlst[j]:
            finalsortedlst.remove(finalsortedlst[i])
        else:
            i += 1
    return finalsortedlst
