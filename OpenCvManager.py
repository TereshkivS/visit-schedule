import cv2
from cv2 import *
import pickle
import os
import uuid

import numpy
from PIL import Image


# TODO add mutex to recognizer

class OpenCvManager:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # project directory
        self.IMAGES_DIR = os.path.join(self.BASE_DIR, 'images')  # directory of images

    def LoadNameLabels(self):
        try:
            with open("labels.pickle", 'rb') as f:
                og_labels = pickle.load(f)
                return og_labels
        except IOError:
            labels = {}
            return labels


    def ReverseLabels(self, og_labels):
        labels = {v: k for k, v in og_labels.items()}
        return labels

    def CreateRecognizer(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        return recognizer

    def ReadFromFileToRecognizer(self, recognizer):
        recognizer.read("train.yml")

    def StartMonitoring(self):
        cap = cv2.VideoCapture(0)
        recognizer = self.CreateRecognizer()
        self.ReadFromFileToRecognizer(recognizer)
        while True:
            ret, frame = cap.read()
            # convert frame to gray color
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                # contains faces on the screen
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                # recognize
                # TODO if TimeToLive is not new read from recognizer
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 45 and conf <= 85:
                    labels = self.ReverseLabels(self.LoadNameLabels())
                    label = labels[id_]
                    self.SetTextAroundFace(frame, x, y, id_, label)
                    self.DrawRectangleAroundFaces(frame, x, y, w, h)
                # todo write roi into file

            cv2.imshow('Video', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    def DrawRectangleAroundFaces(self, frame, x, y, w, h):
        color = (0, 255, 0)     # green color
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    def SetTextAroundFace(self, frame, x, y, id_, name):
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

    def TrainPhotos(self, dataBase):
        recognizer = self.CreateRecognizer()
        # dictionary " name : id "
        label_ids = self.LoadNameLabels()
        print(label_ids)
        listOfStudents = dataBase.listOfStudent
        #listOfStudents = dataBase.DeserializeDataBase()
        # 2 dimential array of detected faces
        x_train = []
        y_labels = []
        for root, dirs, files in os.walk(self.IMAGES_DIR):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "_").lower()
                    if not label in label_ids:
                        clearstruui = self.GetUuidByName(label, listOfStudents).replace('-', '')
                        current_id = int(clearstruui, base=16)
                        print(current_id)
                        label_ids[label] = current_id
                    # set current id
                    id_ = label_ids[label]
                    # some numbers of persons
                    pil_image = Image.open(path).convert("L")  # grayscale
                    # convert to array of numpy
                    image_array = numpy.array(pil_image, "uint8")
                    # detect faces on the frame
                    faces = self.face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                    for x, y, w, h in faces:
                        # region of interests
                        print("Faces was found")
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

    def GetUuidByName(self, label, listofstudents):
        # todo hanle if is not matches
        for x in listofstudents:
            if x.name.lower() + x.surname.lower() == label:
                return x.pid
        # matches = next(item for item in listofstudents if item["name"].lower() + item["surname"].lower() == label)
        # print("Matches = " + matches["pid"])
        print("GetUuidByName crashed because it was no same label in list of students")
        return 0

    def TakeAPhoto(self, folderPath):
        cam = VideoCapture(0, cv2.CAP_DSHOW)  # 0 -> index of camera
        while True:
            s, img = cam.read()
            if s:  # frame captured without any errors
                # check if person already exists
                if not os.path.exists(folderPath):
                    os.mkdir(folderPath)
                # TODO don't work with unicode ((
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                print(faces)
                if len(faces) is not 0:
                    print("Photo is done")
                    imwrite(os.path.join(folderPath, str(uuid.uuid4()) + '.png'), img)
                    break
        cam.release()
        cv2.destroyAllWindows()
