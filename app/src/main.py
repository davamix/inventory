from pathlib import Path
from flask import Flask

from controllers.main import MainController
from controllers.detection import DetectionController

from services.detection import DetectionService

# Download model paramaters if needed
DetectionService()

templates_path = Path(Path.cwd(), "src", "templates")

app = Flask(__name__, template_folder = templates_path)
app.secret_key = b"session_secret_key"

# https://stackoverflow.com/a/45438226/844372
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS")

    return response

# Register module names with the templates
modules = {
    "keyboard": "keyboard.html",
    "tv": "monitor.html"
    }

app.add_url_rule("/main", view_func=MainController.as_view("main"))
app.add_url_rule("/detect", view_func=DetectionController.as_view("detection", modules=modules))
# app.add_url_rule("/register")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)