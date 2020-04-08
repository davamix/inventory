import io
import base64
from PIL import Image
from flask import request, render_template
from flask.views import MethodView

from services.detection import DetectionService

class DetectionController(MethodView):
    def __init__(self, modules):
        self.modules = modules
        self.detection_service = DetectionService()

    def post(self):
        data = request.get_json()

        if data:
            # Decode image
            image_bytes = base64.b64decode(data)

            image = Image.open(io.BytesIO(image_bytes))
            image = image.convert(mode="RGB")

            label, score = self.detection_service.detect(image)

            print(f"{label}: {score}")

            if label in self.modules.keys():
                return render_template(f"modules/{self.modules[label]}"), 206
                # return self.modules[label], 206

            

        return "NO DATA", 204