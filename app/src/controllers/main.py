from flask import request, render_template
from flask.views import MethodView

class MainController(MethodView):
    def __init__(self, modules):
        self.modules = modules

    def get(self):
        return render_template("main.html", title="Inventory")

    def post(self):
        data = request.get_json()
        
        module_name = data["module"]
        print(data)

        if module_name:
            module = self.modules[module_name]["instance"]
            module.save_data(data)

        return "", 204