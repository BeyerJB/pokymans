TYPES = {
    "normal", "fire", "water", "electric", "grass", "ice",
    "fighting", "poison", "ground", "flying", "psychic", "bug",
    "rock", "ghost", "dragon", "dark", "steel", "fairy",
}

REGIONS = {
    "kanto": 1,
    "johto": 2,
    "hoenn": 3,
    "sinnoh": 4,
    "unova": 5,
    "kalos": 6,
    "alola": 7,
    "galar": 8,
    "paldea": 9,
}

def infer_search(query):
    raw = str(query).strip()
    key = raw.lower()

    if raw.isdigit():
        return "dex", raw

    if key in REGIONS:
        return "gen", str(REGIONS[key])

    if key in TYPES:
        return "type1", raw.title()

    return "name", raw

if __name__ == "__main__":
    tests = ["Fire", 471, "Hoenn", "Glaceon", "Porygon2"]
    for item in tests:
        field, value = infer_search(item)
        print(field, value)