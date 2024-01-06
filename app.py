from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from controllers.home_controller import HomeController
from controllers.instagram_controller import InstagramController
import json

app = Flask(__name__)
CORS(app)

# init controllers
home_controller = HomeController()
instagram_controller = InstagramController()

@app.route('/')
def home():
  return home_controller.index()

@app.route("/instagram", methods=["POST"])
def instagram():
   return instagram_controller.index()


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({"code": e.code, "text": e.name})
    response.content_type = "application/json"
    return response
