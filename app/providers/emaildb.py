from app.db import Redis
class EmailRedis:
    def __init__(self):
        self.db=Redis().db
    def get_email(self,provider,id):
        email=self.db.hget(f"{provider}", id)
        if email:
            return email.decode()
        else: return None
    def set_email(self,provider,id,email):
        self.db.hset(f"{provider}", id, email)
