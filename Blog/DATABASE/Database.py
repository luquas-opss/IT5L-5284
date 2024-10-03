import mysql.connector

class Database:
    def __init__(self, HOST, USER, PASSWORD, DATABASE):
        self.DB = mysql.connector.connect(
            host = HOST, user = USER, password = PASSWORD, database = DATABASE
        )
        
    def CURSUR(self):
        return self.DB.cursur()