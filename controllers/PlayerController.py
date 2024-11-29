from models.PlayerModel import PlayerManager
from views.PlayerView import PlayerView
from tinydb import Query

class PlayerController:
    
    def create_player_controller(self):

        player_view = PlayerView()
        lastname, firstname, birth_date, national_id, points = player_view.create_player_view()
        PlayerManager().add_player(lastname, firstname, birth_date, national_id, points)