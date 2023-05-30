# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
# else.

# if este un operator conditional care determina executarea unui bloc de cod,daca este fals conditionalul
# else urmeaza sa execute blocul de cod


# 2. Verifică și afișează dacă x este număr natural sau nu
x = int(input("add number:"))
if x >= 0:
    print("x este un numar natural")
else:
    print("x nu este un numar natural")

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

x = int(input("add number:"))
if x > 0:
    print("x este un numar pozitiv")
elif x < 0:
    print("x este un numar negativ")
else:
    print("x este numar neutru")

# 4. Verifică și afișează dacă x este între -2 și 13.

x = int(input("add number:"))
if x <= -2 and x <= 13:
    print("True")
else:
    print("False")

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

x = int(input("add num1"))
y = int(input("add num2"))
if (x - y) < 5:
    print("True")
else:
    print("False")

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

x = int(input("add number:"))
if not x <= 5 and x <= 27:
    print("True")
else:
    print("False")

# 7.  x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare

x = int(input("add x:"))
y = int(input("add y:"))
if x == y:
    print("sunt egale")
    pass
if x > y:
    print("x este mai mare")
else:
    print("y este mai mare")

# 8.  X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

x, y, z = list(map(int, input('adauga lungimea laturilor: ').split()))

if x == y != z or x == z != y or y == z != x:
    print("triunghiul este isoscel")
elif x == y == z:
    print("triunghiul este echilateral")
elif x != y and y != z and z != x:
    print("triunghiul este oarecare")

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.

l = input("adauga litera:")

if l in ["a", "e", "i", "o", "u"]:
    print(l, "este o vocala")
else:
    print(l, "nu este o vocala")

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = int(input("adauga nota:"))
if nota >= 9:
    print("A")
elif nota >= 8:
    print("B")
elif nota >= 7:
    print("C")
elif nota >= 6:
    print("D")
elif nota >= 4:
    print("E")
elif nota < 4:
    print("F")
