import random

player_health = 100
enemy_health = 100
is_defending = False


def roll(min_value, max_value):
    return random.randint(min_value, max_value)


def show_status():
    status = f"PLAYER HP {player_health:3} ENEMY HP {enemy_health:3}"
    print("\n" + "=" * len(status))
    print(status)
    print("=" * len(status) + "\n")


def player_turn():
    global player_health, enemy_health, is_defending

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
        print("Invalid action")
        return False

    return True


def enemy_turn():
    global player_health, enemy_health, is_defending

    print("\n--- Enemy turn ---")

    # decide action
    if enemy_health < 30:
        enemy_action = random.choice(["heal", "attack"])
    else:
        enemy_action = random.choice(["attack", "attack", "heal"])

    # execute action
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

    is_defending = False


def end_game():
    print("\n" * 30)

    if player_health > 0:
        print("YOU WIN! 🎉")
    else:
        print("YOU LOSE! 💀")

    print(f"Final HP - Player: {player_health}, Enemy: {enemy_health}")


# ---------------- MAIN GAME LOOP ----------------

while player_health > 0 and enemy_health > 0:

    show_status()

    action_valid = player_turn()

    if not action_valid:
        continue

    if enemy_health <= 0:
        break

    enemy_turn()

# ---------------- END GAME ----------------
end_game()
