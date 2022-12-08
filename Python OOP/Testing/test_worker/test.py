from test_worker.worker import Worker

import unittest
from unittest import TestCase


class WorkerTest(TestCase):
    NAME = 'NAME'
    SALARY = 1024
    ENERGY = 2

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__if_is_initialized_with_the_correct_props(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test__worker_energy_is_being_incremented_after_rest_method(self):
        self.worker.rest()

        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test__if_worker_tries_to_work_with_energy_0(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as error:
            worker.work()
        self.assertEqual('Not enough energy.', str(error.exception))

    def test__if_money_is_increased_by_his_salary(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test__if_energy_is_decreased_after_the_work_method_is_called(self):
        self.worker.work()

        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__if_returns_proper_string_with_correct_values(self):
        actual_result = self.worker.get_info()
        expected_result = f'{self.NAME} has saved {0} money.'

        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()




