from tabulate import tabulate
from typing import Any

class PlayerView:
    """
    Displays players information and messages for interact with the user.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    request_player_info
        Asks user for player info and returns them in a tuple.
    player_list(list: list)
        Show the list of all the players in a easy readible format.
    display_player_added_successfully()
        Displays a message to inform the user that the player has been successfully added.
    display_error(error: Any)
        Displays a message to inform the user that an error occured.
    """

    @staticmethod
    def request_player_info() -> tuple:
        """
        Asks user for player info and returns them in a tuple.

        Returns
        -------
            last_name, first_name, birth_date, national_id : tuple
                Player's informations in a tuple form.
        """

        last_name: str = input("Nom de famille: ")
        first_name: str = input("Prénom: ")
        birth_date: str = input("Date de naissance (jj/mm/aaaa): ")
        national_id: str = input("ID National (ex: AB12345): ")

        return last_name, first_name, birth_date, national_id
    
    @staticmethod
    def players_list(list: list) -> None:
        """
        Show the list of all the players in a easy readible format.

        Parameters
        ----------
        list : list
            Players list

        Returns
        -------
        None
        """
        print("\n------ Liste des Joueurs ------\n")
        print(tabulate(list, headers="keys"))
    
    @staticmethod
    def display_player_added_successfully(last_name: str, first_name: str) -> None:
        """
        Displays a message to inform the user that the player has been successfully added.

        Parameters
        ----------
        last_name : str
            Player's last name
        first_name : str
            Player's first name

        Returns
        -------
        None
        """

        print(f"Le.a joueur.euse {last_name} {first_name} a été ajouté avec succès")

    @staticmethod
    def display_error(error: Any) -> None:
        """
        Displays a message to inform the user that an error occured.

        Parameters
        ----------
        error : Any
            The specific error that occured

        Returns
        -------
        None
        """

        print(f"Erreur: {error}")