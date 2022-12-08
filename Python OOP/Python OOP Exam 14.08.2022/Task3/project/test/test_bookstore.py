import unittest

from project.bookstore import Bookstore


class TestBookstore(unittest.TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(20)

    def test_init(self):
        self.assertEqual(20, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_getters_and_setters(self):
        self.bookstore = Bookstore(30)
        self.assertEqual(30, self.bookstore.books_limit)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_if_book_limit_is_negative(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore = Bookstore(-1)
        self.assertTrue(f"Books limit of -1 is not valid" in str(error.exception))

    def test_if_book_limit_is_zero(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore = Bookstore(0)
        self.assertTrue(f"Books limit of 0 is not valid" in str(error.exception))

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        actual_result = len(self.bookstore)
        expected_result = 12
        self.assertEqual(expected_result, actual_result)

    def test_if_book_limit_is_reached(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 10, "Book3": 4}
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("Book1", 2)
        self.assertTrue("Books limit is reached. Cannot receive more books!" in str(error.exception))

    def test_if_title_not_in_dict(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        self.bookstore.receive_book("Book4", 2)
        actual_result = self.bookstore.availability_in_store_by_book_titles
        expected_result = {"Book1": 5, "Book2": 3, "Book3": 4, "Book4": 2}
        self.assertEqual(expected_result, actual_result)

        self.bookstore.receive_book("Book3", 2)
        actual_result = self.bookstore.availability_in_store_by_book_titles
        expected_result = {"Book1": 5, "Book2": 3, "Book3": 6, "Book4": 2}
        self.assertEqual(expected_result, actual_result)

    def test_receive_method_return(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        actual_result = self.bookstore.receive_book("Book3", 2)
        expected_result = "6 copies of Book3 are available in the bookstore."
        self.assertEqual(expected_result, actual_result)

    def test_if_book_doesnt_exists(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book4", 2)
        self.assertTrue("Book Book4 doesn't exist!" in str(error.exception))

    def test_if_book_has_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book3", 6)
        self.assertTrue("Book3 has not enough copies to sell. Left: 4" in str(error.exception))

    def test_if_can_sell_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        actual_result = self.bookstore.sell_book("Book3", 4)
        expected_result = "Sold 4 copies of Book3"
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(4, self.bookstore.total_sold_books)

    def test_str_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 3, "Book3": 4}
        self.bookstore.sell_book("Book3", 1)
        self.bookstore.sell_book("Book2", 1)
        self.bookstore.sell_book("Book1", 3)
        len(self.bookstore)
        actual_result = str(self.bookstore)
        expected_result = "Total sold books: 5" + \
                          "\n" + 'Current availability: 7' + \
                          '\n' + " - Book1: 2 copies" + '\n' + \
                          " - Book2: 2 copies" + '\n' + " - Book3: 3 copies"
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()

