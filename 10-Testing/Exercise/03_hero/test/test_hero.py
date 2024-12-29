from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.main_hero = Hero("Main hero", 5, 100, 10)
        self.enemy_hero = Hero("Enemy hero", 10, 80, 20)

    def test_check_instance_attr_are_set(self):
        self.assertEqual('Main hero', self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_battle__when_fight_yourself(self):
        hero_self = Hero("Main hero", 6, 80, 10)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(hero_self)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle__when_main_hero_health_less_than_0__expect_value_error(self):
        self.main_hero.health = -1
        # self.assertEqual(-1, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle__when_main_hero_health_equal_to_0__expect_value_error(self):
        self.main_hero.health = 0
        # self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle__when_enemy_hero_health_less_than_0__expect_value_error(self):
        self.enemy_hero.health = -1
        # self.assertEqual(-1, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You cannot fight Enemy hero. He needs to rest', str(ex.exception))

    def test_battle__when_enemy_hero_health_equal_to_0__expect_value_error(self):
        self.enemy_hero.health = 0
        # self.assertEqual(0, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You cannot fight Enemy hero. He needs to rest', str(ex.exception))

    def test_draw_case__when_main_health_is_less_than_0_and_enemy_health_equal_to_0__expect_draw(self):
        self.enemy_hero.health = 50
        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_draw_case__when_main_health_equal_to_0_and_enemy_health_less_than_0__expect_draw(self):
        self.main_hero.health = 200
        self.enemy_hero.health = 30
        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_draw_case__when_main_health_equal_to_0_and_enemy_health_equal_to_0__expect_draw(self):
        self.main_hero.health = 200
        self.enemy_hero.health = 50
        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_draw_case__when_main_health_less_than_0_and_enemy_health_less_than_0__expect_draw(self):
        self.enemy_hero.health = 30
        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_main_hero_win(self):
        self.main_hero.damage = 200
        self.main_hero.health = 300

        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You win', result)
        self.assertEqual(205, self.main_hero.damage)
        self.assertEqual(6, self.main_hero.level)
        self.assertEqual(105, self.main_hero.health)

    def test_main_hero_lose(self):
        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You lose', result)
        self.assertEqual(25, self.enemy_hero.damage)
        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(35, self.enemy_hero.health)

        self.assertTrue(self.main_hero.health < 0)

    def test_str_representation(self):
        self.assertEqual('Hero Main hero: 5 lvl\nHealth: 100\nDamage: 10\n', str(self.main_hero))


if __name__ == '__main__':
    main()
