# Facade SubSystems
import time


# Subsistema 1
class PartyRoom:
    def __init__(self):
        self.available = True
        print("Party Room :: Salão de festa contactado!\n\n")

    def schedule(self):
        if self.available:
            print("Party Room :: Salão agendado!\n\n")
        self.available = False
        time.sleep(0.5)


# Subsistema 2
class Florist:
    def __init__(self):
        print("Florist :: Florista contratado!\n\n")

    @staticmethod
    def make_the_decoration():
        print("Florist :: Flores preparadas e montadas!\n\n")
        time.sleep(0.5)


# Subsistema 3
class Restaurant:
    def __init__(self):
        print("Restaurant :: Comida para eventos!\n\n")

    @staticmethod
    def prepare():
        print("Restaurant :: Comidas de diferentes variedades preparadas e serão servidas!\n\n")
        time.sleep(0.5)


# Subsistema 4
class Banda:
    def __init__(self):
        print("Banda :: Musicais para eventos!\n\n")

    @staticmethod
    def prepare_presentation():
        print("Banda :: Palco preparado para o show no evento!\n\n")
        time.sleep(0.5)
