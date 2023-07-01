class Poultry :
    def __init__(self,sound,color,species):
        self.sound = sound
        self.color = color
        self.species = species
    def make_sound(self):
        print(f"quake like {self.sound}")
    def show_boddy(self):
        print(f"{self.color} {self.species}")
        

class Duck(Poultry) :
    def __init__(self,sound,color):
        super().__init__(sound,color)
    
    def duckquake(self):
        print(f"{self.color} duck quake like {self.sound}")

if __name__ == "__main__":
    Bd = Duck("quakkkke","blue")
    Rd = Duck("Dukkkke","red")