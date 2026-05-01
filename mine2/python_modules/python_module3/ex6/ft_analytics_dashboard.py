def list_comprehensions() -> int:
    players: list[str] = ["alice", "bob", "charlie", "diana"]
    scores_list: list[int] = [2300, 1800, 2150, 2500]
    active_status: list[bool] = [True, True, True, False]
    total_players = len(players)

    print("=== List Comprehension Examples ===")
    high_scores: list[str] = []
    for score in range(len(scores_list)):
        if (scores_list[score] > 2000):
            high_scores.append(players[score])

    for score in range(len(scores_list)):
        scores_list[score] *= 2

    active_players: list[str] = []
    for status in range(len(active_status)):
        if (active_status[status] is True):
            active_players.append(players[status])
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_list}")
    print(f"Active players: {active_players}\n")
    return (total_players)


def dict_comprehensions(average_score: list[any]) -> None:
    players: list[str] = ["alice", "bob", "charlie"]
    scores: list[str] = [2300, 1800, 2150]
    achievements: list[str] = [5, 3, 7]

    player_scores: dict[str, int] = {
        players[i]: scores[i] for i in range(len(players))
    }
    score_categories: dict[str, int] = {
        "high": 3,
        "medium": 2,
        "low": 1
    }
    players_achievements: dict[str, int] = {
        players[i]: achievements[i] for i in range(len(players))
    }
    avg_score: float = sum(scores) / len(scores)
    average_score.append(players[0])
    average_score.append(round(avg_score, 2))
    average_score.append(scores[0])
    average_score.append(achievements[0])

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {players_achievements}\n")


def set_comprehensions() -> int:
    data: dict[str, any] = [
        {
            "player": "alice",
            "achievements": "first_kill",
            "regions": "north"
        },
        {
            "player": "alice",
            "achievements": "level_10",
            "regions": "east"
        },
        {
            "player": "alice",
            "achievements": "boss_slayer",
            "regions": "west"
        },
        {
            "player": "alice",
            "achievements": "first_kill",
            "regions": "south"
        },
        {
            "player": "bob",
            "achievements": "boss_slayer",
            "regions": "central"
        },
        {
            "player": "bob",
            "achievements": "first_kill",
            "regions": "north"
        },
        {
            "player": "bob",
            "achievements": "level_10",
            "regions": "east"
        },
        {
            "player": "bob",
            "achievements": "boss_slayer",
            "regions": "west"
        },
        {
            "player": "charlie",
            "achievements": "first_kill",
            "regions": "south"
        },
        {
            "player": "charlie",
            "achievements": "level_10",
            "regions": "central"
        },
        {
            "player": "charlie",
            "achievements": "boss_slayer",
            "regions": "north"
        },
        {
            "player": "diana",
            "achievements": "first_kill",
            "regions": "west"
        },
        {
            "player": "diana",
            "achievements": "boss_slayer",
            "regions": "central"
        }
    ]

    players: list[str] = []
    for value in data:
        players.append(value["player"])
    set_players: set[str] = set(players)

    achievements: list[str] = []
    for value in data:
        achievements.append(value["achievements"])
    set_achievements: set[str] = set(achievements)

    regions: list[str] = []
    for value in data:
        regions.append(value["regions"])
    set_regions: set[str] = set(regions)

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {set_players}")
    print(f"Unique achievements: {set_achievements}")
    print(f"Active regions: {set_regions}\n")

    total_unique_achievemnts: int = len(achievements)
    return (total_unique_achievemnts)


def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===\n")
    total_players: int = 0
    total_unique_achievemnts: int = 0
    average_score: list[int] = []

    total_players = list_comprehensions()
    dict_comprehensions(average_score)
    total_unique_achievemnts = set_comprehensions()

    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievemnts}")
    print(f"Average score: {average_score[1]}")
    print(f"Top Performer: {average_score[0]}"
          f" ({average_score[2]} points, {average_score[3]} achievements)")


def main() -> None:
    ft_analytics_dashboard()


if __name__ == "__main__":
    main()
