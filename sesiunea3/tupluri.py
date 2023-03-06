# create
fruits = ("apple", "banana", "cherry", "cherry")  # permite duplicat

# count

print(20 * "-", "count", 20 * "-")

print(fruits.count("cherry"))

# indexing

print(fruits[0])

# sliceing
print(fruits[:3])
print(fruits[1:3])
print(fruits[-1])

# adding elements

print(20 * "-", "adding elements", 20 * "-")
fruits += ("pear",)
print(fruits)
# sau
y = list(fruits)
y.append("orange")
fruits = tuple(y)

# remove element

print(20 * "-", "remove elem", 20 * "-")

y = list(fruits)
y.remove("apple")
fruits = tuple(y)
print(fruits)
