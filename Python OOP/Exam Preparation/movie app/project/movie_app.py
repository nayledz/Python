from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.__check_if_user_exists(username):
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if not self.__check_if_user_exists(username):
            raise Exception("This user does not exist!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)

        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.remove(movie)
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_name(username)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        movie.likes += 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_name(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)

    def __str__(self):
        result = ""
        if self.users_collection:
            result += "All users: "
            result += ', '.join([user.username for user in self.users_collection]) + '\n'
        else:
            result += "All users: No users." + '\n'
        if self.movies_collection:
            result += 'All movies: '
            result += ', '.join([movie.title for movie in self.movies_collection]) + '\n'
        else:
            result += "All movies: No movies."
        return result.strip()

    def __find_user_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False


