import random
# Definition of items that Alpha Lunatic can drop and their drop rates
alpha_lunatic_items = [
    {"id": 705, "name": "Clover", "drop": 100},
    {"id": 949, "name": "Feather", "drop": 100},
    {"id": 2262, "name": "Clown Nose", "drop": 0.2},
    {"id": 1102, "name": "Sword [4]", "drop": 5},
    {"id": 601, "name": "Fly Wing", "drop": 25},
    {"id": 515, "name": "Carrot", "drop": 100},
    {"id": 622, "name": "Rainbow Carrot", "drop": 1},
    {"id": 4006, "name": "Lunatic Card", "drop": 1}
]
# Function to simulate the drop of an item based on the drop rate
def simulate_alpha_lunatic_drop():
    drops = []  # List to store the items dropped in this attempt
    # Check each item individually based on its drop rate
    for item in alpha_lunatic_items:
        chance = random.uniform(0, 100)  # Generate a random number between 0 and 100
        if chance <= item["drop"]:  # If the chance is less than or equal to the drop rate, the item is dropped
            drops.append(item["name"])  # Add the item to the drop list
    return drops  # Return the list of items that were dropped
# Function to simulate killing N Alpha Lunatics and collecting items
def kill_alpha_lunatics(quantity):
    dropped_items = {}  # Dictionary to store the items and their quantities
    # Simulate killing 'quantity' Alpha Lunatics
    for _ in range(quantity):
        items = simulate_alpha_lunatic_drop()  # Get the items dropped in this attempt
        for item in items:
            if item in dropped_items:
                dropped_items[item] += 1  # If the item has been dropped before, increment the count
            else:
                dropped_items[item] = 1  # If the item hasn't been dropped yet, add it to the dictionary with a count of 1
    return dropped_items  # Return the dictionary with all the dropped items and their quantities
# Main program
if __name__ == "__main__":
    # User input: how many Alpha Lunatics they want to kill
    times = int(input("How many Alpha Lunatics do you want to kill? "))
    # Simulate killing the Alpha Lunatics and storing the drops
    result = kill_alpha_lunatics(times)
    # Display the items that were dropped and their quantities
    if result:
        print("\nYou have obtained the following items:")
        for item, quantity in result.items():
            print(f"{item}: {quantity}x")
    else:
        print("\nYou didn't get any items.")
