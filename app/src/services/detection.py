import torch
import numpy as np
from torchvision import models, transforms
from PIL import Image
from pathlib import Path

class DetectionService():
    def __init__(self):
        # Application path
        # self.app_path = Path(Path.cwd(), "app")

        # https://pytorch.org/docs/stable/torchvision/models.html#object-detection-instance-segmentation-and-person-keypoint-detection
        self.COCO_INSTANCE_CATEGORY_NAMES = [
            '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
            'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
            'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
            'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
            'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
            'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
            'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
            'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
            'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
            'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
            'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
        ]

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.model = models.detection.maskrcnn_resnet50_fpn(pretrained=True).eval().to(self.device)

    def detect(self, image):
        img_tensor = transforms.ToTensor()(image)
        aligned = torch.stack([img_tensor]).to(self.device)
        
        outputs = self.model(aligned)

        print(len(outputs))
        
        # Info for the first prediction (with highest score)
        p = outputs[0]
        label = p["labels"][0]
        score = p["scores"][0]

        return self.COCO_INSTANCE_CATEGORY_NAMES[label.item()], score.item()

# img = Image.open(Path(APP_PATH, "images", "book.png"))

# Convert image from RGBA to RGB
# img_rgb = img.convert("RGB")

# Create a Tensor
# img_tensor = transforms.ToTensor()(img_rgb)
# print(f"Tensor: {img_tensor.shape}")

# Stack the image in order to pass to the model
# aligned = torch.stack([img_tensor]).to(device)
# print(f"Aligned: {aligned.shape}")

# Get predictions
# predictions = model(aligned)

# Info for the first prediction (with highest score)
# p = predictions[0]
# label = p["labels"][0]
# score = p["scores"][0]

# print(f"{COCO_INSTANCE_CATEGORY_NAMES[label.item()]}: {score.item() * 100:.2f}%")

# Labels
# for p in predictions:
#     categories = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in p["labels"].numpy()]
    
#     for c,s in zip(categories, p["scores"]):
#         print(f"{c}: {s.item()}")
