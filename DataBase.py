import pypyodbc


class DataBase():
    def __init__(self):
        self.sqlServerName = "DESKTOP-02ADUN4\\SQLEXPRESS01"
        self.dataBaseName = "WorkerRegistterDB"
        self.connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + self.sqlServerName + ';'
                              'Database=' + self.dataBaseName + ';')
        self.cursor = self.connection.cursor()

    def AddPersonToDB(self, pid, name, surname):
        try:
            sqlQuery = ("""
                    insert Persons
                    (person_id, first_name, last_name)
                    values
                    (?, ?, ?)
                    """)
            self.cursor.execute(sqlQuery, (pid, name, surname))
            self.connection.commit()
        except pypyodbc.IntegrityError:
            print("Already exists item with the ", pid , "id")


    def AddStudentToDB(self, pid, name, surname, group):
        self.AddPersonToDB(pid, name, surname)
        sqlQuery = ("""
                insert Students
                (student_id, group_name)
                values
                (?, ?)
                """)
        self.cursor.execute(sqlQuery, (pid, group))
        self.connection.commit()

    def AddTeacherToDB(self, pid, name, surname, department, profession):
        self.AddPersonToDB(pid, name, surname)
        sqlQuery = ("""
                insert Teachers
                (teacher_id, department, profession)
                values
                (?, ?, ?)
                """)
        self.cursor.execute(sqlQuery, (pid, department, profession))
        self.connection.commit()

    def AddWorkerToDB(self, pid, name, surname, department):
        self.AddPersonToDB(pid, name, surname)
        sqlQuery = ("""
                insert Worker
                (worker_id, department)
                values
                (?, ?)
                """)
        self.cursor.execute(sqlQuery, (pid, department))
        self.connection.commit()