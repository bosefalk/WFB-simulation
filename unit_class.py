# Defines the characterstics of a unit
# Currently has models, WS, S, T, Sv (armour save) and Ld (leadership)
# Create a basic orc unit using orc = Unit(WS = 3, S = 4, T = 3, Sv = 6)
# Then you can use orc.WS for their weapon skill etc

class Unit:

    def __init__(self, models, WS, S, T, Sv, Ld):
        self.models = models
        self.WS = WS
        self.S = S
        self.T = T
        self.Sv = Sv
        self.Ld = Ld

