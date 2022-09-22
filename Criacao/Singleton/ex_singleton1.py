class AppSettings:

    _instance = None

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kargs)

        return cls._instance

    # Problema no Singleton - toda inicializacao sobrepoem as configuracoes mudadas
    def __init__(self):
        self.camera = 0


if __name__ == "__main__":

    as1 = AppSettings()
    print(as1.camera)
    as2 = AppSettings()
    as2.camera=1
    print(as2.camera)

    print(as1, as2)