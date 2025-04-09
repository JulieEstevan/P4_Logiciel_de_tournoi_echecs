class Match:
    """
    Defines a match in a round.

    ...

    Attributes
    ----------
    player1 : list
        The player one of a match, represent with a list of their name, score and national id.
    player2 : list
        The player two of a match, represent with a list of their name, score and national id.
    
    Methods
    -------
    match_json()
        Returns the match data in JSON format.
    """

    def __init__(self, player1_name: str, player1_score: float, player1_national_id, player2_name: str, player2_score: float, player2_national_id) -> None:
        """
        Initializes a new match

        Parameters
        ----------
        player1_name : str
            Player one's name
        player1_score : float
            Player one's score/points
        player1_national_id
            Player one's national id
        player2_name : str
            Player two's name
        player2_score : float
            Player two's score/points
        player2_national_id
            Player two's national id

        Returns
        -------
        None
        """
        
        self.player1 = [player1_name, player1_score, player1_national_id]
        self.player2 = [player2_name, player2_score, player2_national_id]

    def __str__(self) -> str:
        """
        Returns a string representation of the match.

        Returns
        -------
        self : str
            A string representation of the match.
        """
        
        return f"{self.player1[0]} (Score: {self.player1[1]}) contre {self.player2[0]} (Score: {self.player2[1]})"
    
    def match_json(self) -> dict:
        """
        Returns the match data in JSON format.
        
        Returns
        -------
        match : dict
            A dictionnary of the match for JSON format
        """

        match = {
            "player1": [
                self.player1[0], self.player1[1]
            ],
            "player2": [
                self.player2[0], self.player2[1]
            ]
        }
        
        return match