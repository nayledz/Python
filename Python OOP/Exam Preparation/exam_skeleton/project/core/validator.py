class Validator:

    @staticmethod
    def check_if_empty_string_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_if_is_less_than_or_equal_to_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def check_if_number_is_not_in_range(value, min_number, max_number, message):
        if value < min_number or value > max_number:
            raise ValueError(message)