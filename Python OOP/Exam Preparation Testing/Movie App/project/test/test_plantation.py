import unittest

from project.plantation import Plantation


class PlantationTests(unittest.TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(20)

    def test_init(self):
        self.assertEqual(20, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_getters_and_setters(self):
        self.plantation.size = 30
        self.assertEqual(30, self.plantation.size)

    def test_if_value_is_negative(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1
        self.assertTrue("Size must be positive number!" in str(error.exception))

    def test_check_if_worker_in_workers(self):
        self.plantation.workers = ['Pesho', 'Ivan', 'Sasho']
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker('Pesho')
        self.assertTrue("Worker already hired!" in str(error.exception))

    def test_if_worker_hired(self):
        self.plantation.workers = ['Pesho', 'Ivan', 'Sasho']
        result = self.plantation.hire_worker('Toshko')

        self.assertEqual(['Pesho', 'Ivan', 'Sasho', 'Toshko'], self.plantation.workers)
        self.assertEqual(f"Toshko successfully hired.", result)

    def test_return_count_of_plants(self):
        self.plantation.plants = {'Pesho': ['plant1', 'plant2', 'plant3'], 'Sasho': ['plant4', 'plant5', 'plant6']}
        actual_result = len(self.plantation)
        expected_result = 6
        self.assertEqual(expected_result, actual_result)

    def test_if_worker_not_in_workers(self):
        self.plantation.workers = ['Pesho', 'Ivan', 'Sasho']
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Vlado", 'plant1')
        self.assertEqual("Worker with name Vlado is not hired!", str(error.exception))

    def test_if_plantation_is_full(self):
        plantation = Plantation(6)
        plantation.workers = ['Pesho', 'Ivan', 'Sasho']
        plantation.plants = {'Pesho': ['plant1', 'plant2', 'plant3'], 'Sasho': ['plant4', 'plant5', 'plant6']}
        len(plantation)
        with self.assertRaises(ValueError) as error:
            plantation.planting("Pesho", 'plant1')
        self.assertEqual("The plantation is full!", str(error.exception))

    def test_if_worker_planted(self):
        plantation = Plantation(7)
        plantation.workers = ['Pesho', 'Ivan', 'Sasho']
        plantation.plants = {'Pesho': ['plant1', 'plant2', 'plant3'], 'Sasho': ['plant4', 'plant5', 'plant6']}
        len(plantation)
        result = plantation.planting('Pesho', 'plant7')
        expected_result = {'Pesho': ['plant1', 'plant2', 'plant3', "plant7"], 'Sasho': ['plant4', 'plant5', 'plant6']}
        actual_result = plantation.plants
        self.assertEqual(expected_result, actual_result)
        self.assertEqual("Pesho planted plant7.", result)

    def test_if_worker_planted_but_not_in_workers(self):
        plantation = Plantation(8)
        plantation.workers = ['Pesho', 'Ivan', 'Sasho']
        plantation.plants = {'Pesho': ['plant1', 'plant2', 'plant3'], 'Sasho': ['plant4', 'plant5', 'plant6']}
        len(plantation)
        result = plantation.planting('Ivan', 'plant7')
        expected_result = {'Pesho': ['plant1', 'plant2', 'plant3'], 'Sasho': ['plant4', 'plant5', 'plant6'], 'Ivan': ['plant7']}
        actual_result = plantation.plants
        self.assertEqual(expected_result, actual_result)
        self.assertEqual("Ivan planted it's first plant7.", result)

    def test_str_method(self):
        plantation = Plantation(7)
        plantation.workers = ['Pesho', 'Sasho']
        plantation.plants = {'Pesho': ['plant1', 'plant2', 'plant3'], 'Sasho': ['plant4', 'plant5', 'plant6']}
        actual_result = str(plantation)
        expected_result = "Plantation size: 7" + \
                          '\n' + "Pesho, Sasho" + \
                          '\n' + 'Pesho planted: plant1, plant2, plant3' +\
                          '\n' + 'Sasho planted: plant4, plant5, plant6'
        self.assertEqual(expected_result, actual_result)

    def test_repr_method(self):
        plantation = Plantation(7)
        plantation.workers = ['Pesho', 'Sasho']
        actual_result =repr(plantation)
        expected_result = 'Size: 7' + '\n' + 'Workers: Pesho, Sasho'
        self.assertEqual(expected_result, actual_result)