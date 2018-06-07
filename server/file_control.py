from server.database_control import DataBaseController as db
from server.request_response_control import ReqResController as rrc


class FileController:

	def __init__(self):
		self.db = db()
		self.rrc = rrc()

	def save_file(self, user, filename, data):
		import pdb;pdb.set_trace()
