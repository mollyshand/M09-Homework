import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating':[]})
                                                                               
    def add_book(self, book_name, rating):
        """ 
        Adds a book to the list if it does not already exist
        """
        if book_name in self.book_list["book_name"].values:
            print(f"{book_name} is already in the book list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1
            
    def has_read(self, book_name):
        return book_name in self.book_list["book_name"].values
                                                                
    def num_books_read(self):
        return self.num_books
                                                                               
    def fav_books(self):
        return self.book_list[self.book_list["book_rating"] > 3]
                                                                               

                                                                               
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@milleniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Dune", 5)
    test_object.add_book("War of the Worlds", 4)
                                                                               
    print("\nBook list:")
    print(test_object.book_list)
                                                                               
    print("\nHas read 'Dune'?", test_object.has_read("Dune"))
    print("\nHas read 'The Hobbit'?", test_object.has_read("The Hobbit"))
                                                                               
    print("\nNumber of Books Read:", test_object.num_books_read())
                                                                               
    print("\nFavorite Books:")
    print(test_object.fav_books())
                                                                               