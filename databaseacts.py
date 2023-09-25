from sqlite3 import InterfaceError
import mysql.connector
class databaseActs:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                database="membean",
                host="localhost",
                user="root",
                password="1234"
                )
            self.mycursor=self.mydb.cursor()
            self.connection = True
        except (InterfaceError, ConnectionRefusedError):
            print("Connection failed with the database")
            self.connection = False
    def checkExists(self, checkemail):
        self.mycursor.execute("SELECT email from users;")
        self.emailcheck = self.mycursor.fetchall()
        for em in self.emailcheck:
            if em[0] == checkemail:
                self.exists = True
                break
            else:
                self.exists = False
        if self.exists == True:
            return True
        else:
            return False
    def signUp(self, firstname,lastname,email,password):
        self.mycursor.execute("SELECT email from users")
        self.result = self.mycursor.fetchall()
        for x in self.result:
            print(x[0])
            if x[0] == email:
                self.upstatus = True
                break
            else:
                self.upstatus = False

        if self.upstatus == False:
            #later the password should be encrypted with the key stored externally and then passed into the database
            self.mycursor.execute(f"INSERT INTO users (FirstName, LastName, Email, Password, Status) values ('{firstname}','{lastname}', '{email}', '{password}', 0);")
            self.mydb.commit()
            print("Signup succesful")


    def signIn(self, inemail, inpassword):
        self.mycursor.execute(f"SELECT * FROM users where Email = '{inemail}' AND Password = '{inpassword}';")
        self.account = self.mycursor.fetchone()
        if self.account:
            return True
        else:
            return False
    def returnPassword(self, mail):
        self.mycursor.execute(f"SELECT Password FROM users WHERE Email = '{mail}'; ")
        self.resultt = self.mycursor.fetchone()
        return self.resultt
