from app.db import Redis
class EmailRedis:
    def __init__(self):
        self.db=Redis().db
    def get_email(self,provider,id):
        return self.db.hget(f"{provider}", id)
    def set_email(self,provider,id,email):
        self.db.hset(f"{provider}", id, email)
