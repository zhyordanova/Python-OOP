from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('Test name', 2)

    def test_init__expect_to_set_attributes_correctly(self):
        self.assertEqual('Test name', self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add__when_enough_space__expect_to_add_passenger_to_the_list(self):
        self.train.add('Passenger name')

        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual("Added passenger Passenger name", self.train.PASSENGER_ADD.format('Passenger name'))

    def test_add__when_not_enough_space__expect_exception(self):
        self.train.add('Passenger name')
        self.train.add('Passenger name2')

        with self.assertRaises(ValueError) as ex:
            self.train.add('Passenger name3')

        self.assertEqual("Train is full", str(ex.exception))

    def test_add__when_passenger_name_exist__expect_exception(self):
        self.train.add('Passenger name')
        self.assertListEqual(['Passenger name'], self.train.passengers)

        with self.assertRaises(ValueError) as ex:
            self.train.add('Passenger name')

        self.assertEqual("Passenger Passenger name Exists", str(ex.exception))

    def test_remove__when_passenger_exist__expect_to_remove_from_the_list(self):
        self.train.add('Passenger name')
        self.assertListEqual(['Passenger name'], self.train.passengers)

        self.train.remove('Passenger name')
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Removed Passenger name", self.train.PASSENGER_REMOVED.format('Passenger name'))

    def test_remove__when_passenger_not_exist__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove('Passenger name')

        self.assertEqual("Passenger Not Found", str(ex.exception))


if __name__ == '__main__':
    main()
