from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel_consumption = 1.25
    fuel = 50
    capacity = 50
    horse_power = 200

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_check_instance_attr_are_set(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_needed_fuel_to_drive(self):
        expected_needed_fuel = 6.25
        actual_needed_fuel = self.vehicle.fuel_consumption * 5
        self.assertEqual(expected_needed_fuel, actual_needed_fuel)

    def test_drive__when_enough_fuel__expected_to_reduced_fuel(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_drive__when_not_enough_fuel__expected_do_not_change_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(49)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_method(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)
        self.vehicle.refuel(1)
        self.assertEqual(44.75, self.vehicle.fuel)

    def test_refuel__when_not_enough_capacity(self):
        with self. assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str_representation(self):
        self.assertEqual('The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption', str(self.vehicle))


if __name__ == '__main__':
    main()
