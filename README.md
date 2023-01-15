# Python-Sorting-UI

T073 Data Analyzer(c) can be reached at:
E-mail: firaselezzi1@gmail.com

**Description/General Usage Notes:**
==================================
- Provides a user with an interface and selection of commands, to load a datafile, 
which can have a book added to it, removed from it, books gotten from it by factors of title, 
rate, author, publisher or category, find all the categories for a given book by title, and 
sort books either by, title, rate, publisher or author.

- T073\_Data\_Analyzer(c) contains 4 necessary files of:
	T073\_P1\_load\_data.py
	T073\_P2\_add\_remove\_search\_dataset.py
	T073\_P3\_sorting\_fun.py
	T073\_P4\_booksUI.py

- Be aware that the add/remove function creates a temporary dictionary rather than genuinely 
editing the intial csv datafile.

- Please verify the correct files are present before contacting support.

**Installation:**
===============
Python 3.10.1 or later is required for proper use.
No further modules must be loaded everything is included in this project package.

**Usage:**
========
> python T073_P4_booksUI.py

The program will run and prompt the user to enter a single character depending on which action
they wish to take to analyze or edit a given dataset.

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

This user interface is provided and the commands are self explanatory.

*Disclaimer if choosing to add a book and for the rating a string is entered it will result
in an error.

**Credits:**
==========
Firas El-Ezzi
Author of:
- T073\_P4\_UI\_case1.py
- book\_category\_dictionary
- sort\_books\_author
- add\_book
- remove\_book
- test\_get\_books\_by\_category
- test\_get\_books\_by\_rate

- T073\_P4\_UI\_case4.py
- sort\_books\_ascending\_rate
- get\_books\_by\_category
- get\_books\_by\_rate
- checking\_get\_books\_by\_title
- checking\_get\_books\_by\_author

- T073\_P4\_UI\_case2.py
- sort\_books\_title
- get\_books\_by\_title
- get\_books\_by\_author
- test\_get\_books\_by\_publisher
- test\_get\_all\_categories\_for\_book\_title

- T073\_P4\_UI\_case3.py
- sort\_books\_publisher
- get\_books\_by\_publisher
- get\_all\_categories\_for\_book\_title
- test\_add\_book
- test\_remove\_book

**License:**
==========
MIT License
Copyright (c) [2022] [T073\_Data\_Analyzer]
