from ultralytics import YOLO
from multiprocessing import Queue


def videoTrack(queue, source='sources/video2.mp4'):
    trackModel = YOLO("yolov8n.pt")

    results = trackModel.track(source=source, show=True, conf=0.4, save=False, save_txt=False, stream=True, classes=[11])

    for frame in results:
        boxes = frame.boxes
        queue.put(boxes)


if __name__ == '__main__':
    queueObj = Queue()
    videoTrack(queueObj)
