import json
import os


class DataBaseController:

	def __init__(self):
		self.users = self.load_db("users")
		self.files = self.load_db("files")

	def load_db(self, domain):
		db = "users.json" if domain == "users" else "files.json"
		fname = "./database/{}".format(db)
		with open(fname, "r") as ifile:
			return json.load(ifile)

	def save_db(self, domain, data):
		db = "users.json" if domain == "users" else "files.json"
		fname = "./database/{}".format(db)
		with open(fname, "w") as ifile:
			return json.dump(data, ifile, indent=4)

	def find(self, domain, key, query):
		db = self.users if domain == "users" else self.files
		for _id, data in db.items():
			if data[key] == query:
				return data
		return None

	def create(self, domain, new_object):
		db = self.users if domain == "users" else self.files
		try:
			new_pk = int(max(db.keys())) + 1
		except ValueError:
			new_pk = 0
		new_object["_id"] = new_pk
		db[new_pk] = new_object
		if domain == "users":
			self.users = db
		else:
			self.files = db
		self.save_db(domain, db)
		return new_pk
		