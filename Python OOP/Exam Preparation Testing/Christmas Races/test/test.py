import unittest

from project.team import Team


class TestTeam(unittest.TestCase):

    def setUp(self) -> None:
        self.team = Team("LEVSKI")

    def test_init(self):
        self.assertEqual("LEVSKI", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_getters_and_setters(self):
        team = Team('BARCELONA')
        self.assertEqual('BARCELONA', team.name)

    def test_if_name_is_not_valid(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "LEVSKI123"
        self.assertTrue("Team Name can contain only letters!", str(error.exception))

    def
