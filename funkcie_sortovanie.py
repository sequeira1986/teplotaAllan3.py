#!/usr/bin/python
# -*- coding: utf-8 -*-


import random

zoznam1 = [random.randint(0, 100) for i in range(5)]
zoznam2 = [random.randint(0, 100) for i in range(5)]
zoznam3 = [random.randint(0, 100) for i in range(5)]
zoznam4 = [random.randint(0, 100) for i in range(5)]

zasnam5 = []
for prvok1 in zoznam1:
    zasnam5.append(prvok1)
for prvok2 in zoznam2:
    zasnam5.append(prvok2)
for prvok3 in zoznam3:
    zasnam5.append(prvok3)
for prvok4 in zoznam4:
    zasnam5.append(prvok4)


# print(zasnam5)

def sortuj(zasnam, poradie):
    if poradie == "zostupne":
        zasnam.sort(reverse=True)
    elif poradie == "vzostupne":
        zasnam.sort()
    else:
        print("Zadaj správnu hodnotu")

    return zasnam


# print(sortuj(zasnam5, "zostupne"))
def hladaj(zoznam, cislo):
    return any(prvok == cislo for index, prvok in enumerate(zoznam))


print(hladaj(zasnam5, 21))

print(hladaj(zasnam5, 3))
print(sortuj(zasnam5, "zostupne"))
print(sortuj(zasnam5, "njiako"))
print(sortuj(zasnam5, "vzostupne"))
