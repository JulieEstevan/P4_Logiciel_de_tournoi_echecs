import re
import os
from tinydb import TinyDB

class Player:
    """
    Defines a player in a tournament.

    ...

    Attributes
    ----------
    last_name : str 
        Player's last name
    first_name : str
        Player's first name
    birth_date : str 
        Player's birth date
    national_id : str
        Player's national ID
    points : float, optional
        Player's points in a tournament
    
    Methods
    -------
    player_json()
        Returns player data in JSON format.
    players_db()
        Returns the access of the players table.
    save_player(player: dict)
        Save the player's info into the players table.
    load_players()
        Returns all the data in a list from players table.
    update_points(points: float)
        Updates the player's points.
    """

    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str) -> None:
        """
        Initializes a new player.

        Parameters
        ----------
        last_name : str 
            Player's last name
        first_name : str
            Player's first name
        birth_date : str 
            Player's birth date
        national_id : str
            Player's national ID

        Raises
        ------
        ValueError
            If the national ID or birth date format is invalid

        Returns
        -------
        None
        """

        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = 0.0   # Float number for potential half-points

        # Validation of the national ID format
        if not re.match(r'^[A-Z]{2}\d{5}$', self.national_id):
            raise ValueError("Format error, the national ID must be two letters followed by five digits (e.g., AB12345)")
        
        # Validation of the birth date format
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', self.birth_date):
            raise ValueError("Format error, the birth date must be in the format dd/mm/yyyy")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the player.

        Returns
        -------
        self : str
            A string that represent the player
        """

        return f"{self.last_name} {self.first_name} ({self.national_id})"
    
    def player_json(self) -> dict:
        """
        Returns player data in JSON format.

        Returns
        -------
        player_json : dict
            A dictionarry in JSON format
        """

        player_json = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "points": self.points
        }
        return player_json

    @classmethod
    def players_db(cls) -> TinyDB:
        """
        Returns the access of the players table.

        Returns
        -------
        players_table : Table
            Players table using TinyDB
        """

         # Directory and JSON file creation if it doesn't already exist
        directory = os.path.dirname("data/players.json")
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Database creation for players data
        cls.db = TinyDB("data/players.json", indent=4, ensure_ascii=False, encoding="utf-8")
        players_table = cls.db.table("players")

        return players_table

    @classmethod
    def save_player(cls, player: dict) -> None:
        """
        Save the player's info into the players table.

        Parameters
        ----------
        player : dict
            Player's info turned into JSON format
        
        Returns
        -------
        None
        """
        
        cls.players_db().insert(player)

    @classmethod
    def load_players(cls) -> list:
        """
        Returns all the data in a list from players table.

        Returns
        -------
        players_data : list
            List of all the players
        """

        players_data = cls.players_db().all()

        return players_data
    
    def update_points(self, points: float) -> None:
        """
        Updates the player's points.

        Parameters
        ----------
        points : float
            Player's points

        Returns
        -------
        None
        """

        self.points += points