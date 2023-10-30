# modules
import itertools

# variables
MAX_ITEMS_TO_SACRIFICE = 4
MAX_COMBINATIONS = 3

# ancient mobs
ancient_mobs = {
    "Abominable Weaver": ["A", "S", "T"],
    "Ancient Beast": ["A", "B"],
    "Ethereal Guardian": ["E", "G"],
}

# ruins
items_to_sacrifice = {
    "A": [
        {"class": "Weapon", "item": "Weapon: Battlestaff of Terror", "ruins": ["A", "S"]},
        {"class": "Weapon", "item": "Weapon: Cursed Axe", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Dark Katana", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Diamond Pickaxe", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Firebrand", "ruins": ["A", "S"]},
        {"class": "Weapon", "item": "Weapon: Flail", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Hammer of Gravity", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Jailor's Scythe", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Stormlander", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: The Last Laugh", "ruins": ["A", "S"]},
        {"class": "Weapon", "item": "Weapon: Venom Glaive", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Whirlwind", "ruins": ["A"]},
        {"class": "Armor", "item": "Armor: Battle Robe", "ruins": ["A"]},
        {"class": "Bow", "item": "Bow: Imploding Crossbow", "ruins": ["A", "S"]},
    ],
    "S": [
        {"class": "Weapon", "item": "Weapon: Battlestaff of Terror", "ruins": ["A", "S"]},
        {"class": "Bow", "item": "Bow: Imploding Crossbow", "ruins": ["A", "S"]}
    ],
    "T": [
        {"class": "Artifact", "item": "Artifact: Corrupted Seeds", "ruins": ["T"]}
    ],
    "B": [],
    "E": [],
    "G": [],
}

# functions
def get_ruins_and_items_to_summon(ancient_mobs_input):
    ruins = set()
    combinations = []
    items_needed = set()
    item_classes = set()

    for ancient_mob in ancient_mobs_input:
        if ancient_mob in ancient_mobs:
            mob_ruins = ancient_mobs[ancient_mob]
            ruins.update(mob_ruins)
            for ruin in mob_ruins:
                if ruin in items_to_sacrifice:
                    rune_items = items_to_sacrifice[ruin]
                    for item_data in rune_items:
                        item_class = item_data["class"]
                        item = item_data["item"]
                        ruins_required = item_data["ruins"]
                        if all(ruin in ruins for ruin in ruins_required):
                            if item_class not in item_classes:
                                items_needed.add(item)
                                item_classes.add(item_class)
                else:
                    print(f"No items found for rune '{ruin}'")
        else:
            print(f"Ancient mob '{ancient_mob}' not found.")

    items_needed = list(items_needed)[:MAX_ITEMS_TO_SACRIFICE]
    item_combinations = list(itertools.combinations(items_needed, min(len(items_needed), MAX_COMBINATIONS)))
    combinations.extend(item_combinations)

    return {"ruins": ruins, "combinations": combinations}

#code
num_ancients = int(input("Enter the number of ancient mobs to summon (1-4): "))
if num_ancients < 1 or num_ancients > 4:
    print("Invalid number of ancient mobs.")
else:
    ancient_mobs_input = []
    for i in range(num_ancients):
        ancient_mob = input(f"Enter the name of ancient mob {i+1}: ")
        ancient_mobs_input.append(ancient_mob)

    result = get_ruins_and_items_to_summon(ancient_mobs_input)
    if isinstance(result, str):
        print(result)
    else:
        ruins = result["ruins"]
        combinations = result["combinations"]
        print(f"To summon {', '.join(ancient_mobs_input)}, complete the following ruins:")
        for ruin in ruins:
            print(ruin)
        print("")
        print(f"Here are {min(MAX_COMBINATIONS, len(combinations))} combinations to sacrifice items:")
        for i, combination in enumerate(combinations[:MAX_COMBINATIONS], 1):
            print(f"Combination {i}:")
            combination_classes = set()
            for item in combination:
                try:
                    item_class = items_to_sacrifice[item]["class"]
                    if item_class not in combination_classes:
                        print(item)
                        combination_classes.add(item_class)
                except KeyError:
                    print(f"{item}")
            print("")
