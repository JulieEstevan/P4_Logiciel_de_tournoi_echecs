class RoundView:

    @staticmethod
    def display_rounds(round):

        print(f"\n--- {round["name"]} ---\n")
        print(f"• Debut : {round["start_date"]}")
        print(f"• Fin : {round["end_date"]}")
        print("\n--- Matchs ---\n")

    @staticmethod
    def display_round_matches(match):

        print(f"• {match["player1"][0]} (Score: {match["player1"][1]}) contre {match["player2"][0]} (Score: {match["player2"][1]})")
