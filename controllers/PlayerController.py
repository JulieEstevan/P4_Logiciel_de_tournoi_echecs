from models.PlayerModel import PlayerManager
from views.PlayerView import PlayerView

class PlayerController:
    
    def create_player_controller(self):

        player_view = PlayerView()
        lastname, firstname, birth_date, national_id, points = player_view.create_player_view()
        PlayerManager().add_player(lastname, firstname, birth_date, national_id, points)

    def players_list_controller(self):

        players = PlayerManager().players_list()
        player_view = PlayerView()
        player_view.players_list_view(players)
        