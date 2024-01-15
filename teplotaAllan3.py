# -*- coding: utf-8 -*-

def konvertuj_teplotu(teplota, jednotka):
    if jednotka == 'C':
        # Konvertujeme  z Celsius na Fahrenheit podla vsorec
        konvertovana_teplota = (teplota * 9/5) + 32
        vystupna_jednotka = 'F'
    elif jednotka == 'F':
        # Konvertuj z Fahrenheit na Celsius
        konvertovana_teplota = (teplota - 32) * 5/9
        vystupna_jednotka = 'C'
        # aby napisal opacna jednotka zadavame dalsiu hodnotu vystupna_jednotka
    else:
        # Ošetrenie chyby pre nesprávnu jednotku
        print("Chyba: Zadajte správnu jednotku ('C' alebo 'F')")
        return

    # Zaokruhli výsledok na dve desatinné miesta
    konvertovana_teplota = round(konvertovana_teplota, 2)

    # tu Vypíseme  vysledok do konzoly
    print(f"Konvertovaná teplota: {konvertovana_teplota} {vystupna_jednotka}")

# Zadanie hodnôt interaktívne cez input
teplota = float(input("Zadajte teplotu: "))
jednotka = input("Zadajte jednotku ('C' pre stupne Celsius, 'F' pre stupne Fahrenheit): ")

# Príklad volania funkcie s použitím interaktívne zadaných hodnôt
konvertuj_teplotu(teplota, jednotka)
