class NormalPasswordError(Exception):
    def __str__(self):
        return 'The Password is not valid'


class EmailValidationError(Exception):
    def __str__(self):
        return 'The email is not valid'


# class PriceValidationError(Exception):
#     def __str__(self):
#         return 'The price is not valid'


class NameValidationError(Exception):
    def __str__(self):
        return 'The Name is not valid'


class PhoneValidationError(Exception):
    def __str__(self):
        return 'The Phone is not valid'


class CharacterValidationError(Exception):
    def __str__(self):
        return 'The Character is not valid'


class DateValidationError(Exception):
    def __str__(self):
        return 'The date is not valid'


class StateValidationError(Exception):
    def __str__(self):
        return 'The state of order is not valid'


class OrderTypeValidationError(Exception):
    def __str__(self):
        return 'The order type is not valid'


class IntegerValidationError(Exception):
    def __str__(self):
        return 'The number type is not a valid integer'


class FloatValidationError(Exception):
    def __str__(self):
        return 'The number type is not a valid float'


class JSONValidationError(Exception):
    def __str__(self):
        return 'The input string is not a valid JSON'


class BoolValidationError(Exception):
    def __str__(self):
        return 'The input is not boolean'
