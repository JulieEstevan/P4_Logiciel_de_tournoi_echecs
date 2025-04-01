from models.round_model import Round
from models.player_model import Player
import os
from datetime import datetime
from tinydb import TinyDB, Query

class Tournament:
    """
    Defines a tournament.

    ...

    Attributes
    ----------
    name : str
        Tournament's name
    location : str
        Tournament's location
    start_date : str, optional
        Tournament's starting date in DD/MM/YYYY format, defaults to None
    end_date : str, optional
        Tournament's ending date in DD/MM/YYYY format, defaults to None
    number_of_rounds : int
        Tournament's number of rounds in total, defaults to 4
    current_round : int, optional
        Tournament's current round playing, defaults to 0
    rounds : list, optional
        Tournament's rounds list, defaults to an empty list
    players : list, optional
        Tournament's participating players list, defaults to an empty list
    description : str, optional
        Tournament's brief description, defaults to an empty string
    pairs_already_played : list, optional
        Tournament's list of players pairs that already played together in the tournament, defaults to an empty set

    Methods
    -------
    tournament_json()
        Returns tournament data in a JSON format.
    add_player(player: Player)
        Adds a player in the tournament's players list.
    add_round(round_instance: Round)
        Adds a round in the tournament's rounds list.
    get_ranking()
        Returns a sorted list of the players in the tournaments based on theirs points.
    end_tournament()
        End the tournament by adding the end date in the tournament data.
    tournament_db()
        Returns the access of the tournaments table.
    save_tournament(tournament: dict)
        Save the tournament info into the tournaments table.
    load_tournaments()
        Returns a list of all the tournaments from the tournaments table.
    """

    def __init__(self, name: str, location: str, number_of_rounds: int = 4) -> None:
        """
        Initializes a new tournament.

        Parameters
        ----------
        name : str
            Tournament's name
        location : str
            Tournament's location
        number_of_rounds : int
            Tournament's number of rounds in total, defaults to 4
        
        Returns
        -------
        None
        """
        
        self.name = name
        self.location = location
        self.start_date = None
        self.end_date = None
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.description = str("")
        self.pairs_already_played = []

    def tournament_json(self) -> dict:
        """
        Returns tournament data in a JSON format.

        Returns
        -------
        tournament_json : dict
            A dictionnary in JSON format
        """

        tournament_json = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "rounds": self.rounds,
            "players": self.players,
            "description": self.description,
            "pairs_already_played": self.pairs_already_played
        }

        return tournament_json
    
    def add_player(self, player) -> None:
        """
        Adds a player in the tournament's players list.

        Parameters
        ----------
        player : Player
            Player to add in the players list

        Returns
        -------
        None
        """

        self.players.append(player)

    def add_round(self, tournament) -> None:
        """
        Adds a round in the tournament's rounds list.

        Parameters
        ----------
        round_instance : Round
            Round to add in the round list

        Returns
        -------
        None
        """

        self.tournaments_db().update({"rounds" : self.rounds}, Query().name == tournament.name)
        self.tournaments_db().update({"pairs_already_played" : self.pairs_already_played}, Query().name == tournament.name)
        self.tournaments_db().update({"current_round" : self.current_round})
        

    def get_ranking(self) -> list:
        """
        Returns a sorted list of the players in the tournaments based on theirs points.

        Returns
        -------
        ranking : list
            The tournament's players list sorted by theirs points
        """

        ranking = sorted(
            self.players, key=lambda player: player.points, reverse=True
        )

        return ranking
    
    def end_tournament(self) -> None:
        """
        End the tournament by adding the end date in the tournament data.

        Returns
        -------
        None
        """

        self.end_date = datetime.now().strftime("%d/%m/%Y")
    
    @classmethod
    def tournaments_db(cls) -> TinyDB:
        """
        Returns the access of the tournaments table.

        Returns
        -------
        tournaments_table : Table
            Tournaments table using TinyDB
        """

        directory = os.path.dirname("data/tournaments.json")
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Database creation for tournaments data
        cls.db = TinyDB("data/tournaments.json", indent=4, ensure_ascii=False, encoding="utf-8")
        tournaments_table = cls.db.table("tournaments")

        return tournaments_table

    @classmethod
    def save_tournament(cls, tournament: dict) -> None:
        """
        Save the tournament info into the tournaments table.

        Parameters
        ----------
        tournament : dict
            Tournament's info turned into JSON format

        Returns
        -------
        None
        """

        cls.tournaments_db().insert(tournament)

    @classmethod
    def load_tournaments(cls) -> list:
        """
        Returns a list of all the tournaments from the tournaments table.

        Returns
        -------
        tounaments_data : list
            List of all the tournaments
        """

        tournaments_data = cls.tournaments_db().all()

        return tournaments_data