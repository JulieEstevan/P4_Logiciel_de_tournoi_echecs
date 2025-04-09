import os
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
    update_pairs_already_played(tournament : Tournament)
        Update the tournament's pairs already played in the tournament table.
    add_round(round_instance: Round)
        Adds a round in the tournament and updates it, and updates its current round in the tournaments table.
    update_players_score(player_points : float, player_id : str, tournament : Tournament)
        Updates the tournament's players score in the tournaments table.
    get_ranking(players : list)
        Returns a sorted list of the tournament's players list based on theirs points.
    start_tournament(tournament : Tournament)
        Starts the tournament by updating its start date and current round in the tournaments table.
    end_tournament(tournament : Tournament)
        End the tournament by updating its end date and description in the tournament table.
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
            A dictionnary of the tournament for JSON format
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

    def update_pairs_already_played(self, tournament) -> None:
        """
        Update the tournament's pairs already played in the tournament table.

        Parameters
        ----------
        tournament : Tournament
            A specific tournament

        Returns
        -------
        None
        """

        self.tournaments_db().update({"pairs_already_played" : self.pairs_already_played}, Query().name == tournament.name)

    def add_round(self, tournament) -> None:
        """
        Adds a round in the tournament and updates it, and updates its current round in the tournaments table.

        Parameters
        ----------
        tournament : Tournament
            A specific tournament

        Returns
        -------
        None
        """

        self.tournaments_db().update({"rounds" : self.rounds}, Query().name == tournament.name)
        self.tournaments_db().update({"current_round" : self.current_round}, Query().name == tournament.name)
        
    def update_players_score(self, player_points : float, player_id : str, tournament) -> None:
        """
        Updates the tournament's players score in the tournaments table.

        Parameters
        ----------
        player_points : float
            The point of the player
        player_id : str
            The national id of the player
        tournament : Tournament
            A specific tournament

        Returns
        -------
        None
        """

        for player in self.players:
            if player["national_id"] == player_id:
                player["points"] = player_points
        self.tournaments_db().update({"players" : self.players}, Query().name == tournament.name)

    def get_ranking(self, players : list) -> list:
        """
        Returns a sorted list of the players in the tournaments based on theirs points.

        Parameters
        ----------
        players : list
            List of the players to sort

        Returns
        -------
        ranking : list
            The tournament's players list sorted by theirs points
        """

        ranking = sorted(
            players, key=lambda player: player["points"], reverse=True
        )

        return ranking
    
    def start_tournament(self, tournament) -> None:
        """
        Starts the tournament by updating its start date and current round in the tournaments table.

        Parameters
        ----------
        tournament : Tournament
            A specific tournament

        Returns
        -------
        None
        """
    
        self.tournaments_db().update({"start_date" : self.start_date}, Query().name == tournament.name)
        self.tournaments_db().update({"current_round" : self.current_round}, Query().name == tournament.name)
    
    def end_tournament(self, tournament) -> None:
        """
        End the tournament by updating its end date and description in the tournament table.

        Parameters
        ----------
        tournament : Tournament
            A specific tournament

        Returns
        -------
        None
        """

        self.tournaments_db().update({"end_date" : self.end_date}, Query().name == tournament.name)
        self.tournaments_db().update({"description" : self.description}, Query().name == tournament.name)
    
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