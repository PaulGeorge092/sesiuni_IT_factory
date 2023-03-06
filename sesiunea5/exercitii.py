"""
try: (Blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: <-- Prinderea tuturor exceptiilor de tipul NumeEroare
    se executa doar daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): <-- Gruparea mai multe tipuri de Exceptii
    se executa daca se prinde AltNumeEroare sau IncaUnNumeEroare
except Eroarea4 as ex: <-- Stocarea mesajului unei erori intr-o variabila (exemplul variabilei 'ex')
    se poate accesa mesajul de Eroarea4 prin variabila ex
except:
    se executa la orice alt tip de eroare nespecificat
else:
    se executa doar daca nu se arunca eroare in blocul try
finally:
    se executa indiferent daca se arunca eroare sau nu
"""

def get_all_param_values(*args, **kwargs):
    return list(args) +  list(kwargs.values())

print(get_all_param_values(1,2,4,a=6, b=5))

# sa se scrie o functie care rpimeste ca param 2 numere si return cel mai mare
def get_max(a,b):
    return a a > b else b
print(get_max(2,3))

#

