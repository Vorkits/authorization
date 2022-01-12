import redis
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class Redis( metaclass=Singleton):
    def __init__(self):
        self.db=redis.Redis(host='localhost', port=6379, db=0)
