from unittest import TestCase, main

from extended_list import IntegerList


class IntegerListTests(TestCase):

    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, 4, 5)

    def test_add__element_not_integer__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add("asd")
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add__valid_element__expect_return_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], self.int_list.add(6))



    def test_remove_index__index_not_in_range__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(5)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_index__return_element__expect_removed_element(self):
        self.assertEqual(self.int_list.remove_index(0), 1)
        self.assertEqual([2, 3, 4, 5], self.int_list.get_data())

    def test__init__other_types_involved__expect_only_integers(self):
        self.int_list = IntegerList(1, 'two', 3, 'four', 5)
        self.assertEqual([1, 3, 5], self.int_list.get_data())

    def test_get__index_not_in_range_expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(5)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert__index_not_in_range__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(5, 6)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert__element_not_integer__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(0, 'zero')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert__element_valid__expect_change_in_list(self):
        self.int_list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.int_list.get_data())

    def test_get_biggest(self):
        self.assertEqual(self.int_list.get_biggest(), 5)

    def test_get_index(self):
        self.assertEqual(1, self.int_list.get_index(2))


if __name__ == '__main__':
    main()
