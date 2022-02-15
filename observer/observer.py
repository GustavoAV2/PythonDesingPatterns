from abc import ABCMeta, abstractmethod


# Assuntos/Tópico
class AgenciaNoticia:

    def __init__(self):
        self.__followers = []
        self.__last_news = []

    def __repr__(self):
        return "::Objeto::"

    def subscribes(self, observer):
        self.__followers.append(observer)

    def unsubscribe(self, follower=None):
        if not follower:
            self.__followers.pop()
        else:
            return self.__followers.remove(follower)

    def notify_everyone(self, *args, **kwargs):
        for observer in self.__followers:
            observer.notify()

    def adding_news(self, news):
        self.__last_news = news

    def view_news(self):
        return f"Urgente {self.__last_news}"

    @property
    def followers(self):
        return [type(follower).__name__ for follower in self.__followers]


class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notify(self):
        pass


class InscritosSMS(TipoInscricao):
    def __init__(self, observer: AgenciaNoticia):
        self.observer = observer
        self.observer.subscribes(self)

    def notify(self):
        print(f"{type(self).__name__} {self.observer.view_news()}")


class InscritosEmail(TipoInscricao):
    def __init__(self, observer: AgenciaNoticia):
        self.observer = observer
        self.observer.subscribes(self)

    def notify(self):
        print(f"{type(self).__name__} {self.observer.view_news()}")


class InscritosOutroMeio(TipoInscricao):
    def __init__(self, observer: AgenciaNoticia):
        self.observer = observer
        self.observer.subscribes(self)

    def notify(self):
        print(f"{type(self).__name__} {self.observer.view_news()}")


if __name__ == "__main__":
    agc = AgenciaNoticia()

    InscritosEmail(agc)
    InscritosSMS(agc)
    InscritosOutroMeio(agc)

    print(f"Inscritos: {agc.followers}", end="\n")

    agc.adding_news("O padrão Observer está sendo usado!")
    agc.notify_everyone()

    print(f"\nDescadastrado: {type(agc.unsubscribe()).__name__}")
    print(f"Inscritos: {agc.followers}", end="\n")

    agc.adding_news("Desing Patterns com Python")
    agc.notify_everyone()
