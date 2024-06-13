from unittest import TestCase

from prime_factor import PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_prime_factor_of_1(self):
        self.assertEqual([], self.prime_factor.of(1))

    def test_prime_test_of_2(self):
        self.assertEqual([2], self.prime_factor.of(2))

