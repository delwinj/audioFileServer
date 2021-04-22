# flask packages
from flask import Flask
from flask_restful import Api

# local packages
from api.errors import errors
from database.db import initialize_db
from api.routes import initialize_routes

app = Flask(__name__)
api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/audio-db'
}
app.url_map.strict_slashes = False

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run()
