# EX1 În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.


# variabila -> container din memoria RAM pt a stoca valori

# EX2 Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabile:
# string
# int
# float
# boolean

name = "George"  # str
age = 30  # int
temperature = 30.4  # float
white_colour = False  # bool

# EX3 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat
print(type(name))
print(type(age))
print(type(temperature))
print(type(white_colour))

# EX4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# Verifică tipul acesteia.

print(round(temperature))
temperature = round(temperature)
print(type(temperature))

# EX5 Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print("Hello ", name, "how are you")
print("Am varsta de", age, "ani")
print("Temperatura trebuie sa fie de", temperature, "grade celsius")
print("Culoarea masinii este:", white_colour)

# EX6 Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

nume = input("Adauga numele:")
prenume = input("Adauga prenumele:")
print(f"numele complet are: {len(nume + prenume)}", "caractere")

# EX7 Citește de la tastatură:
# -lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

lungimea = int(input("adauga  lungimea"))
latimea = int(input("adauga latimea"))
x = lungimea * latimea
print("Aria triunghiului este:", x)

# EX8 Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# afișează de câte ori apare cuvântul 'the'

string = "Coral is either the  stupidest animal or the smartest rock"
print(f"{string.count('the')}")

# EX9 acelasi string:inlocuieste the cu THE peste tot
print(string.replace('the', 'THE'))

# EX10 Același string: Folosește un assert ca să verifici dacă acest string conține doar numere.

assert string.isdigit
