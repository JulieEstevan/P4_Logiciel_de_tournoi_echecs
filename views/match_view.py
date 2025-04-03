class MatchView:

    @staticmethod
    def display_matches(match, round):

        print(f"\n--- Match --- {match.player1[0]} contre {match.player2[0]}")

    @staticmethod
    def requested_score(match):

        return input(
            f"\nQui a gagné ? (1 pour {match.player1[0]}, 2 pour {match.player2[0]}, N pour match nul) : "
        )
    
    @staticmethod
    def displayer_message(message):

        print(message)