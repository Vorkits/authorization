from app.db import Redis
class EmailRedis:
    def __init__(self):
        self.db=Redis().db
    def get_email(self,provider,id):
        email=self.db.hget(f"{provider}", id)
        print(email)