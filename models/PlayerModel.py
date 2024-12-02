from tinydb import TinyDB, Query, where
import os
import json

class PlayerModel:

    def __init__(
        self,
        lastname: str,
        firstname: str,
        birth_date: str,
        national_id: str,
        points: float
    ) -> None:
        """Initialisation des donnees d'un joueur""" 

        self.lastname = lastname
        self.firstname = firstname
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = points

    def player_json_format(self):

        player_json = {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "points": self.points
            }
        return player_json

class PlayerManager:

    def __init__(self) -> None:

        self.db = TinyDB("data/players.json", indent=4, ensure_ascii=False, encoding="utf-8")
        self.players_table = self.db.table("players")

        if not os.path.exists("data/players.json"):
            """Creation du fichier JSON en cas d'inexistance de ce fichier"""
            with open("data/players.json", "w") as f:
                json.dump([], f)

    def add_player(self, lastname: str, firstname:str, birth_date: str, national_id: str, points: float):
        """Ajout d'un joueur dans la base de donnees"""

        player = PlayerModel(lastname, firstname, birth_date, national_id, points)

        existing_player = self.players_table.get(Query().national_id == national_id)
        if existing_player:
            print("Ce joueur existe deja dans la base de donnees")
            return

        self.players_table.insert(player.player_json_format())
        print(f"Le joueur {player.lastname} {player.firstname} a ete ajoute a la base de donnees")

    def update_player_points(self):
        """Mise a jour des points d'un joueur dans la base de donnees"""
        pass

    def players_list(self) -> list:
        """Creation d'une liste dans l'ordre alphabetique de tout les joueurs present dans la base de donnees"""
        players_data = self.players_table.all()
        players = []
        for player in players_data:
            player_model = PlayerModel(
                    player["lastname"],
                    player["firstname"],
                    player["birth_date"],
                    player["national_id"],
                    player["points"],
                )
            players.append(
                {"Nom" : player_model.lastname,
                 "Prenom" : player_model.firstname,
                 "Date de naissance" : player_model.birth_date,
                 "ID" : player_model.national_id,
                 "Points" : player_model.points,}
            )
        players = sorted(players, key=str)

        return players

    def get_player_by_id(self, national_id):
        """Recherche un joueur dans la base de donnees via son ID national d'echecs"""

        player = self.players_table.search(where("national_id") == national_id)
        if player:
            return player
        else:
            return None