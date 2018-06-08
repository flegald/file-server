from server.database_control import DataBaseController as db
from server.request_response_control import ReqResController as rrc
from server.token_control import generate_token, decrypt_token
from werkzeug.security import generate_password_hash, check_password_hash
import os

class UserController:

	def __init__(self):
		self.db = db()
		self.rrc = rrc()

	@staticmethod
	def verify_register_requirements(username, password):
		err = None
		verified = False, 
		un_len = len(username)
		pw_len = len(password)
		if un_len < 3 or \
		un_len > 20:
			err = "Username must be between 3 and 20 characters."
		elif pw_len < 8:
			err = "Password must be at least 8 characters."
		else:
			verified = True
		return verified, err

	def save_user(self, username, password):
		new_pk = False
		try:
			user = {"username": username, "password": generate_password_hash(password)}
			new_pk = self.db.create("users", user)
			return False, new_pk
		except Exception as e:
			return e, new_pk

	def register_user(self, user_info):
		username = user_info["username"]
		password = user_info["password"]
		if self.db.find("users", "username", username):
			content = {"error": "User Already Exists"}
			return self.rrc.response("400", content)

		verified, err = self.verify_register_requirements(username, password)
		if err:
			content = {"error": err}
			print(err)
			return self.rrc.response("400", content)

		save_error, new_pk = self.save_user(username, password)
		if save_error:
			content = {"error": save_error}
			print(save_error)
			return self.rrc.response("400", content)
		os.makedirs(os.path.join(os.getcwd(), "user_images", str(new_pk)))
		return self.rrc.response("204", {"message": "success"})

	def login(self, user_info):
		username = user_info["username"]
		password = user_info["password"]
		user = self.db.find("users", "username", username)
		if user and check_password_hash(user["password"], password):
			token = generate_token(user)
			content = {"token": token.decode("utf8")}
			return self.rrc.response("200", content)
		else:
			content = {"error": "Invalid Credentials"}
			return self.rrc.response("403", content)

	def validate_token(self, data):
		err = False
		token = data.headers.get("X-Session", None)
		if not token:
			err = True
			return "No Auth Provided", err
		try:
			info = decrypt_token(token)
			user_id = info["user_id"]
		except:
			err = True
			return "Invalid Token", err
		user = self.db.find("users", "_id", int(user_id))
		if not user:
			err = True
			return "Invalid User", err
		return user, err