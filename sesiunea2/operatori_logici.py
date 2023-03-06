x = True
y = False

print("x and y is", x and y)
print(" x or y", x or y)
print("not x is", not x) #inversam valoarea de adevar

x = 0 or 4 #or va evalua fiecare operand si se opreste la primul care este adevarat
print(x)
y = 7 or 9
print(y)

z = 7 and 0
print(z)
z = 7 and 5 #merge pana la capat si returneaza
print(z)