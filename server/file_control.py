import os
from flask import Flask, request, redirect, url_for
from flask_api import status

from werkzeug.utils import secure_filename
from server.database_control import DataBaseController as db
from server.request_response_control import ReqResController as rrc

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class FileController:

	def __init__(self):
		self.db = db()
		self.rrc = rrc()

	def save_file(self, user, filename, data):
		file = data.files["file"]
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_path = os.path.join("user_images", str(user), filename)
			file.save(os.path.join(os.getcwd(), "user_images", str(user), filename))
			return {"message": file_path}, status.HTTP_201_CREATED

	def view_files(self, user):
		file_path = os.path.join(os.getcwd(), "user_images", str(user))
		files = []
		for user_file in os.listdir(file_path):
			files.append(user_file)
		return {"files": files}, status.HTTP_200_OK
