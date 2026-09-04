from SmartSearch import infer_search
import os
import csv


def loadPokemon():
    with open("list.csv", "r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("lYou did not catch them all...")
        return None
    return rows

def search_pokemon(pokemon_list):
    pass

def add_pokemon(pokemon_list):
    pass

def remove_pokemon(pokemon_list):
    pass

def save_pokemon(pokemon_list):
    pass













if __name__ == '__main__':
    pokemon_list = loadPokemon()
    if pokemon_list is None:
        pokemon_list = []

    choice = 0
    while choice != 5:
        print("\n--- Pokedex ---")
        print("1. View Pokemon")
        print("2. Search Pokemon")
        print("3. Add Pokemon")
        print("4. Remove Pokemon")
        print("5. Save and quit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Enter a number 1-5.")
            continue

        if choice == 1:
            view_pokemon(pokemon_list)
        elif choice == 2:
            search_pokemon(pokemon_list)
        elif choice == 3:
            add_pokemon(pokemon_list)
        elif choice == 4:
            remove_pokemon(pokemon_list)
        elif choice == 5:
            save_pokemon(pokemon_list)
            print("Saved. Goodbye.")
        else:
            print("Enter a number 1-5.")