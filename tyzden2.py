import datetime

# Definujte správne meno a heslo
spravne_meno = "pouzivatel"
spravne_heslo = 12345


# Definujte funkciu na zápis informácií o výnimočnej udalosti do súboru
def zapis_vynimky(vynimka):
    with open("vynimky.log", "a") as f:
        f.write(str(datetime.datetime.now()) + " " + str(vynimka) + "\n")
# Získajte prihlasovacie údaje od používateľa
zadane_meno = input("Zadajte meno: ")
zadane_heslo = input("Zadajte heslo: ")
# Skúste nastaviť heslo na číselnú hodnotu
try:
    zadane_heslo = int(zadane_heslo)
except ValueError:
    print("Heslo musí byť číslo!")
    zapis_vynimky(Exception("Heslo musí byť číslo!"))
    exit()
# Overte, či sú prihlasovacie údaje správne
try:
    if zadane_meno in ["pouzivatel", "admin"]:
        if zadane_heslo == spravne_heslo:
            print("Prihlásenie úspešné!")
        else:
            print("Nesprávne heslo!")
            zapis_vynimky(Exception("Nesprávne heslo!"))
    else:
        print("Nesprávne meno!")
        zapis_vynimky(Exception("Nesprávne meno!"))
except KeyError:
    print("Meno nie je v databáze!")
    zapis_vynimky(Exception("Meno nie je v databáze!"))
except TypeError:
    print("Meno alebo heslo musí byť správneho typu!")
    zapis_vynimky(Exception("Meno alebo heslo musí byť správneho typu!"))
except IndexError:
    print("Heslo je príliš krátke!")
    zapis_vynimky(Exception("Heslo je príliš krátke!"))
