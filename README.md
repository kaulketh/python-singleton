# Singleton in Python

##### Thanks to [**_it-swarm.dev_**](https://www.it-swarm.dev/de/python/ein-singleton-python-erstellen/972393601/)
## Python 2 and 3 compatible version with a Metaclass

To write something that works in both Python2 and 3, a slightly more complicated scheme has to be used. Since metaclasses are usually subclasses of type type, you can use one to dynamically create an intermediate base class at runtime with this as a metaclass, and then as the base class of the public singleton base class.
````python
class _Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(_Singleton('SingletonMeta', (object,), {})): pass

class MySingletonClass(Singleton):
    pass
````

An ironic aspect of this approach is the use of subclasses to implement a metaclass. A possible advantage is that isinstance (inst, singleton) returns True in contrast to a pure metaclass.
