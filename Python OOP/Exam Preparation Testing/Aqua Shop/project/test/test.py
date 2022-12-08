import unittest

from project.movie import Movie


class TestMovie(unittest.TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Stranger Things", 2022, 10.00)

    def test_init(self):
        self.assertEqual("Stranger Things", self.movie.name)
        self.assertEqual(2022, self.movie.year)
        self.assertEqual(10.00, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_getters_and_setters(self):
        movie = Movie("Peaky Blinders", 2019, 10.00)
        self.assertEqual("Peaky Blinders", movie.name)
        self.assertEqual(2019, movie.year)

    def test_if_name_is_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ""
        self.assertTrue("Name cannot be an empty string!" in str(error.exception))

    def test_if_year_is_not_valid(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1886
        self.assertTrue("Year is not valid!" in str(error.exception))

    def test_if_actor_is_in_the_list(self):
        self.movie.actors = ['actor1', 'actor2', 'actor3']
        result = self.movie.add_actor('actor1')
        self.assertEqual("actor1 is already added in the list of actors!", result)

    def test_if_actor_is_not_in_list(self):
        self.movie.actors = ['actor1', 'actor2', 'actor3']
        self.movie.add_actor('actor4')
        self.assertEqual(['actor1', 'actor2', 'actor3', 'actor4'], self.movie.actors)

    def test_gt_method(self):
        first_movie = Movie("Stranger Things", 2022, 10.00)
        second_movie = Movie("Peaky Blinders", 2019, 5.00)
        actual_result = str(first_movie > second_movie)
        self.assertEqual('"Stranger Things" is better than "Peaky Blinders"', actual_result)
        third_movie = Movie("Titanic", 1997, 11)
        second_result = str(first_movie > third_movie)
        self.assertEqual('"Titanic" is better than "Stranger Things"', second_result)

    def test_repr_method(self):
        self.movie.actors = ['actor1', 'actor2', 'actor3']
        actual_result = repr(self.movie)
        expected_result = "Name: Stranger Things" + \
                          '\n' + 'Year of Release: 2022' + \
                          '\n' + 'Rating: 10.00' + '\n' + \
                          'Cast: actor1, actor2, actor3'
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()