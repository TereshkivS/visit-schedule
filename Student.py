class Student:
    def __init__(self, first_name, surname, personalID):
        self.__name = first_name
        self.__surname = surname
        self.__pid = personalID

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getPid(self):
        return self.__pid