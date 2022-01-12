import redis
class Redis(object):
    def __new__(cls):
        if not hasattr(cls, 'db'):
            cls.db = r = redis.Redis(host='localhost', port=6379, db=0)
            
        return cls.db