import math


class Integer:
    ROMAN_DIGITS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }


    def __init__(self, value):
        self.value = value

    @classmethod
    def from_roman(cls, value):
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in cls.ROMAN_DIGITS:
                num += cls.ROMAN_DIGITS[value[i:i + 2]]
                i += 2
            else:
                num += cls.ROMAN_DIGITS[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_float(cls, value):
        if not type(value) == float:
            return "value is not a float"
        return cls(math.floor(value))

    @classmethod
    def from_string(cls, value):
        if not type(value) == str:
            return "wrong type"
        return cls(int(value))

    def add(self, integer):
        if not type(integer) == Integer:
            return "number should be an Integer instance"
        return self.value + integer.value



import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")

    def test_add_success(self):
        first_integer = Integer(10)
        second_integer = Integer(12)
        result = first_integer.add(second_integer)
        self.assertEqual(result, 22)

    def test_add_error(self):
        first_integer = Integer(10)
        second_integer = 12
        result = first_integer.add(second_integer)
        self.assertEqual(result, "number should be an Integer instance")


if __name__ == "__main__":
    unittest.main()
