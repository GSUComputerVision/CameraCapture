from ultralytics import YOLO
from ultralytics.engine.results import Results
from multiprocessing import Queue

def videoInference(queue):
    model = YOLO('yolov8n.pt')

    results = model(source='0', show=True, conf=0.4, save=False, classes=[0, 11], save_txt=False, stream=True)

    classes = {0: 'person', 11: 'stop-sign'}

    for frame in results:
        boxes = frame.boxes
        queue.put(boxes)

    print('Done')

if __name__ == '__main__':
    queue = Queue()
    videoInference(queue)
