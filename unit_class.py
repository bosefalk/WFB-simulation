# Defines the characterstics of a unit
# Currently has name, models, WS, S, T, Sv (armour save) and Ld (leadership)
# Create a basic orc unit using orc = Unit(WS = 3, S = 4, T = 3, Sv = 6)
# Then you can use orc.WS for their weapon skill etc

class Unit:

    def __init__(self, name, models, WS, S, T, I, Sv, Ld):
        self.name = name
        self.models = models
        self.WS = WS
        self.S = S
        self.T = T
        self.I = I
        self.Sv = Sv
        self.Ld = Ld

