#
# Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3

schimbari_max = 3
schimbari_efectuate = 0
players = ["Neymar", "Ronaldo", "Guti", "Adriano", "Roberto"]
x = input("player out:")
y = input("player in:")

if x in players:
    schimbari_efectuate += int(input("cate schimbari ai facut?:"))
    if schimbari_efectuate >= schimbari_max:
        print("Ai atins nr maxim de schimbari")
    else:
        players.remove(x)
        players.append(y)
        z = schimbari_max - schimbari_efectuate
        print(f"A intrat {y} , a iesit {x} , mai ai {z} schimbari")
        print(players)
else:
    schimbari_efectuate += int(input("cate schimbari ai facut?:"))
    z = schimbari_max - schimbari_efectuate
    print(f"Nu se poate efectua schimbarea deoarece jucătorul {x} nu e în teren, mai ai"
          f" {z} schimbari")

# seturi

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}


# ● Adaugă în zilele_sapt ‘luni’

zile_sapt.add("luni")

# ● Afișează zile_sapt

print(zile_sapt)

# 2.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

if weekend.issubset(zile_sapt):
    print("True")
else:
    print("False")

# 3. Afișează diferențele dintre aceste 2 seturi.

dif = zile_sapt.difference(weekend)
print(dif)

# 4. Afișează intersecția elementelor din aceste 2 seturi

intersection = zile_sapt.intersection(weekend)
print(intersection)

