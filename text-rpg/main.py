import random

player_health = 100
enemy_health = 100
is_defending = False

def roll(min_value, max_value):
    return random.randint(min_value, max_value)

def hp_bar(hp):
    bars = hp // 10
    return "█" * bars + "-" * (10 - bars)

while player_health > 0 and enemy_health > 0:

    # STATUS
    status = f"P [{hp_bar(player_health)}] {player_health:3}  |  E [{hp_bar(enemy_health)}] {enemy_health:3}"

    print("\n" + "=" * len(status))
    print(status)
    print("=" * len(status) + "\n")

    # PLAYER TURN
    print("--- Your turn ---")
    print("[A] Attack  [D] Defend  [H] Heal")
    action = input("Choose action: ").lower()

    if action in ["a", "attack"]:
        damage = roll(15, 60)

        if random.random() < 0.2:
            damage *= 2
            print("💥 CRITICAL HIT!")

        enemy_health = max(0, enemy_health - damage)
        print(f"You dealt {damage} damage!")

    elif action in ["d", "defend"]:
        is_defending = True
        print("🛡️ You prepare to defend...")

    elif action in ["h", "heal"]:
        heal = roll(10, 35)
        player_health = min(100, player_health + heal)
        print(f"✨ You healed {heal} HP!")

    else:
        print("Invalid action! Choose A, D, or H.")
        continue

    if enemy_health <= 0:
        break

    # ---------------- ENEMY TURN ----------------
    print("\n--- Enemy turn ---")

    # smarter healing logic: only if actually damaged
    enemy_missing_hp = 100 - enemy_health

    if enemy_missing_hp < 15:
        # almost full HP → never heal
        enemy_action = "attack"

    elif enemy_missing_hp < 30:
        # slightly hurt → small chance to heal
        enemy_action = random.choice(["attack", "attack", "heal"])

    else:
        # clearly damaged → more balanced behavior
        enemy_action = random.choice(["attack", "heal"])

    if enemy_action == "attack":
        damage = roll(10, 50)

        if random.random() < 0.15:
            damage *= 2
            print("⚠️ Enemy CRITICAL HIT!")

        if is_defending:
            damage //= 2
            print(f"🛡️ You blocked! Damage reduced to {damage}.")

        player_health = max(0, player_health - damage)
        print(f"Enemy dealt {damage} damage!")

    elif enemy_action == "heal":
        heal = roll(10, 30)
        enemy_health = min(100, enemy_health + heal)
        print(f"Enemy healed {heal} HP!")

    is_defending = False

# ---------------- END GAME ----------------
print("\n" + "=" * 30)

if player_health > 0:
    print("YOU WIN! 🎉")
else:
    print("YOU LOSE! 💀")

print(f"Final HP - Player: {player_health}, Enemy: {enemy_health}")
