
class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('Called')
        else:
            print('Was called')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == '__main__':
    obj_singleton1 = Singleton()
    obj_singleton2 = Singleton()

    print(id(obj_singleton1))  # Mostrando local de memória
    print(id(obj_singleton2))  # Mostrando local de memória
