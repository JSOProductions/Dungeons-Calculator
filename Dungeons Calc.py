import tkinter as tk
from tkinter import messagebox
import itertools

# Variables
MAX_ITEMS_TO_SACRIFICE = 4
MAX_COMBINATIONS = 3
combinations = []
combination_index = 0

# Ancient mobs
ancient_mobs = {
    "Abominable Weaver": [["A", "S", "T"], [2, 1, 1]],
    "Ancient Beast": [["A", "B"], [1, 2]],
    "Ethereal Guardian": [["E", "G"], [1, 1]],
}

# Ruins
items_to_sacrifice = {
    "A": [
        {"class": "Weapon", "item": "Weapon: Battlestaff of Terror", "ruins": ["A", "S"]},
        {"class": "Weapon", "item": "Weapon: Cursed Axe", "ruins": ["A"]},
        {"class": "Weapon", "item": "Weapon: Dark Katana", "ruins": ["A"]},
        # ... more items ...
    ],
    "S": [
        {"class": "Weapon", "item": "Weapon: Battlestaff of Terror", "ruins": ["A", "S"]},
        # ... more items ...
    ],
    "T": [
        {"class": "Artifact", "item": "Artifact: Corrupted Seeds", "ruins": ["T"]}
    ],
    "B": [],
    "E": [],
    "G": [],
}

# Functions
def get_ruins_and_items_to_summon():
    global combinations, combination_index  # Declare combinations and combination_index as global variables

    ancient_mobs_input = []
    for ancient_mob, var in ancient_mob_buttons.items():
        if var.get() == 1:
            ancient_mobs_input.append(ancient_mob)

    ruins = set()
    combinations = []
    items_needed = set()
    item_classes = set()

    for ancient_mob in ancient_mobs_input:
        if ancient_mob in ancient_mobs:
            mob_ruins, mob_counts = ancient_mobs[ancient_mob]
            ruins.update(mob_ruins)
            for ruin, count in zip(mob_ruins, mob_counts):
                if ruin in items_to_sacrifice:
                    rune_items = items_to_sacrifice[ruin]
                    for item_data in rune_items:
                        item_class = item_data["class"]
                        item = item_data["item"]
                        ruins_required = item_data["ruins"]
                        if all(ruin in ruins for ruin in ruins_required):
                            if item_class not in item_classes:
                                items_needed.add((item, count))
                                item_classes.add(item_class)
                else:
                    print(f"No items found for rune '{ruin}'")
        else:
            print(f"Ancient mob '{ancient_mob}' not found.")

    items_needed = list(items_needed)[:MAX_ITEMS_TO_SACRIFICE]
    item_combinations = list(itertools.combinations(items_needed, min(len(items_needed), MAX_COMBINATIONS)))
    combinations.extend(item_combinations)
    combination_index = 0

    items_text.config(state=tk.NORMAL)
    items_text.delete(1.0, tk.END)
    for item, count in items_needed:
        items_text.insert(tk.END, f"- {item} (x{count})\n")
    items_text.config(state=tk.DISABLED)

    return {"ruins": ruins, "combinations": combinations}

def summon_ancient_mobs():
    result = get_ruins_and_items_to_summon()
    if isinstance(result, str):
        messagebox.showerror("Error", result)
    else:
        ruins = result["ruins"]
        combinations = result["combinations"]
        ruins_label.config(text="Ruins to complete:")
        ruins_text.config(state=tk.NORMAL)
        ruins_text.delete(1.0, tk.END)
        for ruin in ruins:
            ruins_text.insert(tk.END, f"- {ruin}\n")
        ruins_text.config(state=tk.DISABLED)

        # Remove the "Next" button if there are no more combinations
        if not combinations:
            next_button.config(state=tk.DISABLED)
        else:
            next_button.config(state=tk.NORMAL)
            show_next_combination()

def show_next_combination():
    global combination_index  # Declare combination_index as a global variable
    if combinations:
        combination = combinations[combination_index]
        combination_index = (combination_index + 1) % len(combinations)
        combination_text.config(state=tk.NORMAL)
        combination_text.delete(1.0, tk.END)
        for item, count in combination:
            combination_text.insert(tk.END, f"- {item} (x{count})\n")
        combination_text.config(state=tk.DISApologies, but it seems like the code snippet got truncated. Could you please provide the complete code so that I can assist you with modifying it accordingly?
