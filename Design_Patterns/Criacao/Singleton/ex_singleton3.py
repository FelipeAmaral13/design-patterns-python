class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):

    def __init__(self):
        self.camera = 0


if __name__ == "__main__":

    as1 = AppSettings()
    print(as1.camera)

    as2 = AppSettings()
    as2.camera = 1  
    print(as2.camera)

    as3 = AppSettings()
    print(as3.camera)

    print(as1, as2)




