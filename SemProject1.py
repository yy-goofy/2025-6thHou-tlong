#Name:Tristan long
#Class: 6th Hour
#Assignment: Semester Project 1

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Lariat Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).
import random
partyDict = { "LaeZel" : {
        "HO" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadow-heart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}


enemyDict = { "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mind-flayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).

#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses


#3. If the attack hits, roll damage and subtract it from the target's hit points.


#4. The second in initiative rolls to attack (and rolls damage) afterwords.


#5. Repeat steps 2-5 until one of the characters is dead.

Shadow_heart_hp = 100
Dragon_hp = 100
player1_turn = True
game_running = True
print("Welcome to the 1v1 DND game")
print("Shadow_heart HP: [100] | Dragon HP: [100]\n")
while game_running:
    if player1_turn:
        input("Shadow_heart, press Enter to roll a d20...")
        roll = random.randint(1, 20)
        damage = roll  # Simple damage model: roll equals damage dealt
        print(f"Shadow_heart rolled a {roll} and deals {damage} damage!")
        Dragon_hp -= damage
        print(f"Dragon now has {Dragon_hp} HP remaining.\n")
        if Dragon_hp <= 0:
            print("Dragon has been defeated! Shadow_heart wins!")
            game_running = False
        else:
            player1_turn = False
    elif not player1_turn:
        input("Dragon, press Enter to roll a d20...")
        roll = random.randint(1, 20)
        damage = roll
        print(f"Dragon has rolled a {roll} and deals {damage} damage!")
        Shadow_heart_hp -= damage
        print(f"Shadow_heart now has {Shadow_heart_hp} HP remaining.\n")
        if Shadow_heart_hp <= 0:
            print("Player 1 has been defeated Player 2 wins")
            game_running = False
        else:
            player1_turn = True