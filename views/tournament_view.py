class TournamentView:

    def __init__(self):
        pass

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