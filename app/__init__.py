from flask import Flask
from .landing.routes import landing

app = Flask(__name__)

app.register_blueprint(landing)
app.static_folder = 'static'


from app import routes