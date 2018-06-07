from flask import request, url_for, render_template
from flask_api import FlaskAPI, status, exceptions
import jinja2

from server.user_control import UserController
from server.file_control import FileController
from server.request_response_control import ReqResController
from werkzeug import secure_filename

app = FlaskAPI(__name__)

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

_USERCONTROL = UserController()
_FILECONTROL = FileController()
_RRC = ReqResController()

@app.route("/")
def home():
	return render_template("index.jinja2")

@app.route("/api/register", methods=["POST"])
def register_user():
	err = _RRC.check_request_format(request)
	if err: return err
	return _USERCONTROL.register_user(request.data)

@app.route("/api/login", methods=["POST"])
def login_user():
	err = _RRC.check_request_format(request)
	if err: return err
	return _USERCONTROL.login(request.data)

@app.route("/api/files/<filename>", methods=["PUT"])
def put_file(filename):
	data, err = _USERCONTROL.validate_token(request)
	if err:
		content = {"error": data}
		return _RRC.response("403", content)
	user_id = data["_id"]
	file_saved = _FILECONTROL.save_file(user_id, filename, request)


if __name__ == "__main__":
	app.run()