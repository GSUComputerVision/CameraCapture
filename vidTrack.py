from ultralytics import YOLO

trackModel = YOLO("yolov8n.pt")

results = trackModel.track(source=0, show=True, conf=0.4, save=False, save_txt=True)
