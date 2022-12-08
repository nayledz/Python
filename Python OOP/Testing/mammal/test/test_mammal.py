from unittest import TestCase

from project.mammal import Mammal


class TestMammal(TestCase):
    MAMMAL_NAME = 'name'
    MAMMAL_TYPE = 'type'
    MAMMAL_SOUND = 'sound'
    KINGDOM = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.MAMMAL_NAME, self.MAMMAL_TYPE, self.MAMMAL_SOUND)

    def test_mammal_init_should_create_proper_obj(self):
        self.assertEqual(self.MAMMAL_NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.MAMMAL_SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.MAMMAL_NAME} makes {self.MAMMAL_SOUND}"

        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):
        actual_result = self.mammal.get_kingdom()
        expected_result = self.KINGDOM
        self.assertEqual(expected_result, actual_result)

    def test_info(self):
        actual_result = self.mammal.info()
        expected_result = f"{self.MAMMAL_NAME} is of type {self.MAMMAL_TYPE}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()