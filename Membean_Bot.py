from pickle import TRUE
from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import random
import openai
import sys
from databaseacts import databaseActs
def startMembeanSession(email, password):
    options = Options()
    options.headless = True
    service = Service()
    driver = webdriver.Chrome(service = service, options = options)
    openai.api_key= "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"
    gptmessages = [
        {"role": "system", "content": "you are a question solver"}
        ]
    new=2
    abc=[]
    word="a"
    choicelist=[]
    i=0
    global ct
    ct=0
    try:
        def executeSolveQuestionNormal():
            print("Solving Question ..")
            data = "Solving Question .."
            choices=[]
            choicee=None
            choice=None
            time.sleep(4)
            question=driver.find_element(By.CLASS_NAME,"question").text
            choices=driver.find_elements(By.CLASS_NAME,"choice ")
            optiona=choices[0].text
            optionb=choices[1].text
            optionc=choices[2].text
            optiond=choices[3].text
            chatgptquestion = "Question = "+question+"\n A) "+optiona+"\n B) "+optionb+"\n C) "+optionc+"\n D) "+optiond+"\n Only answer with the letters A,B,C or D: "
            print(chatgptquestion)
            data = chatgptquestion
            gptmessages.append({"role": "user", "content": chatgptquestion})
            completion = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
             messages=gptmessages
            )
            answer = completion.choices[0].message.content
            print("answer= ", answer)
            data = "answer= ", answer
            try:
                a=answer.index(")")
            except ValueError:
                try:
                    a=answer.index(":")
                    a+=3
                except ValueError:
                    a=1
            answerid = answer[a-1].lower()
            if answerid == "a":
                choices[0].click()
            elif answerid == "b":
                choices[1].click()
            elif answerid == "c":
                choices[2].click()
            elif answerid == "d":
                choices[3].click()
            else:
                print("Invalid answer, answering as A")
                data = "Invalid answer, answering as A"
                choices[0].click()
            print("Question answered as ", answer[a-1])
            data = "Question answered as ", answer[a-1]
            time.sleep(3)
        def check_constellation_question():
                try:
                    driver.find_element(By.XPATH,"//img[@alt = 'constellation question']")
                except NoSuchElementException:                                                                             
                    return False
                return True
        def check_exists_by_class(classs):
            try:
                driver.find_element(By.CLASS_NAME,classs)
            except NoSuchElementException:
                return False
            return True
        def check_exists_by_id(id):
            try:
                driver.find_element("id",id)
            except NoSuchElementException:
                return False
            return True
        def mainFunction():
            global login
            global ct
            url = "https://membean.com/training_sessions/new"
            driver.get(url)
            print("a")
            driver.find_element("id", "username").send_keys(email)
            driver.find_element("id", "password").send_keys(password)
            driver.find_element(By.XPATH,'//*[@id="login"]/div[4]/button').click()
            time.sleep(3)
            if check_exists_by_id("Proceed")==True:
                print("Login Succesful")
                login = True
                data = "Login Succesful"
                driver.find_element("id","Proceed").click()
            while i==0:
                ct += 1
                randomisedvalue=random.randint(30,45)
                time.sleep(4.5)
                if check_exists_by_class("choice.answer")==True:
                    if ct==1:
                        print("Login Succesful")
                        login=True
                    print("Study section")
                    data = "Study section"
                    time.sleep(3)
                    word=driver.find_element(By.CLASS_NAME,"wordform").text
                    driver.find_element(By.CLASS_NAME,'choice.answer').click()
                    print("Question answered")
                    data = "Question answered"
                    print(f"Waiting {randomisedvalue} seconds before proceeding")
                    data = (f"Waiting {randomisedvalue} seconds before proceeding")
                    time.sleep(randomisedvalue)
                    driver.find_element("id","next-btn").click()
                    print("Next button clicked")
                    data = "Next button clicked"
                    time.sleep(2)
                elif check_constellation_question()==True:
                    if ct==1:
                        print("Login Succesful")
                        data = "Login Succesful"
                        login=True
                    choices=driver.find_elements(By.CLASS_NAME,"choice ")
                    print("Constellation question, answering as A")
                    data = "Constellation question, answering as A"
                    time.sleep(2)
                    choices[0].click
                elif check_exists_by_class("letter-wrapper"):
                    if ct==1:
                        print("Login Succesful")
                        data = "Login Succesful"
                        login=True
                    print("Wrting question")
                    data = "Writing question"
                    for char in word:
                        driver.find_element("id", "choice").send_keys(char)
                        time.sleep(0.3)
                    print("Ansered as ", word) 
                    data = "Ansered as ", word
                elif check_exists_by_id("Click_me_to_stop"):
                    if ct==1:
                        print("Login Succesful")
                        data = "Login Succesful"
                        login=True
                    print("Session end")
                    data = "Session end"
                    driver.find_element("id","Click_me_to_stop").click()
                    time.sleep(2)
                    driver.close()
                    print("Session ended")
                    data = "Session ended"
                    break
                else:
                    if ct==1:
                        print("Login Succesful")
                        data = "Login Succesful"
                        login=True
                    executeSolveQuestionNormal()
        mainFunction()
    except:
        if login==False:
            print(f"Login Failed with these crede ntials email: {email}, password: {password}")
            data = "fLogin Failed with these credentials email: {email}, password: {password}"
            time.sleep(2)
        print("Code has ended with an error")
        data = "Code has ended with an error"
        time.sleep(2)
        print(sys.exc_info())
        data = sys.exc_info()
        time.sleep(2)
        data = 31
def return_data():
    print("yes")
    return data

db = databaseActs()
passs = db.returnPassword("aykefe.27@robcol.k12.tr")
startMembeanSession("aykefe.27@robcol.k12.tr", passs[0])