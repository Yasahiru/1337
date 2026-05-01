def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set = {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    Achievement_analytics(alice, bob, charlie)


def Achievement_analytics(alice: set, bob: set, charlie: set) -> None:
    print("=== Achievement Analytics ===")
    unique_achievements: set = alice.union(bob.union(charlie))

    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    common_for_players = alice.intersection(bob.intersection(charlie))

    shared_achievements = (alice.intersection(bob).union(
        bob.intersection(charlie))).union(charlie.intersection(alice))

    rare_achievements = unique_achievements.difference(shared_achievements)

    print(f"Common to all players: {common_for_players}")
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main() -> None:
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
