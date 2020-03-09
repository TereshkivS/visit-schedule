import json
import os
import Student

class DataBaseProcessor():
    def __init__(self):
        try:
            self.listOfStudent = self.DeserializeDataBase()
            print("Deserialization was done in StudentDataBaseProcessor")
        except:
            self.listOfStudent = []
            print("Create empty lists of students")

    def __del__(self):
        self.SerializeDataBase()
        print("Serialization was done in StudentDataBaseProcessor")


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
            return self.ConvertInListOfStudentsFromDict(listofstudents)

    def ConvertInListOfStudentsFromDict(self, listOfDictionaries):
        listOfStudents = []
        matches = next(item for item in listOfDictionaries)
        for each in listOfDictionaries:
            student = Student.Student(name=each["name"],
                              surname=each["surname"],
                              pid=each["pid"],
                              institute=each["institute"],
                              profession=each["profession"],
                              group=each["group"],
                              educationalLevel=each["educationalLevel"],
                              age=each["age"],
                              gpa=each["gpa"])
            listOfStudents.append(student)
            print(student)
        return listOfStudents
