class TournamentView:

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
    def display_players_list_by_index(players) -> None:

        for index, player in enumerate(players, start=1):
            print(f"{index}. {player.last_name} {player.first_name} (ID national: {player.national_id})")

    @staticmethod
    def choice_for_players_to_add():

        choice: str = input("Entrez les numéros des joueurs à ajouter (par exemple, 1,3,5 ou 't' pour terminer) : ")

        return choice
    
    @staticmethod
    def display_tournament_list_by_index(tournaments):
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name}")

    @staticmethod
    def tournaments_list(tournaments):

        print("\n------ Liste des Tournois ------\n")
        for tournament in tournaments:
            if not tournament["end_date"]:
                print(f"• {tournament["name"]} à {tournament["location"]}")
            else:
                print(f"• {tournament["name"]} à {tournament["location"]} du {tournament["start_date"]} au {tournament["end_date"]}")

    @staticmethod
    def choice_for_tournament_to_start():
        return input("Entrez le numéro du tournoi à sélectionner (ou 'retour' pour revenir au menu principal : ")
    
    @staticmethod
    def requested_tournament_description():
        return input(f"Entrez la description du tournoi :")
    
    @staticmethod
    def tournament_summary(tournament):
        print("\n---- Récapitulatif du tournoi ----\n")
        print(f"Le tournoi -- {tournament.name} -- se deroulant a {tournament.location} a debute le {tournament.start_date} et s'est termine le {tournament.end_date}")
        print(f"C'etait un tournoi en {tournament.number_of_rounds} tours, avec {len(tournament.players)} joueurs")
        print("\n---- Classement des joueurs ----\n")
        for index, player in enumerate(tournament.players, start=1):
            print(f"{index}. {player["last_name"]} {player["first_name"]} (Score: {player["points"]})")

    @staticmethod
    def display_message(message: str) -> None:
        """
        Displays a message to inform the user that the tournament has been successfully added.

        Parameters
        ----------
        name : str
            Tounament's name

        Returns
        -------
        None
        """

        print(message)