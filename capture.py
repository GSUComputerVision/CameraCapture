import cv2 as cv

vid = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, frame = vid.read()
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv.destroyAllWindows()
print('Done')
