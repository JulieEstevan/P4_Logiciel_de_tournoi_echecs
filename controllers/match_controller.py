from views.match_view import MatchView


class MatchController:
    """
    Manages the operations related to the matches.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    get_score(match)
        Update player(s) score depending on user choice.
    """

    def get_score(match) -> None:
        """
        Update player(s) score depending on user choice.

        Parameters
        ----------
        match : Match
            Represente a specific match.

        Returns
        -------
        None
        """
        choice = ""

        while choice not in ["1", "2", "n", "N"]:
            choice = MatchView.requested_score(match)

            if choice == "1":
                match.player1[1] += 1
            elif choice == "2":
                match.player2[1] += 1
            elif choice.lower() == "n":
                match.player1[1] += 0.5
                match.player2[1] += 0.5
            else:
                MatchView.display_message(
                    "Entrée invalide. Veuillez réessayer."
                )
