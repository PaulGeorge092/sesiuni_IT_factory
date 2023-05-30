#testare unitest

from sesiunea8.testing_examples.app.func import is_div_3_5

import unittest


class TestFunc(unittest.TestCase):

    # def test_descriere_succinta_test(self):
    #     pass

    def test_is_div_3_5_35(self):
        self.assertEqual('FizzBuzz', is_div_3_5(15))

from sesiunea8.testing_examples.app.func import is_div_3_5

import unittest
from parameterized import parameterized


class TestFunc(unittest.TestCase):

    # def test_descriere_succinta_test(self):
    #     pass

    def test_is_div_3_5_35(self):
        self.assertEqual('FizzBuzz', is_div_3_5(15))

    def test_is_div_3_5_3(self):
        self.assertEqual('Fizz', is_div_3_5(9))

    def test_is_div_3_5_5(self):
        self.assertEqual('Buzz', is_div_3_5(20))

    def test_is_div_3_5_not_35(self):
        self.assertEqual(None, is_div_3_5(4))

    @parameterized.expand([
        ('FizzBuzz', 15),
        ('Fizz', 9),
        ('Buzz', 20),
        (None, 4)
    ])
    def test_is_div_3_5(self, expected, n):
        self.assertEqual(expected, is_div_3_5(n))



from sesiunea8.testing_examples.app.func import is_div_3_5
import pytest


def test_is_div_3_5_35():
    assert is_div_3_5(15) == 'FizzBuzz'


@pytest.mark.parametrize("n, expected", [
    (15, 'FizzBuzz'),
    (9, 'Fizz'),
    (20, 'Buzz'),
    (4, None)
])
def test_is_div_3_5(n, expected):
    assert is_div_3_5(n) == expected


"""
Implementeaza o functie care verifica daca un numar luat
ca si parametru este par. Daca e par returneaza True,
daca nu, returneaza False.

Fa o verificare pentru a te asigura ca parametrul dat este
un numar intreg. Daca nu e, arunca o exceptie custom.

Testeaza cazul in care se arunca eroarea,
folosind libraria unittest, respectiv pytest
"""

#definirea unei exceptii custom
class NotIntException(Exception):
    pass


def check_is_even(number):
    if not isinstance(number, int):
        raise NotIntException(f"{number} is not an int.")
    if number % 2 == 0:
        return True
    return False

def test_check_is_even_exception(self):
        self.assertRaises(NotIntException, check_is_even, 'trei')

        # sau
        with self.assertRaises(NotIntException) as exc:
            check_is_even('trei')
            self.assertEqual(str(exc.value), 'trei is not an int')

def test_check_is_even_exception():
    with pytest.raises(NotIntException) as exc:
        check_is_even('trei')
    assert str(exc.value) == 'trei is not an int.'
    assert exc.value.args[0] == 'trei is not an int.'


"""
O clasa numita Calculator in care
sa avem disponibile si implementate 2 metode:
add - 2 param: a, b -> returnam suma
substract - 2 param -> returnam diferenta
"""


class Calculator:

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

from sesiunea8.testing_examples.app.calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator_obj = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator_obj.add(2, 3), 5)

    def test_substract(self):
        self.assertEqual(self.calculator_obj.substract(3, 2), 1)

    def tearDown(self):
        # ultimul pas care are loc la rularea testelor
        # aici punem functionalitatea necesara
        # astfel incat sa facem curatenie in urma
        # testelor
        # ex: inchiderea conexiunii la baza de date
        pass