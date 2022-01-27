# Facade
from context.subsystems import Banda, Florist, Restaurant, PartyRoom


class EventOrganizer:
    def __init__(self):
        print("Event Organizer :: Iniciado o Gerenciamento do Evento!\n\n")

    @staticmethod
    def organize():
        party_room = PartyRoom()
        party_room.schedule()

        restaurant = Restaurant()
        restaurant.prepare()

        florist = Florist()
        florist.make_the_decoration()

        banda = Banda()
        banda.prepare_presentation()


class Client:
    def __init__(self):
        print("Client :: Existente!\n\n")

    @staticmethod
    def to_hire():
        print("Client :: Contratou o Gerenciador de Eventos!\n\n")

        event_organizer = EventOrganizer()
        event_organizer.organize()

    def __del__(self):
        print("Client :: Evento encerrado e Cliente satisfeito!")

