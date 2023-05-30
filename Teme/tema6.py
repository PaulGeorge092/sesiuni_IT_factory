# 1.Clasa Cerc
# Atribute: rază, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

from math import pi


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f"{self.raza} {self.culoare}")

    def aria(self):
        return pi * self.raza ** 2

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return pi * (self.raza * 2)


c = Cerc(30, "negru")
c.descriere_cerc()
c.aria()
c.diametru()
c.circumferinta()


# 2. Clasa Dreptunghi
# Atribute: lungime, lățime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare
# . Poți verifica schimbarea culorii prin apelarea metodei descrie()

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return f" Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}"

    def schimba_culoarea(self, alta_culoare):
        self.culoare = alta_culoare

    def aria(self,):
        return self.lungime * self.latime

    def perimetru(self,):
        return (2 * self.lungime) + (2 * self.latime)

d = Dreptunghi(40, 20, "albastru")
d.descriere()
d.schimba_culoarea("rosu")
d.aria()
d.perimetru()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} are un salariu de {self.salariu}")

    def nume_complet(self):
        return self.nume and self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu *= (1 + procent / 100)
        return self.salariu

a = Angajat("Paul", "George", 7000)
a.descrie()
a.nume_complet()
a.salariu_lunar()
a.salariu_lunar()
a.marire_salariu(20)

# clasa cont bancar
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# # ● creditare_cont(suma)

class Cont:
    def __init__(self, iban, titular, sold, ):
        self.iban = iban
        self.titular = titular
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular} are in contul {self.iban} suma de {self.sold}")

    def debitare_cont(self, suma):
        if suma > self.sold:
            raise ValueError("fonduri insuficiente")
        elif suma < self.sold:
            self.sold -= suma
        return self.sold

    def creditare_cont(self, suma):
        self.sold += suma
        return self.sold

c = Cont(123456, "Paul George", 8700)
c.afisare_sold()
c.debitare_cont(3000)
c.creditare_cont(2500)

# optionale
# clasa factura

from datetime import date
class Factura:
    seria = 12345
    data = date.today()

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def __repr__(self):
        return f"{self.numar} | {self.nume_produs} | {self.cantitate} | {self.pret_buc}"

    def schimba_cantitatea(self, schimba_cantitate):
        self.cantitate = schimba_cantitate
        return self.cantitate

    def schimba_pret(self, schimba_pret):
        self.pret_buc = schimba_pret
        return self.pret_buc

    def schimba_nume(self, schimba_nume):
        self.nume_produs = schimba_nume
        return self.nume_produs

    def genereaza_factura(self):
        print(f"Factura seria {self.seria} numar {self.numar}")
        print(f"Data:{self.data}")
        print("-" * 50)
        print("Produs | Cantitate | Pret Bucata | Total")
        print("-" * 50)
        total = self.cantitate * self.pret_buc
        print(f"{self.nume_produs} |    {self.cantitate}    |       {self.pret_buc}  |    {total}")


fac = Factura(23, "Telefon", 7, 700)
fac.genereaza_factura()


# clasa masina


class Masina:
    marca = "Ford"
    model = ["Mustang", "Mondeo", "Focus"]
    viteza_actuala = 0
    viteza_maxima = 300
    culoare = "Gri"
    culori_disponibile = ("Rosu", "Verde", "Galben", "Negru", "Albastru", "Alb")
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Viteza actuala: {self.viteza_actuala}")
        print(f"Viteza maxima: {self.viteza_maxima}")
        print(f"Culoare disponibila: {self.culoare}")
        print(f"Inmatriculata: {self.inmatriculata}")

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopsire(self, culoare):
        if culoare not in self.culori_disponibile:
            raise FileNotFoundError(f"Culoarea nu exista in {self.culori_disponibile}")
        return True

    def accelerate(self, viteza):
        if viteza < 0:
            raise ValueError
        if viteza >= self.viteza_maxima:
            return self.viteza_maxima

    def franare(self):
        return self.viteza_actuala

m = Masina
m.descrie("Mustang")
m.inmatriculare()
m.vopsire("Rosu")
m.accelerate(200)
m.franare()

