# 1. Lungime

name = "Dragos"
print(len(name))

# 2. Majuscule

name = "dragos"
print(name.upper())  # transforma toate literele mici in majuscule

# 3. Litere mici

name = "draGoS"
print(name.lower())  # transforma toate literele in litere mici

# 4. Numarare

name = "anamaria"
print(name.count("a"))  # nr de aparitii al caracterului in string
print(name.count("i"))
print(name.count("b"))

# 5. Replace

name = "anamaria"
name = name.replace("a", "b")  # toate aparitiile caracterului "a" au fost inlocuite cu "b"
print(name)

food = "pizza"
print(food.replace("zz", "t"))

name = "anamaria"
print(name.replace("a", "b", 2))

# 6. Indexing

name = "John"
print(name.index("o"))  # cauta primul caracter cautat
print(name[0])
print(name[-1]) # cauta ultimul caracter cautat
print(name[len(name) - 1])

# 7. Slicing

b = "Hello world"
print(b[2:5])  # de la 2 la 5 (fara 5)
print(b[:5]) # de la inceput pana la 5 (neinclusiv)
print(b[2:]) # de la caracterul al 2-lea pana la final
print(b[-5:-2]) # indexare nagativa