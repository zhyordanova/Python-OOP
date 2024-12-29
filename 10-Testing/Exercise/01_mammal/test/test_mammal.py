from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    name = 'Mammal name'
    type = 'mammal type'
    sound = 'mammal sound'

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_check_instance_attr_are_set(self):
        self.assertEqual('Mammal name', self.mammal.name)
        self.assertEqual('mammal type', self.mammal.type)
        self.assertEqual('mammal sound', self.mammal.sound)

    def test_make_sound__expect_correct_sound(self):
        self.assertEqual('Mammal name makes mammal sound', self.mammal.make_sound())

    def test_kingdom_initial(self):
        result = self.mammal._Mammal__kingdom
        expected_result = 'animals'
        self.assertEqual(result, expected_result)

    def test_get_kingdom__expected_correct_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())


    def test_get_info__expect_correct_value(self):
        expected_info = 'Mammal name is of type mammal type'
        actual_info = self.mammal.info()
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    main()
