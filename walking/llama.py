from datetime import date


class Llama:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal with a default value
        self.walking = True
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
