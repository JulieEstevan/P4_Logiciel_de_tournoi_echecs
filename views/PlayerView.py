import re
from utils.InputValidator import InputValidator

class PlayerView:

    def create_player_view(self):
        """Demande a l'utilisateur les information du joueur et retourne les valeurs entrees"""

        valid_input = InputValidator()

        lastname = valid_input.string_input_validator("Entrez le nom de famille: ")
        firstname = valid_input.string_input_validator("Entrez le prenom: ")
        birth_date = valid_input.date_input_validator("Entrez la date de naissance (JJ/MM/AAAA): ")
        national_id = valid_input.id_input_validator("Entrez l'ID national d'echecs (AB12345): ")
        points = valid_input.float_input_validator("Entrez le nombre de point: ")
        

        return lastname, firstname, birth_date, national_id, points