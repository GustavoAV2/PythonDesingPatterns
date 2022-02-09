class Actor:
    def __init__(self):
        self.busy = False

    def available(self):
        self.busy = False
        print(f'{type(self).__name__} está disponível para atuação!')

    def unavailable(self):
        self.busy = True
        print(f'{type(self).__name__} está ocupado em uma atuação!')

    def get_status(self):
        return self.busy


class Agent:

    @staticmethod
    def to_work():
        actor = Actor()
        if actor.get_status():
            actor.unavailable()
        else:
            actor.available()


if __name__ == '__main__':
    agent = Agent()
    agent.to_work()
