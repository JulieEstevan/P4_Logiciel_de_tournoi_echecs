import re

class InputValidator:

    def string_input_validator(self, prompt):
        
        string_format = "[a-zA-Z]"
        value = input(prompt)
        
        while not re.match(string_format, value):
            print("Format incorrect, les chiffres et texte vide sont refuse")
            value = input(prompt)
        return value
    
    def date_input_validator(self, prompt):

        value = input(prompt)
        date_format = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"

        while not re.match(date_format, value):
            print("Format de la date incorrect")
            value = input(prompt)
        return value
    
    def id_input_validator(self, prompt):

        id_format = re.compile(r"[A-Z]{2}\d{5}$")
        value = input(prompt)

        while not re.match(id_format, value):
            print("Format de l'ID incorrect")
            value = input(prompt)
        return value
    
    def float_input_validator(self, prompt):

        float_format = "[+]?([0-9]+([.][0-9]*)?|[.][0-9]+)"
        value = input(prompt)

        while not re.match(float_format, value):
            print("Format incorrect, veuillez entrer un ou plusieurs chiffres")
            value = input(prompt)
        return float(value)