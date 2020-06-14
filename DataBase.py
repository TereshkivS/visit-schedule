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

    def GetListOfPersons(self):
        sqlQuery = ("""
                    select * from Persons
                """)
        self.cursor.execute(sqlQuery)
        results = self.cursor.fetchall()
        print(results)
        return results

    def CheckIfPersonIsInExits(self, pid):
        sqlQuery = ("""
                            select * from Exits where person_id=?
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

    def IsValidExit(self, pid):
        sqlQuery = ("""select * from Enters where 
            enter_date>(select exit_date from Exits 
            where exit_id=(select max(exit_id) from Exits 
            where person_id=?))""")
        pidList = (pid,)
        self.cursor.execute(sqlQuery, pidList)
        results = self.cursor.fetchall()
        print("Result table of IsValidExit" + str(results))
        if results:
            return True
        else:
            return False

    def FixPersonsEnter(self, pid):
        if not self.CheckIfPersonIsInEnters(pid) or self.IsValidEnter(pid):
            self.AddPersonEnter(pid)
            nameAndSurname = self.GetPersonNames(pid)
            self.AddToResultEntersExits(nameAndSurname[0])

    def FixPersonsExit(self, pid):
        if not self.CheckIfPersonIsInExits(pid) or self.IsValidExit(pid):
            self.AddPersonExit(pid)
            nameAndSurname = self.GetPersonNames(pid)
            self.AppendToResultEntersExits(nameAndSurname[0])

    def GetCurrentVisitorsList(self, date, timeBefore, timeAfter):
        dateTimeStringBefore = str(date.year()) + "-" + str(date.month()) + \
                         "-" + str(date.day()) + " " + str(timeBefore.hour()) \
                         + ":" + str(timeBefore.minute()) + ":" + str(timeBefore.second())
        dateTimeStringAfter = str(date.year()) + "-" + str(date.month()) + \
                               "-" + str(date.day()) + " " + str(timeAfter.hour()) \
                               + ":" + str(timeAfter.minute()) + ":" + str(timeAfter.second())
        print("Before date = " + dateTimeStringBefore)
        print("After date = " + dateTimeStringAfter)
        #sqlQuery = ("""
        #select person_id from Enters where enter_date>?
        #""")
        sqlQuery = ("""
        select * from ResultEntersExits where (enter_date > ? and exit_date < ?) or (enter_date > ? )""")
        self.cursor.execute(sqlQuery, (dateTimeStringBefore, dateTimeStringAfter, dateTimeStringBefore))
        results = self.cursor.fetchall()
        print("Result query table")
        print(results)
        return results

    def GetPersonNames(self, pid):
        sqlQuery = ("""
                select first_name, last_name
                from Persons where person_id = ?
                        """)
        pidList = (pid,)
        self.cursor.execute(sqlQuery, pidList)
        results = self.cursor.fetchall()
        print(results)
        return results

    def AddToResultEntersExits(self, nameAndSurname):
        sqlQuery = ("""
        insert ResultEntersExits 
        (first_name, last_name, enter_date)
        values
        (?, ?, GETDATE())""")
        self.cursor.execute(sqlQuery, (nameAndSurname[0], nameAndSurname[1]))
        self.connection.commit()

    def AppendToResultEntersExits(self, nameAndSurname):
        sqlQuery = ("""
        update ResultEntersExits
        set exit_date = GETDATE()
        where table_id=(select max(table_id) from ResultEntersExits
        where first_name=? and last_name=?)
        """)
        self.cursor.execute(sqlQuery, (nameAndSurname[0], nameAndSurname[1]))
        self.connection.commit()

if __name__ == "__main__":
    db = DataBase()
    db.GetListOfPersons()

    #db.GetPersonNames(676251)
