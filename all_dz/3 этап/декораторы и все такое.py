class Animal:
    species = []
    def __init__(self, name):
        self.name = name
        self.species.append(name)



    @classmethod
    def add_species(cls, species_name):
        if species_namea not in cls.species:
            cls.species.append(species_name)
        else:
            print(f"Вид '{species_name}' уже есть в реестре!")


    @classmethod
    def show_species(cls):
        return cls.species


