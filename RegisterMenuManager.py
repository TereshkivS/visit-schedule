from cv2 import *
from Student import Student
import uuid
import StudentDataBaseProcessor


class RegisterMenuManager:
    def __init__(self):
        # TODO move in constants
        self.__images_path = os.path.join(os.getcwd(), 'images')
        self.__dbproccessor = StudentDataBaseProcessor.DataBaseProcessor()
        self.__folderPath = ''

    def RegisterInDataBase(self, OpenCvManager, student):
        # Add in list of students
        self.__dbproccessor.AppendStudent(student)
        #self.__dbproccessor.AppendDataBase()
        OpenCvManager.TrainPhotos(self.__dbproccessor)

    def GetFolderPath(self):
        return self.__folderPath

    def CalculateFolerPath(self, student):
        folderName = student.name.lower()+student.surname.lower()
        self.__folderPath = os.path.join(self.__images_path, folderName)