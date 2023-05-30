# # Verifică dacă x are minim 4 cifre (x e int).
# # (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# n = int(input("add n:"))
# print(f"{n}  are {len(str(abs(n)))} cifre")
#
# if len(str(abs(n))) < 4:
#     print(f"{n} nu are minim 4 cifre")
# else:
#     print(f"{n} are minim 4 cifre")
#
# # 2.Verifică dacă x are exact 6 cifre.
#
# if len(str(abs(n))) == 6:
#     print(f"{n} are exact 6 cifre")
# else:
#     print(f"{n} nu are exact 6 cifre")
#
# # Verifică dacă x este număr par sau impar (x e int)
#
# if n % 2 == 0:
#     print(f"{n} este un numar par")
# else:
#     print(f"{n} este impar")
#
# # a, b, c (int)
# # Afișează care este cel mai mare dintre ele?
#
# a, b, c = list(map(int, input("add val:").split()))
#
# if a > b and a > c:
#     print("a este mai mare")
# elif b > c and b > a:
#     print("b este mai mare")
# else:
#     print("c este mai mare")
#
# # X, y, z - reprezintă unghiurile unui triunghi
#
# # Verifică și afișează dacă triunghiul este valid sau nu
#
# x, y, z = list(map(int, input('unghiuri: ').split()))
#
# if x + y + z == 180 and x and y and z != 0:
#     print("True")
# else:
#     print("False")
#
# # Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# #  Citește de la tastatură un int x
# #  Afișează stringul fără ultimele x caractere
#
# my_str = "Coral is either the stupidest animal or the smartest rock"
# x = int(input("add x:"))
# print(my_str[:-x])

# Același string. Declară un string nou care să fie format
# din primele 5 caractere + ultimele 5

# my_str2 = (my_str[:5]) + (my_str[-5:])
# print(my_str2)

# Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot
# stringul până la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest'

# index = my_str.index("rock")
# print(my_str[0:index])

# Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# ● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.


import random
import time

dice_roll = int(input("alege numar:"))
print("dice roll...")
time.sleep(3)
roll = random.randint(1, 6)
if dice_roll > roll:
    print(f"Ai pierdut. Ai ales un nr mai mare. Ai ales {dice_roll} dar a fost {roll}")
elif dice_roll < roll:
    print(f"Ai pierdut. Ai ales un nr mai mic. Ai ales {dice_roll} dar a fost {roll}")
else:
    print("Felicitari ai ghicit")
