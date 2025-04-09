class MatchView:
    """
    Displays matches information and messages for interact with the user and giving them specific info.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    display_matches(match : Match)
        Displays a match in string format to the user.
    requested_score(match : Match)
        Asks user for the players score, returns user's choice.
    display_message(message : str)
        Displays a customizable message for the user.
    """

    @staticmethod
    def display_matches(match) -> None:
        """
        Displays a match in string format to the user.

        Parameters
        ----------
        match : Match
            A specific match.

        Returns
        -------
        None
        """

        print(f"\n--- Match --- {match.player1[0]} contre {match.player2[0]}")

    @staticmethod
    def requested_score(match) -> str:
        """
        Asks user for the players score, returns user's choice.

        Parameters
        ----------
        match : Match
            A specific match.

        Returns
        -------
        input : str
            User's choice.
        """

        return input(
            f"\nQui a gagné ? (1 pour {match.player1[0]}, 2 pour {match.player2[0]}, N pour match nul) : "
        )

    @staticmethod
    def display_message(message) -> None:
        """
        Displays a customizable message for the user.

        Parameters
        ----------
        message : str
            A message to display.

        Returns
        -------
        None
        """

        print(message)
