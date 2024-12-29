from unittest import TestCase

from hashtable.hashtable import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_attributes(self):
        self.assertEqual(4, len(self.hash_table.keys))
        self.assertEqual(4, len(self.hash_table.values))
        self.assertEqual(4, self.hash_table.max_capacity)

    def test_add_with_available_space(self):
        self.hash_table.add("test_key_1", "test_value_1")
        self.assertEqual(1, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.max_capacity)
        self.assertEqual("test_value_1", self.hash_table["test_key_1"])

    def test_add_with_no_available_space__expect_to_resize(self):
        for number in range(1, self.hash_table.max_capacity + 1):
            self.hash_table.add(f'test_key_{number}', f'test_value_{number}')

        self.assertEqual(4, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.max_capacity)

        # Here we overload the dict and it should resize
        self.hash_table.add(f'test_key_5', f'test_value_5')
        self.assertEqual(5, self.hash_table.actual_length)
        self.assertEqual(8, self.hash_table.max_capacity)
        self.assertIn('test_key_5', self.hash_table.keys)

    def test_value_is_replaced_when_key_exist(self):
        self.hash_table.add('test_key', 'test_value')
        self.assertEqual('test_value', self.hash_table['test_key'])
        self.hash_table['test_key'] = 'new_value'
        self.assertEqual('new_value', self.hash_table['test_key'])

    def test_get_with_existing_key(self):
        self.hash_table.add('test_key', 'test_value')
        self.assertEqual('test_value', self.hash_table.get('test_key'))

    def test_get_with_not_existing_key(self):
        self.hash_table.add("test_key", "test_value")
        self.assertIsNone(self.hash_table.get("not existing"))

    def test_get_with_not_existing_key_with_default_value(self):
        self.hash_table.add("test_key", "value")
        self.assertEqual("DEFAULT", self.hash_table.get("not existing", "DEFAULT"))

    def test_representation(self):
        self.hash_table.add("test_key", "test_value")
        self.assertEqual('{test_key: test_value}', str(self.hash_table))

    def test_collision_set_next_available_index(self):
        self.hash_table["name"] = "Peter"
        self.assertEqual(1, self.hash_table.keys.index("name"))
        # collision with index 1
        self.hash_table["age"] = 25
        self.assertEqual(2, self.hash_table.keys.index("age"))

    def test_collision_set_next_available_index_at_0(self):
        self.hash_table["name"] = "Peter"
        self.assertEqual(1, self.hash_table.keys.index("name"))
        # collision with index 1
        self.hash_table["age"] = 25
        self.assertEqual(2, self.hash_table.keys.index("age"))
        self.hash_table["work"] = "Some title"
        self.assertEqual(3, self.hash_table.keys.index("work"))

        # Go back to index 0 because no other available
        self.hash_table["eyes color"] = "blue"
        self.assertEqual(0, self.hash_table.keys.index("eyes color"))

