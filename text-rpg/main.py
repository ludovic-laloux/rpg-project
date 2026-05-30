import random

# ---------------- CONFIG ----------------
MAX_HP = 100

# ---------------- STATE ----------------
player_health = MAX_HP
enemy_health = MAX_HP
is_defending = False


# ---------------- UTILITY ----------------
def roll(min_value, max_value):
    return random.randint(min_value, max_value)


def hp_bar(hp):
    bars = hp // 10
    return "█" * bars + "-" * (10 - bars)


def show_status():
    status = (
        f"P [{hp_bar(player_health)}] {player_health:3}  |  "
        f"E [{hp_bar(enemy_health)}] {enemy_health:3}"
    )

    print("\n" + "=" * len(status))
    print(status)
    print("=" * len(status) + "\n")


# ---------------- PLAYER ----------------
def player_turn():
    global player_health, enemy_health, is_defending

    print("--- Your turn ---")
    print("[A] Attack  [D] Defend  [H] Heal")

    action = input("Choose action: ").lower()

    if action in ["a", "attack"]:
        damage = roll(15, 60)

        # critical hit (v3 feature)
        if random.random() < 0.2:
            damage *= 2
            print("💥 CRITICAL HIT!")

        enemy_health = max(0, enemy_health - damage)
        print(f"You dealt {damage} damage!")

    elif action in ["d", "defend"]:
        is_defending = True
        print("🛡️ You brace for impact...")

    elif action in ["h", "heal"]:
        heal = roll(10, 35)
        player_health = min(MAX_HP, player_health + heal)
        print(f"✨ You healed {heal} HP!")

    else:
        print("Invalid action!")
        return False

    return True


# ---------------- ENEMY AI ----------------
def enemy_choose_action():
    """Smarter v3-style logic but cleanly separated."""
    missing_hp = MAX_HP - enemy_health

    if missing_hp < 15:
        return "attack"
    elif missing_hp < 30:
        return random.choice(["attack", "attack", "heal"])
    else:
        return random.choice(["attack", "heal"])


def enemy_turn():
    global player_health, enemy_health, is_defending

    print("\n--- Enemy turn ---")

    action = enemy_choose_action()

    if action == "attack":
        damage = roll(10, 50)

        # enemy critical hit (v3 feature)
        if random.random() < 0.15:
            damage *= 2
            print("⚠️ Enemy CRITICAL HIT!")

        if is_defending:
            damage //= 2
            print(f"🛡️ You blocked! Damage reduced to {damage}.")

        player_health = max(0, player_health - damage)
        print(f"Enemy dealt {damage} damage!")

    elif action == "heal":
        heal = roll(10, 30)
        enemy_health = min(MAX_HP, enemy_health + heal)
        print(f"Enemy healed {heal} HP!")

    is_defending = False


# ---------------- GAME END ----------------
def end_game():
    print("\n" + "=" * 30)

    if player_health > 0:
        print("YOU WIN! 🎉")
    else:
        print("YOU LOSE! 💀")

    print(f"Final HP - Player: {player_health}, Enemy: {enemy_health}")


# ---------------- MAIN LOOP ----------------
while player_health > 0 and enemy_health > 0:

    show_status()

    if not player_turn():
        continue

    if enemy_health <= 0:
        break

    enemy_turn()


# ---------------- END ----------------
end_game()
