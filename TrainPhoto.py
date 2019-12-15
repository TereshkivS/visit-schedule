import os
import Student
from PIL import Image
import cv2
import numpy
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(BASE_DIR, 'images')

# TODO change path to more universal for differents OS
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# TODO check another face recognitions classes
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
# dictionary " name : id "
label_ids = {}
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
            id_ = label_ids[label]
            #some numbers of persons
            #y_labels.append(label)
            #x_train.append(path)
            pil_image = Image.open(path).convert("L")  # grayscale
            image_array = numpy.array(pil_image, "uint8")
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for x,y,w,h in faces:
                roi = image_array[y:y+h, x:x+w]
                # face
                x_train.append(roi)
                # ids
                y_labels.append(id_)

with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, numpy.array(y_labels))
recognizer.save("train.yml")