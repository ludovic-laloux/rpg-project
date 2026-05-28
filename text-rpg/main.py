import random

player_health = 100
enemy_health = 100
is_defending = False

def roll(min_value, max_value):
    return random.randint(min_value, max_value)

while player_health > 0 and enemy_health > 0:

    # STATUS
    status = f"PLAYER HP {player_health:3} ENEMY HP {enemy_health:3}"

    print("\n" + "=" * len(status))
    print(status)
    print("=" * len(status) + "\n")

    # PLAYER TURN
    print("--- Your turn ---")
    action = input("Choose action (A Attack, D Defend, H Heal): ").lower()

    if action == "a":
        damage = roll(20, 100)
        enemy_health = max(0, enemy_health - damage)
        print(f"You dealt {damage} damage!")

    elif action == "d":
        is_defending = True
        print("You prepare to defend...")

    elif action == "h":
        heal = roll(10, 40)
        player_health = min(100, player_health + heal)
        print(f"You healed {heal} HP!")

    else:
        print("Invalid action!")
        continue

    # stop if enemy is dead
    if enemy_health <= 0:
        break

    # ---------------- ENEMY TURN ----------------
    print("\n--- Enemy turn ---")

    # Step 1: decide action
    if enemy_health < 30:
        enemy_action = random.choice(["heal", "attack"])
    else:
        enemy_action = random.choice(["attack", "attack", "heal"])

    # Step 2: execute action
    if enemy_action == "attack":
        damage = roll(10, 80)

        if is_defending:
            damage //= 2
            print(f"You blocked it! Damage reduced to {damage}.")

        player_health = max(0, player_health - damage)
        print(f"Enemy dealt {damage} damage!")

    elif enemy_action == "heal":
        heal = roll(10, 40)
        enemy_health = min(100, enemy_health + heal)
        print(f"Enemy healed {heal} HP!")

    # reset defense after enemy turn
    is_defending = False

# ---------------- END GAME ----------------
print("\n==============================")

if player_health > 0:
    print("YOU WIN! 🎉")
else:
    print("YOU LOSE! 💀")

print(f"Final HP - Player: {player_health}, Enemy: {enemy_health}")
