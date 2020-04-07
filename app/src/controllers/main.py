from flask import render_template
from flask.views import MethodView

class MainController(MethodView):
    def __init__(self):
        pass

    def get(self):
        return render_template("main.html", title="Inventory")