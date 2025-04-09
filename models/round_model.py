class Round:
    """
    Defines a round in a tournament.

    ...

    Attributes
    ----------
    name : str
        Round's name
    number : int, optional
        Round's number, default to 1
    start_date : str, optional
        Round's starting date in DD/MM/YYYY HH/MM/SS format, defaults to None
    end_date : str, optional
        Round's ending date in DD/MM/YYYY HH/MM/SS format, defaults to None
    matches : list, optional
        Round's list of its matches, defaults to an empty list
    
    Methods
    -------
    round_json()
        Returns round data in JSON format.
    append_match(match)
        Adds match to the round's matches list.
    """

    def __init__(self, name : str) -> None:
        """
        Initializes a new round.

        Parameters
        ----------
        name : str
            Round's name

        Returns
        -------
        None
        """
        
        self.name = name
        self.number = 1
        self.start_date = None
        self.end_date = None
        self.matches = []

    def round_json(self) -> dict:
        """
        Returns round data in JSON format.

        Returns
        -------
        round : dict
            A dictionnary of the round for JSON format
        """

        round = {
            "name": self.name,
            "number": self.number,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": self.matches
        }

        return round
    
    def append_match(self, match) -> None:
        """
        Adds match to the round's matches list.

        Parameters
        ----------
        match : Match
            Represent a specific match.

        Returns
        -------
        None
        """

        self.matches.append(match)