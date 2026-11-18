import uuid

class Book:

    #Default constructor
    def __init__():
        self.title = ''
        self.author = ''
        self.genre = ''
        self.ID = str(uuid.uuid4())
        self.__state = 'NOT IN INVENTORY'
        self.__borrower = ''
    
    #Creating a book
    def __init__(self, title, author, genre, ID, state, borrower):
        self.title = title
        self.author = author
        self.genre = genre
        self.ID = str(uuid.uuid4())
        self.__state = state
        self.__borrower = borrower

    def check_in(self, borrower):
        self.__state = 'CHECKED IN'
        self.__borrower = borrower

    def check_out(self, borrower):
        self.__state = 'CHECKED OUT'
        self.__borrower = borrower

    def get_state(self, __state, ID):
        return self.__state
