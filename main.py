from multiprocessing import Process, Queue
import vidInference

def main(q):
    classes = {0: 'person', 11: 'stop-sign'}

    while True:
        frame = q.get()
        for box in frame.cls:
            print(classes[int(box)], " detected from main.py")


if __name__ == '__main__':
    q = Queue()
    p = Process(target=vidInference.videoInference, args=(q,))
    p2 = Process(target=main, args=(q,))
    p.start()
    p2.start()
    p.join()
    p2.join()
    print("Done")
