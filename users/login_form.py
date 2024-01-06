import logging

from pydantic import BaseModel

from .models import User


class LoginForm(BaseModel):
    username: str
    password: str

    def authenticate(self):
        try:
            if User.objects.filter(username=self.username, password=self.password).exists():
                user = User.objects.get(username=self.username, password=self.password)
                if user:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            logging.warning(e)
            return False
