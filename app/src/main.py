from pathlib import Path
from flask import Flask
from flask_socketio import SocketIO

from controllers.main import MainController
from controllers.detection import DetectionController

from services.detection import DetectionService
from modules.keyboard import KeyboardModule
from modules.monitor import MonitorModule

# Download model paramaters if needed
DetectionService()

templates_path = Path(Path.cwd(), "src", "templates")

app = Flask(__name__, template_folder = templates_path)
app.secret_key = b"session_secret_key"

socketio = SocketIO(app)

# https://stackoverflow.com/a/45438226/844372
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS")

    return response

def load_modules():
    print("Loading modules...")

    modules = {
        "keyboard": {
            "template": "keyboard.html",
            "instance": KeyboardModule(socketio)
        },
        "tv":{ # Monitor
            "template": "monitor.html",
            "instance": MonitorModule(socketio)
        }
    }

    return modules

modules = load_modules()
print(f"Modules loaded: {modules.keys()}")

app.add_url_rule("/main", view_func=MainController.as_view("main", modules=modules))
app.add_url_rule("/detect", view_func=DetectionController.as_view("detection", modules=modules))

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)