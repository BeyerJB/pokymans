def format_pokemon(mon):
    type_label = mon["type1"]
    if mon.get("type2"):
        type_label = f"{mon["type1"]}/{mon["type2"]}"
    return (
        f"#{mon["dex"]} - {mon["name"]}\n"
        f"{type_label} Type, Gen {mon["gen"]}\n"
        f"{mon["height_m"]}m, {mon["weight_kg"]}kgs"
    )


def print_pokemon(pokemon_list, ids=None):
    if not pokemon_list:
        print("No pokemon to display.")
        return

    if ids is None:
        to_print = pokemon_list
    else:
        wanted = {str(i) for i in ids}
        to_print = [mon for mon in pokemon_list if str(mon["dex"]) in wanted]

    if not to_print:
        print("No matching pokemon.")
        return

    for mon in to_print:
        print(format_pokemon(mon))
        print()
    
    input("Press Enter to continue...")