class MatchView:

    @staticmethod
    def requested_score(match):
        print(f"\n--- Match ---\n {match.player1[0]} contre {match.player2[0]}\n")
        return input(
            f"Qui a gagné ? (1 pour {match.player1[0]}, 2 pour {match.player2[0]}, N pour match nul) : "
        )
    
    @staticmethod
    def displayer_message(message):

        print(message)