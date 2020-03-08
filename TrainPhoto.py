import os
import Student
from PIL import Image
import cv2
import numpy
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # project directory
images_dir = os.path.join(BASE_DIR, 'images')  # directory of images

# TODO change path to more universal for differents OS
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# TODO check another face recognitions classes
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
# dictionary " name : id "
label_ids = {}
# 2 dimential array of detected faces
x_train = []
y_labels = []

for root, dirs, files in os.walk(images_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "_").lower()
            if not label in label_ids:
                label_ids[label] = current_id
                current_id = current_id + 1
            # set current id
            id_ = label_ids[label]
            # some numbers of persons
            # y_labels.append(label)
            # x_train.append(path)
            pil_image = Image.open(path).convert("L")  # grayscale
            # convert to array of numpy
            image_array = numpy.array(pil_image, "uint8")
            # print(image_array)
            # detect faces on the frame
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for x, y, w, h in faces:
                # region of interests
                roi = image_array[y:y + h, x:x + w]
                # face
                x_train.append(roi)
                # ids
                y_labels.append(id_)

# save face names
with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

# train data and save it to file
recognizer.train(x_train, numpy.array(y_labels))
recognizer.save("train.yml")


def GetLowerDirectoryName():
    return os.path.basename(root).replace(" ", "_").lower()
