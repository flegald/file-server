import jwt
import datetime


def generate_token(user_info):
	user_id = user_info["_id"]
	meta_data = {
		"exp": (datetime.datetime.utcnow() + datetime.timedelta(days=10)).timestamp(),
		"user_id": user_id
	}
	token = jwt.encode(meta_data, "secret", algorithm="HS256")
	return token

def decrypt_token(token):
	return jwt.decode(token, "secret", algorithm="HS256")