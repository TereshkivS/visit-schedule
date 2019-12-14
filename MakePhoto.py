import numpy
import cv2
import os


images_path = os.path.join(os.getcwd(), 'images')

cap = cv2.VideoCapture(0)
count = 0
while(True):
    ret, frame = cap.read()

    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if not os.path.exists('images'):
        os.mkdir('images')
    else:
        cv2.imwrite(os.path.join(images_path, '%d.jpg') % count, frame)
        break


cap.release()
cv2.destroyAllWindows()