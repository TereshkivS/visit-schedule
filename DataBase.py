import datetime

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
        sqlQuery = ("""
                    insert Persons
                    (person_id, first_name, last_name)
                    values
                    (?, ?, ?)
                    """)
        self.cursor.execute(sqlQuery, (pid, name, surname))
        self.connection.commit()

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

    def AddPersonEnter(self, pid):
        sqlQuery = ("""
                    insert Enters 
                    (person_id, room_id, enter_date)
                    values
                    (?, ?, GETDATE())
                    """)
        self.cursor.execute(sqlQuery, (pid, 1))
        self.connection.commit()

    def AddPersonExit(self, pid):
        sqlQuery = ("""
                    insert Exits 
                    (person_id, room_id, exit_date)
                    values
                    (?, ?, GETDATE())
                    """)
        self.cursor.execute(sqlQuery, (pid, 1))
        self.connection.commit()

    def GetListOfPersons(self):
        sqlQuery = ("""
                    select * from Persons
                """)
        self.cursor.execute(sqlQuery)
        results = self.cursor.fetchall()
        print(results)
        return results

    def CheckIfPersonIsInEnters(self, pid):
        sqlQuery = ("""
                    select * from Enters where person_id=?
                    """)
        pidList = (pid,)
        self.cursor.execute(sqlQuery, pidList)
        results = self.cursor.fetchall()
        if results:
            return True
        else:
            return False

    def IsValidEnter(self, pid):
        sqlQuery = ("""
                    select * from Exits where
                    exit_date>(select enter_date from Enters 
                    where enter_id=(select max(enter_id) from Enters 
                    where person_id=?))
                    """)
        pidList = (pid,)
        self.cursor.execute(sqlQuery, pidList)
        results = self.cursor.fetchall()
        print("Result table of IsValidEnter" + str(results))
        if results:
            return True
        else:
            return False

    def FixPersonsEnter(self, pid):
        if not self.CheckIfPersonIsInEnters(pid) or self.IsValidEnter(pid):
            self.AddPersonEnter(pid)

    def FixPersonsExit(self, pid):
        self.AddPersonExit(pid)

    def GetCurrentVisitorsList(self, date, time):
        dateTimeString = str(date.year()) + "-" + str(date.month()) + \
                         "-" + str(date.day()) + " " + str(time.hour()) \
                         + ":" + str(time.minute()) + ":" + str(time.second())
        print(dateTimeString)
        #sqlQuery = ("""
        #select person_id from Enters where enter_date>?
        #""")
        sqlQuery = ("""
        select first_name, last_name
        from Persons where
        person_id in (select person_id from Enters where enter_date > ?)""")
        self.cursor.execute(sqlQuery, (dateTimeString,))
        results = self.cursor.fetchall()
        return results



if __name__ == "__main__":
    db = DataBase()
    db.GetListOfPersons()

    #db.AddPersonExit(577055)
