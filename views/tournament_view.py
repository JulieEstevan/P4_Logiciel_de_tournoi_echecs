class TournamentView:
    """
    Displays tournaments information and messages for interact with the user and giving them specific info.

    ...

    Attributes
    ----------
    None
    
    Methods
    -------
    request_tournament_info()
        Asks the user for tournament info and returns them in a tuple.
    display_players_list_by_index(players : list)
        Displays the tournament's players list with an index to the user.
    choice_for_players_to_add()
        Asks the user to choose a player, or multiple players, to add to tournament's players list.
    display_tournament_list_by_index(tournaments : list)
        Displays all the tournaments in a list with index to the user.
    tournaments_list(tournaments : list)
        Displays all the tournaments with their basic info to the user.
    choice_for_tournament_to_start()
        Asks the user to choose a tournament to start it.
    requested_tournament_description()
        Asks the user to type the tournament's description.
    tournament_summary(tournament : Tournament)
        Displays the tournament's summary for the user.
    display_message(message: str)
        Displays a customizable message to the user.
    """

    @staticmethod
    def request_tournament_info() -> tuple:
        """
        Asks user for tournament info and returns them in a tuple.

        Returns
        -------
            name, location, number_of_rounds : tuple
                Tournament's informations in a tuple form.
        """

        name: str = input("Nom du tournoi: ")
        location: str = input("Lieu du tournoi: ")
        number_of_rounds: int = input("Nombre de tours: ")

        return name, location, number_of_rounds
    
    @staticmethod
    def display_players_list_by_index(players : list) -> None:
        """
        Displays the tournament's players list with an index to the user.

        Parameters
        ----------
        players : list

        Returns
        -------
        None
        """

        for index, player in enumerate(players, start=1):
            print(f"{index}. {player.last_name} {player.first_name} (ID national: {player.national_id})")

    @staticmethod
    def choice_for_players_to_add() -> str:
        """
        Asks the user to choose a player, or multiple players, to add to tournament's players list.

        Returns
        -------
        choice : str
            User's choice
        """

        choice: str = input("Entrez les numéros des joueurs à ajouter (par exemple, 1,3,5 ou 't' pour terminer) : ")

        return choice
    
    @staticmethod
    def display_tournament_list_by_index(tournaments : list) -> None:
        """
        Displays all the tournaments in a list with index to the user.

        Parameters
        ----------
        tournaments : list
            List of all the tournaments

        Returns
        -------
        None
        """

        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name}")

    @staticmethod
    def tournaments_list(tournaments : list) -> None:
        """
        Displays all the tournaments with their basic info to the user.

        Parameters
        ----------
        tournaments : list
            List of all the tournaments

        Returns
        -------
        None
        """

        print("\n------ Liste des Tournois ------\n")
        for tournament in tournaments:
            if not tournament["start_date"] and not tournament["end_date"]:
                print(f"• {tournament["name"]} à {tournament["location"]} (À venir ...)")
            elif tournament["start_date"] and not tournament["end_date"]:
                print(f"• {tournament["name"]} à {tournament["location"]} demarré le {tournament["start_date"]} (En cours ...)")
            else:
                print(f"• {tournament["name"]} à {tournament["location"]} du {tournament["start_date"]} au {tournament["end_date"]}")

    @staticmethod
    def choice_for_tournament_to_start() -> str:
        """
        Asks the user to choose a tournament to start it.

        Returns
        -------
        input : str
            User's choice
        """

        return input("Entrez le numéro du tournoi à sélectionner (ou 'retour' pour revenir au menu principal : ")
    
    @staticmethod
    def requested_tournament_description() -> str:
        """
        Asks the user to type the tournament's description.

        Returns
        -------
        input : str
            User's text for the description.
        """

        return input(f"Entrez la description du tournoi :")
    
    @staticmethod
    def tournament_summary(tournament) -> None:
        """
        Displays the tournament's summary for the user.

        Parameters
        ----------
        tournament : Tournament
            A specific tournament.

        Returns
        -------
        None
        """

        print("\n---- Récapitulatif du tournoi ----\n")
        print(f"Le tournoi -- {tournament.name} -- se déroulant à {tournament.location} a débuté le {tournament.start_date} et s'est termine le {tournament.end_date}")
        print(f"C'était un tournoi en {tournament.number_of_rounds} tours, avec {len(tournament.players)} joueurs")
        print("\n---- Classement des joueurs ----\n")
        for index, player in enumerate(tournament.players, start=1):
            print(f"{index}. {player["last_name"]} {player["first_name"]} (Score: {player["points"]})")

    @staticmethod
    def display_message(message: str) -> None:
        """
        Displays a customizable message to the user.

        Parameters
        ----------
        message : str
            A message to display.

        Returns
        -------
        None
        """

        print(message)