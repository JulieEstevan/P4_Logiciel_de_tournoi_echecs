class RoundView:
    """
    Displays rounds information and messages for interact with the user and giving them specific info.

    ...

    Attributes
    ----------
    None
    
    Methods
    -------
    display_ranking(players : list)
        Displays the players ranking to the user.
    display_rounds(round : Round)
        Displays round's basic info to the user.
    display_round_matches(match : Match)
        Displays round's matches for the user.
    """

    @staticmethod
    def display_ranking(players) -> None:
        """
        Displays the players ranking to the user.

        Parameters
        ----------
        players : list
            Players list to display by ranking

        Raises
        ------
        

        Returns
        -------
        None
        """

        for index, player in enumerate(players, start=1):
            print(f"{index}. {player["last_name"]} {player["first_name"]} (Score: {player["points"]})")

    @staticmethod
    def display_rounds(round) -> None:
        """
        Displays round's basic info to the user.

        Parameters
        ----------
        round : Round
            A specific round

        Returns
        -------
        None
        """

        print(f"\n--- {round["name"]} ---\n")
        print(f"• Début : {round["start_date"]}")
        print(f"• Fin : {round["end_date"]}")
        print("\n--- Matchs ---\n")

    @staticmethod
    def display_round_matches(match) -> None:
        """
        Displays round's matches for the user.

        Parameters
        ----------
        match : Match
            A specific match

        Returns
        -------
        None
        """

        print(f"• {match["player1"][0]} (Score: {match["player1"][1]}) contre {match["player2"][0]} (Score: {match["player2"][1]})")