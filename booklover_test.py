import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        bl = BookLover("Test User", "test@test.com", "fiction")
        bl.add_book("Catch 22", 5)
        self.assertTrue(bl.has_read("Catch 22"))
        
    def test_2_add_book(self):
        bl = BookLover("Test User", "test@test.com", "fiction")
        bl.add_book("Catch 22", 5)
        bl.add_book("Catch 22", 4)
        self.assertTrue(bl.has_read("Catch 22"))
        
    def test_3_add_book(self):
        bl = BookLover("Test User", "test@test.com", "fiction")
        bl.add_book("Catch 22", 5)
        self.assertTrue(bl.has_read("Catch 22"))
        
    def test_4_add_book(self):
        bl = BookLover("Test User", "test@test.com", "fiction")
        bl.add_book("Catch 22", 5)
        self.assertFalse(bl.has_read("1984"))
        
    def test_5_add_book(self):
        bl = BookLover("Test User", "test@test.com", "fiction")
        bl.add_book("Catch 22", 5)
        bl.add_book("Moby Dick", 4)
        bl.add_book("All Quiet on the Western Front", 5)
        self.assertEqual(bl.num_books_read(), 3)
        
    def test_6_add_book(self):
        bl = BookLover("Test User", "test@test.com", "fiction")
        bl.add_book("Catch 22", 5)
        bl.add_book("Moby Dick", 4)
        bl.add_book("All Quiet on the Western Front", 5)
        bl.add_book("Catcher in the Rye", 2)
        
        favs = bl.fav_books()
        self.assertTrue(favs["book_rating"] > 3).all()
        
        
if __name__ == '__main__':
    unittest.main(verbosity = 3)
        
        
    
                        
                        
                        