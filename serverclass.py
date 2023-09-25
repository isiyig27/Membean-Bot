from http.server import BaseHTTPRequestHandler, HTTPServer
from mysql.connector.errors import InterfaceError
from urllib.parse import parse_qs, parse_qsl
from databaseacts import databaseActs
from Membean_Bot import startMembeanSession
import threading
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/signup.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("signup.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/membean.png":
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            with open("membean.png","rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/signin.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("signin.html","rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/bot.png":
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            with open("bot.png","rb") as file:
                self.wfile.write(file.read())
        else:
            print("else")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

    def do_POST(self):
        #handling database connection error
        try:
            self.db = databaseActs()
        except InterfaceError:
            print("Connection Failed")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("connectionerror.html", "rb") as file:
                self.wfile.write(file.read())

        print("post")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        if self.path=="/signup.html":
            print("Handling Signup ..")
            self.handle_signup(params)
            if self.handle_signup(params) == False:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Email already exists in the database !!!")
        elif self.path=="/signin.html":
            self.handle_signin(params)
        else:
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.wfile.write(b"Not Found !!!")
    def handle_signup(self, params):
        name = params['name'][0]
        surname = params['surname'][0]
        email = params['email'][0]
        password = params['password'][0]
        print(name, surname, email, password)
        self.db.signUp(name,surname,email,password)
        if self.db.upstatus == True:
            print("Email already exists !!!")
            return False

    def handle_signin(self, params):
        signinemail = params["email"][0]
        signinpassword = params["password"][0]
        print(signinemail, signinpassword)
        print("signin")
        if self.db.signIn(signinemail,signinpassword) == True:
            print("Login succesful")


        else:
            print("Incorrect password or email")
            



