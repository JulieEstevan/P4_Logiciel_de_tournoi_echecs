class Round:

    def __init__(self, name):
        
        self.name = name
        self.number = 1
        self.start_date = None
        self.end_date = None
        self.matches = []

    def round_json(self):

        round = {
            "name": self.name,
            "number": self.number,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": self.matches
        }

        return round
    
    def append_match(self, match):

        self.matches.append(match)