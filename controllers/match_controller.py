from views.match_view import MatchView

class MatchController:

    def get_score(match):
        choice = MatchView.requested_score(match)

        if choice == "1":
            match.player1[1] += 1
        elif choice == "2":
            match.player2[1] += 1
        elif choice.lower() == "n":
            match.player1[1] += 0.5
            match.player2[1] += 0.5
        else:
            MatchView.displayer_message(
                "Entrée invalide. Veuillez réessayer."
            )