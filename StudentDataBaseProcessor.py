import json
import os
import Student

class DataBaseProcessor():
    def __init__(self):
        self.listOfStudent = []


    def AppendStudent(self, student):
        self.listOfStudent.append(student)

    def SerializeDataBase(self):
        with open("data_file.json", "w") as write_to_json_file:
            customlist = []
            for i in self.listOfStudent:
                student = dict(name=i.name,
                               surname=i.surname,
                               pid=i.pid,
                               institute=i.institute,
                               profession=i.profession,
                               group=i.group,
                               educationalLevel=i.educationalLevel,
                               age=i.age,
                               gpa=i.gpa)
                customlist.append(student)
            json_string = json.dumps(customlist)
            write_to_json_file.write(json_string)

    def AppendDataBase(self):
        if os.path.isfile("data_file.json"):
            listofstudents = self.DeserializeDataBase()
            # todo fix when we do not close app, and self.listofstudnets is not empty
            for i in range(len(listofstudents)):
                self.listOfStudent.append(next(item for item in listofstudents))
        self.SerializeDataBase()

    def DeserializeDataBase(self):
        with open("data_file.json", "r") as read_from_json_file:
            listofstudents = json.loads(read_from_json_file.read())
            return listofstudents
