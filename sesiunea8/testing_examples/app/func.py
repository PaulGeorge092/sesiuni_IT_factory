"""
1. Implementeaza o functie care ia ca si parametru un numar
intreg.
Daca numarul este divizibil cu 3 returneaza 'Fizz'.
Daca numarul este divizibil cu 5 returneaza 'Buzz'.
Daca numarul este divizibil atat cu 3 cat si cu 5 returneaza 'FizzBuzz'.

2. Testeaza functia implementata folosind libraria unittest.
"""


def is_div_3_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
