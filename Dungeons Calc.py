import tkinter as tk
from tkinter import messagebox
import itertools

# Variables
MAX_ITEMS_TO_SACRIFICE = 4
MAX_COMBINATIONS = 3

# Ancient mobs
ancient_mobs = {
    "Abominable Weaver": ["A", "S", "T"],
    "Ancient Beast": ["A", "B"],
    "Ethereal Guardian": ["E", "G"],
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

    items_text.config(state=tk.NORMAL)
    items_text.delete(1.0, tk.END)
    for item in items_needed:
        items_text.insert(tk.END, f"- {item}\n")
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

# Create the Tkinter window
window = tk.Tk()
window.title("Ancient Mob Summoner")

# Create and configure the GUI elements
ancient_mob_label = tk.Label(window, text="Select ancient mobs:")
ancient_mob_label.pack()

ancient_mob_buttons = {}
for ancient_mob in ancient_mobs:
    ancient_mob_buttons[ancient_mob] = tk.IntVar()
    ancient_mob_checkbutton = tk.Checkbutton(window, text=ancient_mob, variable=ancient_mob_buttons[ancient_mob], onvalue=1, offvalue=0)
    ancient_mob_checkbutton.pack()

summon_button = tk.Button(window, text="Summon", command=summon_ancient_mobs)
summon_button.pack()

ruins_label = tk.Label(window, text="")
ruins_label.pack()

ruins_text = tk.Text(window, height=10, width=30)
ruins_text.config(state=tk.DISABLED)
ruins_text.pack()

items_label = tk.Label(window, text="Items to sacrifice:")
items_label.pack()

items_text = tk.Text(window, height=10, width=30)
items_text.config(state=tk.DISABLED)
items_text.pack()

window.mainloop()
