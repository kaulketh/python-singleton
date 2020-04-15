class _Singleton(type):
    """ A metaclass that creates a Singleton base class when called.
        Works in Python 2 & 3
        https://www.it-swarm.dev/de/python/ein-singleton-python-erstellen/972393601
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args,
                                                                  **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})):
    """ Works in Python 2 & 3
        https://www.it-swarm.dev/de/python/ein-singleton-python-erstellen/972393601
    """
    pass
