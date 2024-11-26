from tinydb import TinyDB, Query
import os
import json
import datetime

class PlayerModel:

    # Ajouter les lignes 9-15 dans le __init__ ?
    db = TinyDB("data/players.json", indent=4, encoding="utf-8")
    players_table = db.table("players")
    if not os.path.exists("data/players.json"):
            """Creation du fichier JSON en cas d'inexistance de ce fichier"""

            with open("data/players.json", "w") as f:
                json.dump([], f)

    def __init__(
        self,
        lastname: str,
        firstname: str,
        birth_date: datetime,
        national_id: str,
        points: float = 0
    ) -> None:
        """Initialisation des donnees d'un joueur""" 

        self.lastname = lastname
        self.firstname = firstname
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = points

    def add_player(self):
        """Ajout d'un joueur dans la base de donnees"""
        
        self.players_table.insert(
            {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "points": self.points
            }
        )

    def update_player(self):
        """Mise a jour des informations d'un joueur dans la base de donness"""
        pass

    def players_list(self):
        """Creation d'une liste regroupant tout les joueurs present dans la base de donnees"""
        pass
    
    def get_player_by_id(self):
        """Recherche un joueur dans la base de donnees via son ID national d'echecs"""
        pass