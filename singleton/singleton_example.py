
class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    obj_singleton1 = Singleton()
    obj_singleton2 = Singleton()

    id(obj_singleton1)
    # 1714923450224
    id(obj_singleton2)
    # 1714923450224
