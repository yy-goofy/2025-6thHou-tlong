





























import random


player1_hp = 100
player2_hp = 100
player1_turn = True
game_running = True
print("Welcome to the 1v1 D20 Dice Battle!")
print("Player 1 HP: [100] | Player 2 HP: [100]\n")
while game_running:
    if player1_turn:
        input("Player 1, press Enter to roll a d20...")
        roll = random.randint(1, 20)
        damage = roll
        print(f"Player 1 rolled a {roll} and deals {damage} damage!")
        player2_hp -= damage
        print(f"Player 2 now has {player2_hp} HP remaining.\n")
        if player2_hp <= 0:
            print("Player 2 has been defeated! Player 1 wins!")
            game_running = False
        else:
            player1_turn = False
    elif not player1_turn:
        input("Player 2, press Enter to roll a d20...")
        roll = random.randint(1, 20)
        damage = roll
        print(f"Player 2 rolled a {roll} and deals {damage} damage!")
        player1_hp -= damage
        print(f"Player 1 now has {player1_hp} HP remaining.\n")
        if player1_hp <= 0:
            print("Player 1 has been defeated! Player 2 wins!")
            game_running = False
        else:
            player1_turn = True

