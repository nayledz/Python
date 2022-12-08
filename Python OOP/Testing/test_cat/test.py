from test_cat.cat import Cat


import unittest
from unittest import TestCase


class CatTests(TestCase):
    NAME = 'CAT'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test__if_cat_size_is_increased_after_eating(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test__if_cat_is_fed_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test__if_cat_cannot_eat_if_already_fed(self):
        self.cat.eat()

        with self.assertRaises(Exception) as error:
            self.cat.eat()
        self.assertEqual('Already fed.', str(error.exception))

    def test__cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as error:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(error.exception))

    def test__cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
