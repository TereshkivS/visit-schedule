import json
import Student

class DataBaseProcessor:
    def __init__(self):
        self.listOfStudent = []


    def AppendStudent(self, student):
        self.listOfStudent.append(student)

    def SerializeDataBase(self, students):
        json.
