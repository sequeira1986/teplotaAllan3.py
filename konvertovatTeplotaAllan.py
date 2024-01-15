# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

def konvertuj_teplotu(teplota, jednotka):
    if jednotka == 'C':
        # Konvertujeme  z Celsius na Fahrenheit
        konvertovana_teplota = (teplota * 9/5) + 32
    elif jednotka == 'F':
        # Konvertujeme  z Fahrenheit na Celsius
        konvertovana_teplota = (teplota - 32) * 5/9
    else:
        #  chyby pre nesprávnu jednotku
        print("Chyba: Zadajte správnu jednotku ('C' alebo 'F')")
        return

    # Zaokruhlime  výsledok na dve desatinné miesta
    konvertovana_teplota = round(konvertovana_teplota, 2)

    # Vypíš výsledok do konzoly
    print(f"Konvertovaná teplota: {konvertovana_teplota} {jednotka}")

# Zadanie hodnôt interaktívne cez input
teplota = float(input("Zadajte teplotu: "))
jednotka = input("Zadajte jednotku ('C' pre stupne Celsius, 'F' pre stupne Fahrenheit): ")

# Príklad volania funkcie s použitím interaktívne zadaných hodnôt
konvertuj_teplotu(teplota, jednotka)
