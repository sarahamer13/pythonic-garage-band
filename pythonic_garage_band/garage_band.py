class Band:
    instances = []  ### creating a class attribute (list) it will keep track of all instances in band class

    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members is not None else []
        Band.instances.append(self)

    def play_solos(self):    ### allows each member to play solo and return a list of their solos
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):  ### returns the list of all the created band instances
        return cls.instances

    def __str__(self):  ## string method
        return f"Band name: {self.name}"

    def __repr__(self): ## repr method to return a printable object by converting it to a string
        return f"Band(name='{self.name}', members={self.members})"
    
### Parent constructor
class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument
    
## classes below (3) inherited from the parent Musician to represent 3 types of Musicians
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")
      
    def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def play_solo(self):
        return "bom bom buh bom"
