COL_WIDTH = 28

def format_pokemon_lines(mon):
    type_label = mon["type1"]
    if mon.get("type2"):
        type_label = f"{mon['type1']}/{mon['type2']}"
    return [
        f"#{mon['dex']} - {mon['name']}",
        f"{type_label} Type, Gen {mon['gen']}",
        f"{mon['height_m']}m, {mon['weight_kg']}kgs",
    ]


def print_pokemon(pokemon_list, ids=None):
    if not pokemon_list:
        print("No pokemon to display.")
        input("Press Enter to continue...")
        return

    if ids is None:
        to_print = pokemon_list
    else:
        wanted = {str(i) for i in ids}
        to_print = [mon for mon in pokemon_list if str(mon["dex"]) in wanted]

    if not to_print:
        print("No matching pokemon.")
        input("Press Enter to continue...")
        return

    for start in range(0, len(to_print), 3):
        group = to_print[start:start + 3]
        cards = [format_pokemon_lines(mon) for mon in group]
        for line_no in range(3):
            parts = [cards[i][line_no].ljust(COL_WIDTH) for i in range(len(cards))]
            print("".join(parts))
        print()

    input("Press Enter to continue...")