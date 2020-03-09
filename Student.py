import json


class Student:
    def __init__(self, name, surname, pid, institute, profession, group, educationalLevel, age, gpa):
        self.name = name
        self.surname = surname
        self.pid = pid
        self.institute = institute
        self.profession = profession
        self.group = group
        self.educationalLevel = educationalLevel
        self.age = age
        self.gpa = gpa

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)
    #
    # def getName(self):
    #     return self.name
    #
    # def getSurname(self):
    #     return self.surname
    #
    # def getPid(self):
    #     return self.pid
    #
    # def getInstitute(self):
    #     return self.institute
    #
    # def getProfesssion(self):
    #     return self.profession
    #
    # def getGroup(self):
    #     return self.group
    #
    # def getEducationalLeve(self):
    #     return self.educationalLevel
    #
    # def getGPA(self):
    #     return self.gpa
    #
    # def getAge(self):
    #     return self.age
    #
    # def setName(self, name):
    #     self.name = name
