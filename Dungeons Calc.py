# modules


# variables #
MAX_ITEMS_TO_SACRIFICE = 4

# ancient mobs #
ancient_mobs = {
    "Abominable Weaver": ["A", "S", "T"],
}

# Runes #

items_to_sacrifice = {
    "A": {
        "Weapon": ["Weapon: Battlestaff of Terror", "Weapon: Cursed Axe", "Weapon: Dark Katana", "Weapon: Diamond Pickaxe", "Weapon: Firebrand", "Weapon: Flail", "Weapon: Hammer of Gravity", "Weapon: Jailor's Scythe", "Weapon: Stormlander", "Weapon: The Last Laugh", "Weapon: Venom Glaive", "Weapon: Whirlwind"],
        "Armor": ["Armor: Battle Robe"],
        "Bow": ["Bow: Imploding Crossbow"],
        "Artifact": ["Artifact: Corrupted Seeds"],
    },
    "S": {},
    "T": {},
}

# functions
def get_ruins_and_items_to_summon(ancient_mob):
    if ancient_mob in ancient_mobs:
        ruins = ancient_mobs[ancient_mob]
        items = []
        selected_classes = set()
        for ruin in ruins:
            if ruin in items_to_sacrifice:
                rune_items = items_to_sacrifice[ruin]
                for item_class, items_list in rune_items.items():
                    if item_class in selected_classes:
                        continue
                    if items_list:
                        item = items_list.pop(0)
                        items.append(item)
                        selected_classes.add(item_class)
                        break
                    else:
                        print(f"No items found for rune '{ruin}' and class '{item_class}'")
            else:
                print(f"No items found for rune '{ruin}'")
            if len(items) >= MAX_ITEMS_TO_SACRIFICE:
                break
        return {"ruins": ruins, "items": items[:MAX_ITEMS_TO_SACRIFICE]}
    else:
        return "Ancient mob not found."


# code
while True: 
    mob_name = input("")
    result = get_ruins_and_items_to_summon(mob_name)
    if isinstance(result, str):
        print(result)
    else:
        ruins = result["ruins"]
        items = result["items"]
        print(f"To summon {mob_name}, complete the following ruins:")
        for ruin in ruins:
            print(ruin)
        print("")
        print("Sacrifice the following items:")
        for item in items:
            print(item)
    print("")
