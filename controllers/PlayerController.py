from models.PlayerModel import PlayerModel
from views.PlayerView import PlayerView

class PlayerController:

    def create_player(self):

        player_view = PlayerView()
        lastname, firstname, birth_date, national_id = player_view.create_player()
        player = PlayerModel(lastname, firstname, birth_date, national_id)
        player.add_player()
