from multiprocessing import Process, Queue
import vidInference


def mainProg(queue):
    """
    Main program loop that processes detected bounding boxes from a queue.
    """
    classes = {0: 'person', 11: 'stop-sign'}

    while True:
        boxes = queue.get()
        for box in boxes:
            width = "{:.3f}".format(box.xywh[0][2])
            distance = estimateDistance(bbox_width=float(width))
            print(f"Detected Width: {width} Distance: {distance:.2f} ft")


def estimateDistance(bbox_width, focal_length=(23 * 1920) / 9.956, sign_width=30):
    """
    Estimate the distance to an object based on the bounding box width.

    Parameters:
    - bbox_width: Width of the bounding box in pixels.
    - focal_length: Focal length in pixels.
    - sign_width: Real-world width of the object in inches.

    Returns:
    - Distance to the object in feet.
    """
    return (sign_width * focal_length) / (bbox_width * 12)


if __name__ == '__main__':
    q = Queue()
    # Process for video inference
    p1 = Process(target=vidInference.videoInference, args=(q, "sources/video2.mp4"))

    # Process for processing bounding boxes and estimating distances
    p2 = Process(target=mainProg, args=(q,))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    print("Done")
    exit(0)
