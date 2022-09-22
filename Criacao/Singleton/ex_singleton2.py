def singleton(the_class):
    instances = {}

    def get_class(*args,**kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class

@singleton
class AppSettings:

    def __init__(self):
        self.camera = 0


if __name__ == "__main__":

    as1 = AppSettings()
    print(as1.camera)

    as2 = AppSettings()
    print(as2.camera)

    print(as1, as2)