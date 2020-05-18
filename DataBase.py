import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                              'Database=test;'
                              'PORT=1433')

cursor = connection.cursor()