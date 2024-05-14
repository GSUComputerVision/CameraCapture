import ultralytics.engine.results as Results
from PIL import Image
from ultralytics import YOLO

model = YOLO('sources/yolov8n.pt')

results = model(source=['sources/singleStop.jpg', 'sources/multStops.jpeg'], classes=[0, 11])

count = 1

for point in results:
    result: Results = point
    im_array = result.plot()
    im = Image.fromarray(im_array[:, :, ::-1])

    # This contains the data about the sizes of the objects
    var = result.boxes
    shape = result.orig_shape

    print("\nThis is my var", var, "\nOriginal Shape: ", shape)
    # im.show()
    string = "output"+str(count)+".jpg"
    im.save(string)
    count += 1