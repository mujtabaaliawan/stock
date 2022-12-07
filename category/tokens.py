import os
from dotenv import load_dotenv

load_dotenv()
secret_key = str(os.getenv('TOKEN_KEY'))


token1 = {
    "market": "stock",
    "name": "ran_han",
    "city": "karachi",
    "iat": 1516239022
}
token2 = {
    "market": "stock",
    "name": "muji_maz",
    "city": "karachi",
    "iat": 1516239022
}

token3 = {
    "market": "stock",
    "name": "jango_rango",
    "city": "karachi",
    "iat": 1516239022
}

allowed_tokens = [token1, token2, token3]


