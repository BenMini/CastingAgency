# Full Stack Casting Agency API
An API to simplify the casting of films. Allows for casting assistants, directors, and executive producers to all collaberate, in a simplified efficient manner.

## API Authentication and Authorization
There are three roles associated with API:
1. Casting Assistant:
    - Can view actors and movies
2. Casting Director:
    - All permissions of casting assistant and
    - Add or delete an actor from the database
    - Modify actors or movies
2. Executive Producer
    - All permissions a casting director has and
    - Add or delete movie from database
Those without roles are limited to the viewing of the movie and actor list.

## Hosting
App is hosted [here](https://ben-capstone-fsnd.herokuapp.com/)

## Local Requirements
Requires Python 3.7 or later

#### Python 3.7
Follow instructions to install the latest version for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment
It is recommended that you create a virtual environment to work from. You can do that by running:
`python -m venv venv`

#### PIP Dependencies
Once your virtual environment is up and running, you can install the requirements needed for the api:
`pip install -r requirements.txt`

##### Key Dependencies
- [Flask](http://flask.pocoo.org/) is a lightweight backend micro-services framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
The app is configured to run with Postgres but any relational database that is supported by SQLAlchemy will work. The following code will need to be run to create the database:
`dropdb capstone && createdb capstone`

## Running the Server
To run the server, execute:
`flask run --reload`
(The reload flag is optional)
 
# Endpoints
### GET '/'
- returns a JSON object representing what could be the home page
Example: 
```
{
	"hello":"Hello World"
}
```

### GET '/actors'
- returns a JSON object of all actors stored in the database
Example: 
```
{
    "Actors": [
        {
            "id": 1,
            "name": "Brad Pitt",
        }
    ], # shortened for brevity
    "success": true
}
```

### GET '/movies'
- returns a JSON object of all the movies in the database
Example 
```
{
    "movies": [
        {
            "id": 2,
            "title": "\"Fight Club\""
        }
    ], # shortened for brevity
    "success": true
}
```

### GET '/actors/1'
- returns a JSON object with an actors information
Example: 
```
{
    "actors": [
        {
            "age": 56,
            "gender": "\"male\"",
            "id": 1,
            "name": "\"Brad Pitt\""
        }
    ],
    "success": true
}
```

### GET '/movies/1'
- returns JSON object of movie with full detail
Example:
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 06 Dec 1999 00:00:00 GMT",
            "title": "\"The Green Mile\""
        }
    ],
    "success": true
}
```

### POST '/actors'
- Creates a new actor in the database
- Returns JSON object of actor information
Example:
```
{
    "actors": [
        {
            "age": 56,
            "gender": "\"male\"",
            "id": 1,
            "name": "\"Brad Pitt\""
        }
    ],
    "success": true
}
```

### POST '/movies'
- creates a new movie in the database
- returns JSON object with movie info
Example:
```
{
    "movies": [
        {
            "id": 1,
            "title": "\"The Green Mile\""
        }
    ],
    "success": true
}
```

### PATCH '/actors/1'
- Updates actor with correlating ID
- returns JSON object with actor information
Example:
```
{
    "actors": [
        {
            "age": 38,
            "gender": "\"female\"",
            "id": 1,
            "name": "\"Natalie Portman\""
        }
    ],
    "success": true
}
```

### PATCH '/movies/1'
- Updates movie with correlating ID
- Returns JSON object with changed movie info
Example:
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 16 Jul 2010 00:00:00 GMT",
            "title": "\"Inception2\""
        }
    ],
    "success": true
}
```

### DELETE '/actors/1'
- Deletes correlating actor 
- Returns actor ID and success message
Example:
```
{
    "delete": 1,
    "success": true
}
```

### DELETE '/movies/1'
- Deletes correlating movie
- Returns deleted movie ID and success: true
Example:
```
{
    "delete": 1,
    "success": true
}
```