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

```POST: /api/register```

```JSON BODY: { "username": {{username}}, "password": {{password}} }```

Creates new user in "DB".

__

```POST: /api/login```

```JSON BODY: { "username": {{username}}, "password": {{password}} }```

If user exists, will return JWT token

__

### Notes 

"DB" is json files stored in```/database```. A live DB was excluded for time constraints.

More time was taken than intended to create re-usable code. This can be seen in the controller

files.

Last work was being done on the file upload endpoint.
