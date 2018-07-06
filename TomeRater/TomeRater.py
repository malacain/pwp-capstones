class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def change_email(self, address):
        self.email = address
        print("Your email address has been updated!")

    def __repr__(self):
        print(self.books)
        return "User {user}, email: {email}".format(user = self.name, email = self.email)

    def __eq__(self, other_user):
        if self.name == other_user.name:
            if self.email == other_user.email:
                return True
            else:
                return False
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for i in self.books.values():
            total = total + i
        return total / len(self.books.values())


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, newisbn):
        if self.isbn != newisbn:
            self.isbn = newisbn
            print("The ISBN has been changed.")
        else:
            print("Same ISBN, no change.")

    def add_rating(self, rating):
        rating = rating
        if rating == None:
            pass
        elif rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        total = 0
        try:
            for i in self.ratings:
                total = total + i
            return total / len(self.ratings)
        except:
            print("Can't divide by zero")

    def __repr__(self):
        return "{title}".format(title = self.title)



class Fiction(Book):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        super().__init__(title, isbn)

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        self.title = title
        self.isbn = isbn
        super().__init__(self.title, self.isbn)
        self.subject = subject
        self.level = level

    def get_level(self):
        return self.level

    def get_subject(self):
        return self.subject

    def __repr__(self):
        return "{title}, an {level} book on {subject}.".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}  #key = email, value = User object
        self.books = {}  #key = Book object, value = # of users

    def create_book(self, title, isbn):
        tempbook = Book(title, isbn)
        return tempbook

    def create_novel(self, title, author, isbn):
        tempbook = Fiction(title, author, isbn)
        return tempbook

    def create_non_fiction(self, title, subject, level, isbn):
        tempbook = Non_Fiction(title, subject, level, isbn)
        return tempbook


    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():    #if the email address is a key in the dictionary
            nameobj = self.users[email] #set the variable nameobj equal to the value for that key (A user object)
            book.add_rating(rating)
            nameobj.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("This user does not exist")


    def add_user(self, name, email, user_books=None):
        myuser = User(name, email)
        self.users[email] = myuser
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for i in self.books:
            print(i)

    def print_users(self):
        for i in self.users:
            print(i)

    def get_most_read_book(self):
        book = max(self.books.items(), key=lambda x: x[1])
        return book

    def most_positive_user(self):
        highest_rated = None
        value = 0
        lastval = 0
        uservalues = []
        for i in self.users.values():
            try:
                uservalues.append(i)
                lastval = value
                value = i.get_average_rating()
                if value > lastval:
                    highest_rated = i
            except:
                continue

        return highest_rated

    def highest_rated_book(self):
        highest_rated = None
        value = 0
        lastval = 0
        bookkeys = []
        for y in self.books.keys():
            bookkeys.append(y)
            lastval = value
            value = y.get_average_rating()
            if value > lastval:
                highest_rated = y

        return highest_rated

