from flask import Flask
from flask_cors import CORS


app = Flask(__name__, static_folder='static', static_url_path='')
app.debug = True
app.config['JSON_SORT_KEYS'] = False
CORS(app)

if __name__ == "__main__":  
    from views import *
    app.run()