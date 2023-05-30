# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o.

note = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note)

# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).

note = note[::-1]
print(note)

# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz
# deoarece metoda face asta automat.

note.reverse()

# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta initiala

print(note)
# Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.

note2 = note

# 2. De câte ori apare ‘do’?

print(note2.count("do"))
# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
#  Găsește 2 variante să le unești într-o singură listă.

list1.extend(list2)
list1 += list2  # aici o sa se suprascrie acum lista1 extinsa cu lista2
                # in principiu am vrut sa arat 2 variante cum se cere in cerinta


# 4 ● Sortează și afișează lista generată la exercițiul anterior.

list1.sort()
print(list1)

# ● Stergeti numărul 0 folosind o funcție.

list1.remove(0)
# ● Afișaza iar lista.

print(list1)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.

if len(list1) == 0:
    print("lista este goala")
else:
    print("lista nu este goala")

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

list1.clear()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.


if len(list1) == 0:
    print("lista este goala")
else:
    print(" lista nu este goala")

# Acum ar trebui să se afișeze că lista e goală.


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

dict1 = {"Ana": 8,
         "Gigel": 10,
         "Dorel": 5
         }

# Folosește o funcție că să afișezi Elevii (cheile)

print(dict1.keys())

# 9. Printează cei 3 elevi și notele lo
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6

dict1.update({"Dorel": 6})

# ● Printează nota după modificare
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă

dict1.pop("Gigel")
print(dict1)

# ● Vine un coleg nou. Adaugă Ionică, cu nota 9

dict1["Ionica"] = 9

# ● Printează noii elevi

print(dict1)
print(dict1.keys())

print(f"A intrat{subs_players[2]} a iesit {players[4]}, mai aveti{schimbari_max - schimbari_efectuate} schimbari")