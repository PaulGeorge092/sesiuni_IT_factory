# 1. Sa se scrie un program care citeste date de la tastatura si afiseaza doar primele 3 caractere
# diferite de spatiu primite

a = input("Text: ")
a = a.replace(" ", "") #inlocuire text cu TEXT
print(a[:3])

# 2. Sa se scrie un program care citeste date de la tastatura si afiseaza urmatoarele:



b = input("Text: ")
print(f"a. {len(b)}")  #  nr de litere a textului introdus
print(f"b. {b[0]} {b[-1]}") #  prima si ultima litera
print(f"c. {b.upper()}")  # c) textul scris doar cu majuscule
print(f"d. {b.count(b[0])}")  # d) de cate ori apare prima litera
print(f"e. {b.count(' ') + 1}")  # e) cate cuv are textul