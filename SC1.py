#Name:tristan long
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

enemies = {
    "Goblin": {
        "health": 30,
        "damage": 5,
        "armor": 2,
        "type": "ground"
    },
    "Orc": {
        "health": 60,
        "damage": 10,
        "armor": 5,
        "type": "ground"
    },
    "Troll": {
        "health": 100,
        "damage": 15,
        "armor": 8,
        "type": "ground"
    },
    "Harpy": {
        "health": 40,
        "damage": 7,
        "armor": 1,
        "type": "flying"
    },
    "Dragon": {
        "health": 200,
        "damage": 25,
        "armor": 12,
        "type": "flying"
    }
}

print("Current enemy stats:")
for enemy, stats in enemies.items():
    print(f"{enemy}: {stats}")

print("\n--- Damage Update Tool ---")
enemy_name = input("Enter the enemy name you want to adjust: ")

if enemy_name in enemies:
    try:
        new_damage = int(input(f"Enter new damage value for {enemy_name}: "))
        enemies[enemy_name]["damage"] = new_damage
        print(f"\n✅ {enemy_name}'s damage updated successfully!")
    except ValueError:
        print("⚠️ Please enter a valid number for damage.")
else:
    print("⚠️ Enemy not found.")

# Confirm updated dictionary
print("\nUpdated enemy stats:")
for enemy, stats in enemies.items():
    print(f"{enemy}: {stats}")
