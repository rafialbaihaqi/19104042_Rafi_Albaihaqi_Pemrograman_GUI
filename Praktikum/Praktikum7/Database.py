from PyQt5.QtSql import*

def connectdb():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()

        sql = '''Create TABLE Phonebook(
            id INT not null primary key,
            nama VARCHAR(25),
            no_hp VARCHAR(15)
        )'''
        query.exec_(sql)
        if(query.exec_):
            print('Berhasil Create Table')

    else:
        print('ERROR: ' + db.lastError().text())

connectdb()