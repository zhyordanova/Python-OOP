from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware('Test hardware', 'Heavy', 100, 10)

    def test_init__expect_to_set_attributes_correct(self):
        self.assertEqual('Test hardware', self.hardware.name)
        self.assertEqual('Heavy', self.hardware.hard_type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(10, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install__when_enough_memory_and_capacity__expect_to_add_it_to_the_list(self):
        software = LightSoftware('Test software', 5, 2)
        self.hardware.install(software)

        self.assertEqual(1, len(self.hardware.software_components))
        self.assertListEqual([software], self.hardware.software_components)

    def test_install__when_not_enough_memory_and_capacity__expect_exception(self):
        software = ExpressSoftware('Test ex software', 350, 500)

        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)

        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall__when_software_exist__expect_to_remove_it_from_the_list(self):
        software = LightSoftware('Test software', 5, 2)
        self.hardware.install(software)

        self.assertEqual(1, len(self.hardware.software_components))

        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))

    def test_uninstall__when_software_not_exist__expect_to_remove_it_from_the_list(self):
        software_l = LightSoftware('Test software', 5, 2)
        self.hardware.install(software_l)
        self.assertEqual(1, len(self.hardware.software_components))

        software_ex = ExpressSoftware('Test ex software', 350, 500)
        self.hardware.uninstall(software_ex)
        self.assertEqual(1, len(self.hardware.software_components))


if __name__ == '__main__':
    main()
