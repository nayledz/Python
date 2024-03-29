class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n"
        result += "Liked movies:" + '\n'
        if self.movies_liked:
            for movie in self.movies_liked:
                result += movie.details() + '\n'
        else:
            result += "No movies liked." + '\n'
        result += "Owned movies:" + '\n'
        if self.movies_owned:
            for movie in self.movies_owned:
                result += movie.details() + '\n'
        else:
            result += "No movies owned."

        return result.strip()


