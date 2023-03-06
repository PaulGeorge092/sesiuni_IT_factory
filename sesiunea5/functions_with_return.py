def say_hi():
    return "heloo"  # oreste executia functiei
    print("salut")


a = say_hi()
print(a)


def print_first_50():
    for i in range(50):
        print(i)
    # return None
    # return


# functia are valoare de adevar implicit None sau se poate explica eplicit
# cu cele 2 variante de mai sus (ele suntechivalente)

b = print_first_50()
print(b)


def iterare():
    for i in range(5):
        return


print(iterare())


def doar_daca():
    if False:
        return 2
    print("nu e fals")


print(doar_daca())
