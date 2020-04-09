from flask import request, render_template
from flask.views import MethodView

class MainController(MethodView):
    def __init__(self, modules):
        self.modules = modules

    def get(self):
        return render_template("main.html", title="Inventory")

    def post(self):
        module_name = request.form["module"]
        print(request.form)

        if module_name:
            module = self.modules[module_name]["instance"]
            module.save(request.form)

        return "", 204