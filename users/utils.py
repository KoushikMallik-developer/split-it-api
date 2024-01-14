import os

import jwt
import datetime

from dotenv import load_dotenv

from users.models import User


class Utilities:
    @staticmethod
    def generate_token(user: User):
        # Secret key to sign the token
        load_dotenv()
        secret_key = os.environ.get("JWT_SECRET_KEY")

        # Payload (data to be included in the token)
        payload = {
            "user_id": user.id,
            "username": user.email,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=1),  # Token expiration time (1 day from now)
        }

        # Generate the JWT token
        token = jwt.encode(payload, secret_key, algorithm="HS256")

        print("Generated JWT Token:", token)
