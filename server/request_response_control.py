from flask import request, url_for
from flask_api import status
import json

class ReqResController:

	def __init__(self):

		self.status_codes = {
			"200": status.HTTP_200_OK,
			"201": status.HTTP_201_CREATED,
			"204": status.HTTP_204_NO_CONTENT,
			"400": status.HTTP_400_BAD_REQUEST,
			"403": status.HTTP_403_FORBIDDEN,
			"404": status.HTTP_404_NOT_FOUND
		}

	def response(self, status_code, content=False):
		if content:
			resp_content = json.dumps(content)
			return resp_content, self.status_codes[status_code]
		else:
			return self.status_codes[status_code]

	def check_request_format(self, request_body):
		body = request_body.data
		if not body:
			return self.response(400, {"error": "Invalid JSON"})
		return False