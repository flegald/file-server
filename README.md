# file-server

### Installation
##### Requirements
* python
* git
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [pip](https://pypi.org/project/pip/)

Clone repo:

```$:git clone https://github.com/flegald/file-server.git```

Initiate virtualenv in directory:

```$:virtualenv -p python3 . ```

```$:source bin/activate```

Install requirements:

```(file-server)$:pip install -r requirements.txt```


### Run

```(file-server)$:python app.py```

### What's (Mostly) Working

* ```POST: /api/register```

	```JSON BODY: { "username": {{username}}, "password": {{password}} }```

	Creates new user in "DB".

__

* ```POST: /api/login```

	```JSON BODY: { "username": {{username}}, "password": {{password}} }```

	If user exists, will return JWT token

* ```POST: /api/files/<filename>```

	```File in post```

	Will upload a file to users personal file folder.

* ```GET: /api/view/files```

	Will spit out list of all files in users folder.

__

Functionality can all be interacted with in very basic frontend

* Start server and navigate to ```http://127.0.0.1:5000/```

* Enter username and password in inputs and click ```Register```
	User with hashed password will be created in ```database/users.json```
	Directory for users folder (based on newly created user id in ```user_images/<user_id>```)

* Use same inputs with username and password and click ```Login```
	JWT token will be passed into local storage.

* Select a file to upload and click ```Upload```.
	File will then be uploaded in the users directory under ```user_images/<user_id>```.


* Click ```View Files``` To see list of uploaded files by user.
