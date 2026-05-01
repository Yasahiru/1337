from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    platform_status: bool = False

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack(card2):
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        self.matches_played += 1

        winner = self.cards[0]
        looser = self.cards[1]

        winner.update_wins(1)
        looser.update_losses(1)

        self.register_card(winner)
        self.register_card(looser)

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        self.platform_status = False
        leaderboard = []
        card1_rating = self.cards[0].calculate_rating()
        card2_rating = self.cards[1].calculate_rating()
        if (card1_rating > card2_rating):
            leaderboard.append(self.cards[0])
            leaderboard.append(self.cards[1])
        else:
            leaderboard.append(self.cards[1])
            leaderboard.append(self.cards[0])
        return (leaderboard)

    def generate_tournament_report(self) -> dict:
        total = 0
        for card in self.cards.values():
            total += card.rating
        avg_rating = total / len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": self.platform_status,
        }
