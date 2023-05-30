# Curs 1: Unit teste, TDD, Python Packages
## 📝 OBIECTIVE
1. Unit tests - teorie
2. Implementare unit teste folosind libraria unittest
3. Implementare unit teste folosin libraria pytest
4. TDD
5. Python Packages

## 📌 Unit tests - teorie
- Unit tests = Teste unitare
- In programare, testele unitare reprezinta testare de software
in care unitati individuale ale codului sursa sunt testate
  (functii, metode, clase).
- Ele tipic sunt teste automate scrise de software developers
pentru a asigura ca o anumita sectiune ale aplicatiei atinge
comportamentul dorit.
- O unitate de cod poate reprezenta un modul intreg, o clasa,
o functie, o metoda etc.
- Testarea unitara descopera probleme la inceputul ciclului de dezvoltare.
- Problemele aparute (daca apar) includ atat erori in implementarea
programatorului, cat si defecte sau parti lipsa ale specificatiei pentru
unitate.
- Testarea nu va detecta fiecare eroare din program, deoarece nu poate
evalua fiecare cale de executie nici in cele mai triviale implementari.
- In plus, testarea unitatilor prin definitie testeaza doar functionalitatea
unitatilor in sine.

- In Python, sunt 3 metode populare pentru dezvoltarea de teste unitare:
  - folosindu-ne de libraria unittest (https://docs.python.org/3/library/unittest.html)
  - folosindu-ne de libraria pytest (https://docs.pytest.org/en/6.2.x/contents.html)
  - folosindu-ne de doctest (https://docs.python.org/3/library/doctest.html), teste rulate pe
baza documentatiei scrise a functionalitatii

## 📌 Libraria unittest

```python
"""
1. Implementeaza o functie care ia ca si parametru un numar
intreg.
Daca numarul este divizibil cu 3 returneaza 'Fizz'.
Daca numarul este divizibil cu 5 returneaza 'Buzz'.
Daca numarul este divizibil atat cu 3 cat si cu 5 returneaza 'FizzBuzz'.

2. Testeaza functia implementata folosind libraria unittest.
"""
```


## 📌 Libraria pytest
```python
"""
Testeaza functia definita la sectiunea anterioara,
folosind libraria pytest
"""
```

## 📌 Testarea exceptiilor cu librariile unittest si pytest
```python
"""
1. Implementeaza o functie care verifica daca un numar luat
ca si parametru este par. Daca e par returneaza True,
daca nu, returneaza False.

Fa o verificare pentru a te asigura ca parametrul dat este
un numar intreg. Daca nu e, arunca o exceptie custom.

2. Testeaza cazul in care se arunca eroarea,
folosind libraria unittest, respectiv pytest
"""
```
## 📌 TDD
- Test Driven Development (TDD) este o practica de dezvoltare
software care ne impune sa scriem in mod incremental teste
pentru caracteristicile pe care dorim sa le adaugam.

- Cei trei pasi pe care ar trebui developerii sa ii urmeze sunt:
  - Scrie un test pentru o implemetare care esueaza
  - Scrie codul ca sa faci testul sa treaca cu success
  - Refactorizeaza codul in caz de nevoie

- Acest proces este cunoscut ca ciclul Red-Green-Refactory
  - Scrii un test pentru cum ar trebui codul nou sa se comporte si il privesti cu nu trece cu success - Red
  - Scrii codul pana cand testul trece cu success - Green
  - Refactorizezi codul pentru a-l face mai eficient si citibil.

- Implementarea este gata cand nu mai trebuie sa scrii cod ca sa treaca testul
- Plangerea comuna a utilizarii TDD este ca dureaza prea mult timp. Dar cu cat devii tot mai eficient in a scrie testele, timpul necesar pentru a mentine codul scade.

## 📌 Python Packages
https://packaging.python.org/tutorials/installing-packages/
https://packaging.python.org/tutorials/packaging-projects/
