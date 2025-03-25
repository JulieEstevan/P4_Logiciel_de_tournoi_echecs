from models.player_model import Player
from views.player_view import PlayerView

class PlayerController:
    """
    Manages all operations related to players.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    add_player()
        Retrieves player info from user's inputs for saving them, and if an error occured it displays an error message.
    display_players_list()
        Displays the list of all the players, if the list is empty it displays an error message.
    """

    @staticmethod
    def add_player() -> None:
        """
        Retrieves player info from user's inputs for saving them, and if an error occured it displays an error message.

        Returns
        -------
        None
        """

        try:
            last_name, first_name, birth_date, national_id = PlayerView.request_player_info()
            player = Player(last_name, first_name, birth_date, national_id)
            Player.save_player(player.player_json())
            PlayerView.display_player_added_successfully(last_name, first_name)
        except ValueError as e:
            PlayerView.display_error(e)

    @staticmethod
    def display_players_list() -> None:
        """
        Displays the list of all the players, if the list is empty it displays an error message.

        Returns
        -------
        None
        """

        players = []
        for player in Player.load_players():
            player_model = Player(
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["national_id"],
                )
            players.append(
                {"Nom" : player_model.last_name,
                 "Prenom" : player_model.first_name,
                 "Date de naissance" : player_model.birth_date,
                 "ID" : player_model.national_id,}
            )
        players = sorted(players, key=str)
        if players == []:
            PlayerView.display_error("Aucun.e joueur.euse n'a été enregistré")
        else:
            PlayerView.players_list(players)