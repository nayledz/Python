from list.extended_list import IntegerList

import unittest
from unittest import TestCase


class ListTests(TestCase):

    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_non_integer_data(self):
        integer = IntegerList("asd", 5.06)
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_integer_data(self):
        integer = IntegerList(6, 'asd')
        self.assertEqual([6], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(6, 7, 8, 9, 'asd')
        self.assertEqual([6, 7, 8, 9], integer._IntegerList__data)
        result = integer.get_data()
        self.assertEqual([6, 7, 8, 9], result)

    def test_adds_incorrect_data_raises(self):
        integer = IntegerList(6)
        self.assertEqual([6], integer._IntegerList__data)

        with self.assertRaises(ValueError) as error:
            integer.add('6')
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_adds_correct_data(self):
        integer = IntegerList(6)
        self.assertEqual([6], integer._IntegerList__data)

        integer.add(9)
        self.assertEqual([6, 9], integer._IntegerList__data)

    def test_remove_el_removes_the_element(self):
        integer = IntegerList(6)
        integer.remove_index(0)

        self.assertEqual([], integer._IntegerList__data)

    def test_invalid_index_raises(self):
        integer = IntegerList(6)

        with self.assertRaises(IndexError) as error:
            integer.remove_index(1)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_if_returns_removed_element_by_index(self):
        integer = IntegerList(6)
        result = integer.remove_index(0)

        self.assertEqual(6, result)

    def test_get_with_invalid_index_raises(self):
        integer = IntegerList(6)

        with self.assertRaises(IndexError) as error:
            integer.get(2)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_returns_valid_index(self):
        integer = IntegerList(6)
        result = integer.get(0)
        self.assertEqual(6, result)

    def test_insert_valid_index(self):
        integer = IntegerList(6)
        integer.insert(0, 5)

        self.assertEqual([5, 6], integer._IntegerList__data)

    def test_insert_with_invalid_index(self):
        integer = IntegerList(6)

        with self.assertRaises(IndexError) as error:
            integer.insert(2, 6)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_with_invalid_element(self):
        integer = IntegerList(6)

        with self.assertRaises(ValueError) as error:
            integer.insert(0, 'asd')

        self.assertEqual("Element is not Integer", str(error.exception))

    def test_get_biggest_element(self):
        integer = IntegerList(6, 7, 10, 100)
        result = integer.get_biggest()

        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(6, 7, 10, 100)
        result = integer.get_index(7)

        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
