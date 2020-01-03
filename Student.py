class Student:
    def __init__(self, first_name, surname, personalID, institute, profession, group, educationalLevel, age, gpa):
        self.__name = first_name
        self.__surname = surname
        self.__pid = personalID
        self.__institute = institute
        self.__profession = profession
        self.__group = group
        self.__educationalLevel = educationalLevel
        self.__age = age
        self.__gpa = gpa

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getPid(self):
        return self.__pid
