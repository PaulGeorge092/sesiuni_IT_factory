# # 1.Având lista:
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# # Folosește un for că să iterezi prin toată lista și să afișezi;
# # ● ‘Mașina mea preferată este x’.
#
#
# for masina in range(len(masini)):
#     print(f"Masina mea preferata este {masini[masina]}")
#
# # ● Fă același lucru cu un for each.
#
# for masina in masini:
#     print(f"Masina mea preferata este {masina}")
#
# # ● Fă același lucru cu un while.
#
# index = 0
# while True:
#     index < len(masini)
#     print(f"Masina mea preferata este {masini[index]}")
#     index += 1
#     break
#
# # 2. Aceeași listă:
# # Folosește un for else  În for
#
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for x in cars:
#     for y in masini:
#         print("Masina mea preferata este", x, y)
#     else:
#         print("Stop")
#
# # - Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul
# # - Printează lista.
#
#
# cars[1:-1] = [car.upper() for car in cars[1:-1]]
# print(cars)
#
# # 3. Aceeași listă:
# # Vine un cumpărător care dorește să cumpere un Mercedes.
# # Iterează prin ea prin modalitatea aleasă de tine.
# # Printează ‘am găsit mașina dorită de dvs’
# # Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# # Altfel:
# # Printează ‘Am găsit mașina X. Mai căutam‘
#
# import random
#
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# while True:
#     x = random.choice(cars)
#     if x == "Mercedes":
#         print("Am gasit masina dorita de dvs")
#         break
#     else:
#         print(f"Am gasit masina {x}, mai cautam")
#
# # 4. Aceeași listă;
# # Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# # excepția Trabant și Lastun.
# # Dacă mașina e Trabant sau Lăstun:
# # Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# # else).
# # - Printează S-ar putea să vă placă mașina x.
#
#
# for car in cars:
#     if car in ["Trabant", "Lastun"]:
#         continue
#     print(f"S-ar putea sa va placa masina {car}")
#
# # 5. Modernizează parcul de mașini:
# # ● Crează o listă goală, masini_vechi.
#
# masini_vechi = []
#
# # ● Iterează prin mașini.
# # Când găsesti Lăstun sau Trabant:
# # - Salvează aceste mașini în masini_vechi.
#
# for item in cars:
#     if item in ["Trabant", "Lastun"]:
#         cars.remove(item)
#         masini_vechi.append(item)
#
# # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#
# cars.append("Tesla")
#
# # ● Printează Modele vechi: x.
# print(masini_vechi)
#
# # ● Modele noi: x.
# print(cars)
#
# # 6. Având dict:
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# # Vine un client cu un buget de 15000 euro.
# # ● Iterează prin dict.items() și accesează mașina și prețul.
#
# buget = 15000
# dct_nou ={}
# for x , y in pret_masini.items():
#     if y <= buget:
#         dct_nou[x] = y
# print(dct_nou)
# ##  Prezintă doar mașinile care se încadrează în acest buget.
# for i in dct_nou:
#     print(i)
#
# # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină x
#
#
# print(f" Pentru un buget de sub 15000 euro puteți alege mașina {dct_nou}")
#
# # ● Iterează prin listă.
# # 7. Având lista:
# # ● Iterează prin ea.
# # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
#
# numere =numere= [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# element = 3
# x = 0
# for i in numere:
#     if i == element:
#         x += 1
# print(x)
#
# # 8. Aceeași listă:
# # ● Iterează prin ea
# # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
#
# suma = 0
# for i in numere:
#     suma += i
# print(suma)
#
# # 9. Aceeași listă:
# # ● Iterează prin ea.
# # ● Afișază cel mai mare număr (nu ai voie să folosești max).
#
# nr_max = numere[i]
# for i in numere:
#     if i > nr_max:
#         nr_max == i
#
# print(nr_max)
#
# # 10. Aceeași listă:
# # ● Iterează prin ea.
# # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# # Ex: dacă e 3, să devină -3
# # ● Afișază noua listă.
#
# # variante buna
# for i in range(len(numere)):
#     if numere[i] > 0:
#         numere[i] = -numere[i]
#     else:
#         pass
#
# print(numere)
#
# # varianta cu problema
#
# for i in numere:
#     if numere[i] > 0:
#         numere[i] = -numere[i]
#     else:
#         pass
# print(numere)
# # output [-5, -7, 3, -, -3, -1, 0, -4, 3]
#
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# #
# # def bubbleSort(array):
# #     # loop to access each array element
# #     for i in range(len(array)):
# #
# #         # loop to compare array elements
# #         for j in range(0, len(array) - i - 1):
# #
# #             # compare two adjacent elements
# #             # change > to < to sort in descending order
# #             if array[j] > array[j + 1]:
# #                 # swapping elements if elements
# #                 # are not in the intended order
# #                 temp = array[j]
# #                 array[j] = array[j + 1]
# #                 array[j + 1] = temp
# #

#
# for i in range(len(alte_numere)):
#     for x in range(0, len(alte_numere)- i - 1):
#         if alte_numere[x] > [alte_numere[x + 1]]:
#             z = alte_numere[x]
#             alte_numere[x] = alte_numere[x]-1
#             alte_numere[x+ 1] = z

def ascendint_lista(lista):
    for index in range(len(lista)):
        for element in lista:

            if index < element:
                element = index + 1

ascendint_lista([-5, 7, 2, 9, 12, 3, 1, -6, -4, 3])
print(ascendint_lista(lista))


