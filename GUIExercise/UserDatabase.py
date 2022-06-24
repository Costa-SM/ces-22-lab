import sqlite3

class UserDatabase():
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.createTable()

    def createTable(self):
        c = self.connection.cursor()

        c.execute("""create table if not exists users(
                     id_user integer primary key autoincrement,
                     name text,
                     login text,
                     password text,
                     email text,
                     address text,
                     cellphone text)""")
        self.connection.commit()
        c.close()

    def verify_user(self, login, password, error_msg):
        if(len(login) == 0 or len(password) == 0):
                error_msg['foreground'] = '#f00'
                error_msg['text'] = 'Some fields are empty!'
                return False
        
        try:
            c = self.connection.cursor()
            
            for row in c.execute("select * from users where login = :user_log", {"user_log": login}):
                if(row[2]== login and row[3] == password):
                    error_msg['text'] = 'User logged in !'
                    error_msg['foreground'] = '#0f0'
                    return True
        
            error_msg['foreground'] = '#f00'
            error_msg['text'] = 'Incorrect password!'
            return False
        except:
            error_msg['text'] = 'User not registered'

    def existing_user(self, login):
        try:
            c = self.connection.cursor()
            
            for row in c.execute("select * from users where login = ?", (login)):
                if(not row):
                    return False
            
            c.close()

            return True
        
        except:
            return False

    def new_registration(self, name, address, cellphone, email, login, password):
        c = self.connection.cursor()
        c.execute("""INSERT INTO users (name, login, password, email, address, cellphone) 
                    values(?, ?, ?, ?, ?, ?)""", (name, login, password, email, address, cellphone))
