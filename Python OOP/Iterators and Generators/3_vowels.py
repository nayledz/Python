class vowels:
    vowel_chars = 'aeiouy'
    
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            if self.string[self.index].lower() not in self.vowel_chars:
                self.index += 1
                continue

            value_to_return = self.string[self.index]
            self.index += 1
            return value_to_return
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
