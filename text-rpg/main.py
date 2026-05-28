import random

player_health = 100
enemy_health = 100

while player_health > 0 and enemy_health > 0:
    
    action = input("Choose your action: attack, defend or heal: ").lower()

    if action == "attack":
        player_attack = random.randint(0, 100)
        enemy_health = max(0, enemy_health - player_attack)
        print(f"You attacked for {player_attack} damage! Enemy health: {enemy_health}")
        
        if enemy_health > 0:
            enemy_attack = random.randint(0, 100)
            player_health = max(0, player_health - enemy_attack)
            print(f"Enemy attacked for {enemy_attack} damage! Player health: {player_health}")


    elif action == "defend":
        enemy_attack = random.randint(0, 50)
        player_health = max(0, player_health - enemy_attack)
        print(f"Enemy attacked for {enemy_attack} damage! Player health: {player_health}")

        counter = random.randint(1, 30)
        enemy_health = max(0, enemy_health - counter)
        print(f"You countered for {counter} damage! Enemy health: {enemy_health}")
    
    elif action == "heal":
        healing = random.randint(10, 40)
        player_health = min(100, player_health + healing)
        print(f"You healed for {healing}! Player health {player_health}")

        enemy_attack = random.randint(0, 100)
        player_health = max(0, player_health -enemy_attack)
        print(f"Enemy attacked for {enemy_attack} damage! Player health: {player_health}")


    else:
        print("Invalid action! Please choose attack, defend or heal.")


if player_health > enemy_health:
    print(f"You win! You finished with {player_health} health remaining.")

else:
    print(f"You lose! The enemy finished with {enemy_health} health remaining.")

"""
Could be expanded further by adding things like: 
Multiple enemies with different health and attack ranges
Different weapons the player can choose from
A level system where the player gets stronger after winning
"""
