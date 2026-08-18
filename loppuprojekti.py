def load_movies():
    print("Tämä funktio lataa elokuvia")

def save_movies():
    print("Tämä funktio tallentaa elokuvia")

def show_menu():
    print("Tämä funktio näyttää menua")

def add_movie():
    print("Tämä funktio lisää elokuvan")

def show_movies():
    print("Tämä funktio näyttää elokuvia")

def search_movies():
    print("Tämä funktio hakee elokuvia")

def edit_movie():
    print("Tämä funktio muokkaa elokuvia")

def delete_movies():
    print("Tämä funktio poistaa elokuvia")

def show_statistics():
    print("Tämä funktio näyttää tilastoja")


while True:
    print("1. Lisää elokuva")
    print("2. Näytä kaikki elokuvat")
    print("3. Hae elokuvia")
    print("4. Muokkaa elokuvaa")
    print("5. Poista elokuva")
    print("6. Näytä tilastot")
    print("0. Tallenna ja lopeta")

    valinta = int(input("Valitse toiminta (0-6): "))

    if valinta == 0:
        print("Tallenna ja lopeta")
        break
    if valinta not in [1, 2, 3, 4, 5, 6, 0]:
        print("Väärä valinta")
        continue

    if valinta == 1:
        add_movie()
    elif valinta == 2:
        show_movies()
    elif valinta == 3:
        search_movies
    elif valinta == 4:
        edit_movie()
    elif valinta == 5:
        delete_movies()
    elif valinta == 6:
        show_statistics()