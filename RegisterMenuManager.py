from cv2 import *
from Student import Student
import uuid
import StudentDataBaseProcessor


class RegisterMenuManager:
    def __init__(self, student):
        # TODO move in constants
        self.__images_path = os.path.join(os.getcwd(), 'images')
        self.__student = student
        self.__folderName = student.getName().lower()+student.getSurname().lower()
        self.__folderPath = os.path.join(self.__images_path, self.__folderName)
        self.__dbproccessor = StudentDataBaseProcessor.DataBaseProcessor()

    def RegisterInDataBase(self, OpenCvManager):
        # Add in list of students
        self.__dbproccessor.AppendStudent(self.__student)
        self.__dbproccessor.SerializeDataBase()
        OpenCvManager.TrainPhotos(self.__dbproccessor)

    def GetFolderPath(self):
        return self.__folderPath