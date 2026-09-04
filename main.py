from SmartSearch import infer_search
from Pokeprint import print_pokemon
import urllib.request
import os
import csv
import json

def loadPokemon():
    with open("list.csv", "r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("You did not catch them all...")
        return None
    return rows

def search_pokemon(pokemon_list):
    query = input("Enter a search query: ")
    field, value = infer_search(query)

    ids = []
    for mon in pokemon_list:
        if field == "type1":
            hit = (
                mon["type1"].lower() == str(value).lower()
                or mon.get("type2", "").lower() == str(value).lower()
            )
        else:
            hit = str(mon[field]).lower() == str(value).lower()

        if hit:
            ids.append(int(mon["dex"]))

    print_pokemon(pokemon_list, ids)

def add_pokemon(pokemon_list):
    query = input("Enter a pokemon to add: ")
    field, value = infer_search(query)
    rows = fetch_pokemon_from_api(field, value)

    if not rows:
        print("No results.")
        input("Press Enter to continue...")
        return

    for i, mon in enumerate(rows, start=1):
        print(f"{i}. #{mon['dex']} - {mon['name']}")

    try:
        choice = int(input("Add which number? "))
    except ValueError:
        print("Be sure to type the (number).")
        return

    if choice < 1 or choice > len(rows):
        print("That number is not on the list.")
        return

    selected = rows[choice - 1]
    pokemon_list.append(selected)
    print(f"Added {selected['name']}.")

def fetch_pokemon_from_api(field, value):
    if field not in ("name", "dex"):
        print("Add needs a name or dex number.")
        return []

    key = str(value).strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{key}"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "pokymans/1.0"},
    )

    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))

    types = [t["type"]["name"].title() for t in data["types"]]
    row = {
        "dex": str(data["id"]),
        "name": data["name"].title(),
        "type1": types[0],
        "type2": types[1] if len(types) > 1 else "",
        "gen": "",
        "height_m": str(data["height"] / 10),
        "weight_kg": str(data["weight"] / 10),
    }
    return [row]

def remove_pokemon(pokemon_list):
    query = input("Enter a search query to remove: ")
    field, value = infer_search(query)

    ids = []
    for mon in pokemon_list:
        if field == "type1":
            hit = (
                mon["type1"].lower() == str(value).lower()
                or mon.get("type2", "").lower() == str(value).lower()
            )
        else:
            hit = str(mon[field]).lower() == str(value).lower()

        if hit:
            ids.append(int(mon["dex"]))

    if not ids:
        print("No matching pokemon to remove.")
        input("Press Enter to continue...")
        return

    print()
    print("Removing...")
    print_pokemon(pokemon_list, ids)

    wanted = {str(i) for i in ids}
    pokemon_list[:] = [
        mon for mon in pokemon_list if str(mon["dex"]) not in wanted
    ]

def save_pokemon(pokemon_list):
    field_names = ["dex", "name", "type1", "type2", "gen", "height_m", "weight_kg"]
    with open("list.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, field_names)
        writer.writeheader()
        writer.writerows(pokemon_list)
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
            print()
            print_pokemon(pokemon_list)
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