import re

class PlayerView:

    def create_player(self):
        lastname = input("Entrez le nom de famille : ")
        firstname = input("Entrez le prenom: ")
        birth_date = input("Entrez la date de naissance (JJ/MM/YYYY): ")
        date_format = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"
        while not re.match(date_format, birth_date):
            print("Format de la date incorrect")
            birth_date = input("Entrez la date de naissance (JJ/MM/AAAA): ")
        national_id = input("Entrez l'ID national d'echecs (AB12345): ")
        id_format = re.compile(r"[A-Z]{2}\d{5}$")
        while not re.match(id_format, national_id): # Si on se trompe une fois, la boucle bug et affiche une erreur a chaque input suivant
            print("Format de l'ID incorrect")
            birth_date = input("Entrez l'ID national d'echecs (AB12345): ")

        return lastname, firstname, birth_date, national_id