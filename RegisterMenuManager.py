from cv2 import *
from Student import Student
import uuid
import StudentDataBaseProcessor


class RegisterMenuManager:
    def __init__(self, student):
        self.__images_path = os.path.join(os.getcwd(), 'images')
        self.__student = student
        self.__folderName = student.getName().lower()+student.getSurname().lower()
        self.__folderPath = os.path.join(self.__images_path, self.__folderName)
        self.__dbproccessor = StudentDataBaseProcessor.DataBaseProcessor()

    def TakeAPhoto(self):
        cam = VideoCapture(0, cv2.CAP_DSHOW)  # 0 -> index of camera
        s, img = cam.read()
        if s:  # frame captured without any errors
            # check if person already exists
            if not os.path.exists(self.__folderPath):
                os.mkdir(self.__folderPath)
            # TODO don't work with unicode ((
            imwrite(os.path.join(self.__folderPath, str(uuid.uuid4()) + '.png'), img)
        cam.release()
        cv2.destroyAllWindows()

    def RegisterInDataBase(self):
        # Add in list of students
        self.__dbproccessor.AppendStudent(self.__student)
        self.__dbproccessor.SerializeDataBase()
        self.__dbproccessor.DeserializeDataBase()
