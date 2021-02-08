import unittest
from combo_breaker import ComboBreaker


class ComboBreakerTests(unittest.TestCase):

    def test_example_from_platform_input(self):
        breaker = ComboBreaker()

        private_key = breaker.decrypt(7, 5764801, 17807724)

        self.assertEqual(private_key, 14897079)

    def test_given_by_platform_input(self):
        breaker = ComboBreaker()

        door_private_key = breaker.decrypt(7, 2069194, 16426071)
        card_private_key = breaker.decrypt(7, 16426071, 2069194)

        self.assertEqual(door_private_key, 11576351)
        self.assertEqual(door_private_key, card_private_key)

    @unittest.expectedFailure
    def test_should_fail_with_incorrect_pubkeys(self):
        breaker = ComboBreaker()

        private_key = breaker.decrypt(10, 0, 0)
        

if __name__ == '__main__':
    unittest.main()