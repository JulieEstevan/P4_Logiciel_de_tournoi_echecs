class Match:

    def __init__(self, player1_name: str, player1_score: float, player1_national_id, player2_name: str, player2_score: float, player2_national_id):
        
        self.player1 = [player1_name, player1_score, player1_national_id]
        self.player2 = [player2_name, player2_score, player2_national_id]

    def __str__(self):
        
        return f"{self.player1[0]} (Score: {self.player1[1]}) contre {self.player2[0]} (Score: {self.player2[1]})"
    
    def match_json(self):

        match = {
            "player1": [
                self.player1[0], self.player1[1]
            ],
            "player2": [
                self.player2[0], self.player2[1]
            ]
        }
        
        return match