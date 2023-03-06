# 1. sa se scrie un program care citeste un text de la tastatura
#si afiseaza o lista cu fiecare caracter in ordinea inversa a aparitiei in text

text = input( "add text")
text = text[::-1]
l = list(text)
print(l)

# fie seturile
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
#a. sa se afiseze toate elemm care apar in set 1 si nu apar in set 2
#b. --//-- care apar in ambele seturi
#c. --//-- care nu sunt comune

 #a
print(set1.difference(set2))
print(set1-set2)
 #b
print(set1.intersection(set2))
print(set1 & set2)
 #c
print(set1.symmetric_difference(set2))
print(set1 ^ set2)