# 1. operatori de identitate

x1 = 5
y1 = 5
x2 = "hello"
y2 = "hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is y1)  # pt tipuri de de date primitive se va face egalitate la valoare
print(x2 is not y2)
print(x3 is y3)  # se va verifica locatia din memorie pt tipuri de date care nu-s primitive
print(x3 is x3)
print("#" * 50)

# 2 operatori de apartenenta

x = "hello"
y = [1, 2, 3]
print("h" in x)
print("llo" in x)
print(4 not in y)
print([2, 3] in y)

# 3 functii all si any
print("#" * 50)
print(all([1, 2, "a", "v",  None - 7]))  # verifica daca toate elementele pot fi evaluate la adevarat
print(any([0, None, ""[], 1])) #verifica daca cel putin un element poate fi evaluat la true
