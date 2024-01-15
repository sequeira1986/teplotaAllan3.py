# komentujem kod
# generujem prastne pole
libreria = []
while True:
    #hlavne ciklus  tu deklarujem hlavny ciklus a Menu
    print("\n Menu:")
    print("1.pridat knihu ")
    print("2.odstranit knihu ")
    print("3.vypisat vsetky knihy")
    print("4.Ukoncit program")
#ziadame  aby sa zadal moynost
    elleccion = input("zadaj moznost (1/2/3/4): ")

# prvi if
#1.pridat knihu
    if elleccion=="1":
        nombre_del_libro = input("Zadaj nazov knihy: ")
        libreria.append(nombre_del_libro)
        print(f"kniha  '{nombre_del_libro}' bola pridana. ")
#2.odstranit knihu

    elif elleccion=="2":
        nombre_del_libro= input("Zadaj nazov knihu ktoru chcete ostranit ")
        if nombre_del_libro not in libreria:
            print(f"kniha  '{nombre_del_libro}' nebola najdena v kniznice.")
        else:
            libreria.remove(nombre_del_libro)
            print(f"kniha '{nombre_del_libro}' bola ostranena.")
    #3.vypisat vsetky knihy
    elif elleccion=="3":
        if libreria:
            print("vsetky knihy v kniznice: ")
            for kniha in libreria:
                print(kniha)
        else:
            print(" kniynica je prazna! ")
#4.Ukoncit program
    elif elleccion=="4":
        print(" Program bol ukonceny. ")
        break
#neplatna volba
    else:
        print(" prosim, vyberte platnu moznost ")

