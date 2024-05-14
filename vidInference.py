from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Results

model = YOLO('yolov8n.pt')

results = model(source='0', show=True, conf=0.4, save=False, classes=[0, 11], save_txt=True, stream=True)

for point in results:
    result: Results = point
    im_array = result.plot()
    im = Image.fromarray(im_array[:, :, ::-1])
    var = result.boxes

    print("This is my var", var)

print('Done')
