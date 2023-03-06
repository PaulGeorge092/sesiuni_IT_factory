'''
listele sunt utilizate pentru a stoca mai multe valori(colectie)
intr.o singura variabila
listele sunt modificabile, ordonate si permit valori duplicate.
sunt indexabile si indexul incepe de la 0
cand se adauga un element in lista, acesta se va adauga la final.
'''
# create

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
cars = list(("bmw", "audi", "tesla"))
print(type(numbers))
print(len(fruits))

# indexing
print(20 * "-", "indexing", 20 * "-")
print(numbers[0])
print(numbers[-1])
print(numbers[2:4])
print(numbers[::2])  # cate elemente sare la o parcurgere
print(numbers[1::2])
print(numbers[::-1])  # inversare index

# add element
print(20 * "-", "add element", 20 * "-")

numbers.append(10)
print(numbers)
numbers.insert(0, 10)
print(numbers)

# remove element
print(20 * "-", "remove element", 20 * "-")
elem = numbers.pop()  # eliminam valori in functie de indexul lor in lista
print(elem)
print(numbers)
elem2 = numbers.pop(0)  # elimina dupa index
print(elem2)
print(numbers)
numbers.remove(3)  # elimina prima aparitie a valorii date
print(numbers)
numbers.clear()
print(numbers)  # elimina toate elementele
numbers = [3, 4, 5, 6, 7, 1, 9, 3]

# replace element
print(20 * "-", "replace elemenet", 20 * "-")

print(fruits)
fruits[1] = "pear"
print(fruits)

# count

print(numbers.count(3))

# add 2 lists

numbers2 = [1, 3, 5, 7, 9]
numbers.extend(numbers2)  # modifica lista
print(numbers + numbers2)  # creaza o lista noua

# reverse

print(fruits[::-1])
print(fruits)
fruits.reverse()  # modifica lista initiala (in place)
print(fruits)

# sort

numbers.sort()  # #modifica lista initiala (in place)
print(numbers)
numbers.sort(reverse=True)
