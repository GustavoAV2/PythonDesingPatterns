class Object:
    def __init__(self):
        self.__observers = []

    def __repr__(self):
        return "::Objeto::"

    def register(self, observer):
        self.__observers.append(observer)

    def notify_everyone(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class ObserverA:
    def __init__(self, observer: Object):
        observer.register(self)

    def __repr__(self):
        return "::Objeto::"

    def notify(self, observer: Object, *args):
        print(f"O {type(self).__name__} recebeu uma {args[0]} de {observer}")


class ObserverB:
    def __init__(self, observer: Object):
        observer.register(self)

    def notify(self, observer: Object, *args):
        print(f"O {type(self).__name__} recebeu uma {args[0]} de {observer}")


if __name__ == "__main__":
    obj = Object()

    obs_a = ObserverA(obj)
    obs_b = ObserverB(obj)

    obj.notify_everyone("Notificação")

