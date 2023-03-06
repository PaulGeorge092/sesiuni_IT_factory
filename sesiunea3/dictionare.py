# dict sunt folosite pentru a stoca date in perechi de forma
# key:valoare

# create

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1990,
}

car2 = dict(brand="ford", model="mustang", year=1990)

# accesing elements

print(car["brand"])

print(car.get("is_new"))
print(car.get("is_new", True))

# add element

car["is_new"] = False
v = car.setdefault("is_new", True)
print(car)
print(v)
car.setdefault("price", 7900)
print(car)

# replace element

car["price"] = 9600
car.update({"price": 10000, "colour": "black"})
print(car)

# remove element

car.pop("is_new")
print(car)
car.popitem()  # elimina ultimul element inserat
del car["year"]

a = {1: "first", 2: "second"}
a.clear(a)
print(a)

# all keys

print(car.keys())
print(list(car.keys))

# all values

print(list(car.values()))

# all items

print(list(car.items()))

# length

print(len(car))  # nr de chei
