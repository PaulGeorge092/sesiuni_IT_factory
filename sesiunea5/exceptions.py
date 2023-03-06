try:  #testeaza un bloc de cod pentru exceptii
    print(x)
except:  #trateaza diferite tipuri de erori
    print("a aparut o eroare")


try:
    print("1".Upper())
    print(1/0)
    print(x)
except (NameError, ZeroDivisionError):
    print("var nedefinita sau diviziune cu 0")
except AttributeError as ex:
    print(f"eroarea: {ex}")

try:
    print("hello")
except:
    print("eroare")
else:
    print("nicio eraore") # se executa doar daca nu apare nicio eroare


try:
    print(x)
except:
    print("eroare")
finally:  # se executa mereu indiferent de situatie
    print("se executa")

x = -1
if x<0:
    raise Exception("x < 0")




