from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Results

model = YOLO('yolov8n.pt')

results = model(source='0', show=True, conf=0.4, save=False, classes=[0, 11], save_txt=True, stream=True)

for point in results:
    result: Results = point
    var = result.boxes
    print(var, "\n")

print('Done')
