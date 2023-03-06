# 1 sa se scrie un program care citeste de la tastatura numere pana cand se introduce nr 0.
# Pentru fiecare nr introdus se verifica daca este par, iar la final se vor afisa intr-o lista toate nr pare

numar = -1
numere_pare = []
while numar:
    numar = int(input("Introdu un nr: "))
    if numar % 2 == 0:
        numere_pare.append(numar)
print(numere_pare)

#2 sa se scrie un program care citeste un text de la tastatura si va afisa un dictionar cu toate caracterele
# din text in care cheile vor fi caracterele si valorile, daca caracterul cheie este vocala sau consoana
dct = {}
txt = input("Introdu textul:" )
for char in txt :
    if not char.isalpha() :
        continue
    char_type = "vocala" if char in "aeiou" else "consoana"
    dct[char] = char_type
print(dct)


#3 sa se scrie un program care citeste de la tastatura 6 numere si apoi le afiseaza pe cele mai mari decat 9
numbers = []
for _ in range(6) :
    x = int(input("introdu un nr "))
    if x > 9 :
        numbers.append(x)
print(numbers)

# 4 sa se scrie un prg care citeste de la tastatura litere pana se introduce un carcater care nu-i litera
# la final va afisa toate literele unice si sortate
litere = set()
while True:
    caracter = input("introdu un caracter: ")
    if not caracter.isalpha():
        break
    litere.add(caracter)
lst_litere = list(litere)
lst_litere.sort()
print(lst_litere)