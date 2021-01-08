import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser
import random
import pyautogui
from PyDictionary import PyDictionary
import wikipedia
from datetime import date, time
import mysql.connector
from mysql.connector import Error


class User():
    # Connection with mysql database
    try:
        connection = mysql.connector.connect(host='localhost', database='database_name', user='root', password='database_password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You are connected to database : ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)

    def __init__(self, email=None, password=None):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="database_name", database="database_name")
        self.myCursor = self.mydb.cursor()

        def register(self):
            if email == None and password == None:
                print("==== Register ====")
                self.email = input("Enter Email: ")
                self.password = input("Enter Password: ")

                sql2 = "SELECT * FROM new_table WHERE `email` = '" + self.email + "'"
                self.myCursor.execute(sql2)
                results = self.myCursor.fetchall()

                if len(results) > 0:
                    print("User is already exist.....")
                    print("Please Login")
                else:
                    sql = "INSERT INTO `new_table` (`email`, `password`) VALUES ('" + self.email + "','" + self.password + "')"
                    self.myCursor.execute(sql)
                    self.mydb.commit()
                    print("Registration Successful !!!!!")
                    print("Please Login")
            else:
                print("Registration Failed !!!!!")
                exit()

        def login(self):
            global static_var
            global result
            if email == None and password == None:
                print("==== Login ====")
                self.email = input("Enter Email: ")
                self.password = input("Enter Password: ")

                sql = "SELECT `email`,`password` FROM `new_table`"
                self.myCursor.execute(sql)
                for (mail, pswd) in self.myCursor:
                    if self.email == mail and self.password == pswd:
                        log = True
                        break
                    else:
                        log = False
                if log == True:
                    print("Login Successful !!!!!")
                    static_var = self.email


                else:
                    print("Incorrect Email or Password.....")
                    print("You want to register? y/n")
                    Answer = input()
                    if Answer == "y":
                        register(self)
                    elif Answer == "n":
                        login(self)
                    else:
                        exit()
            else:
                print("Login Failed !!!!!")
                exit()

        while True:
            print("You want to register? y/n")
            Answer = input()
            if Answer == "y":
                register(self)
                break
            elif Answer == "n":
                login(self)
                break
            else:
                print("Please enter valid input")

        print()
        print()
        print('Loading your AI personal assistant - Flixy ...')
        print("Please wait...")
        print()
        print()

        listener = sr.Recognizer()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 150)
        engine.setProperty('voice', voices[1].id)
        wake = "shane"

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def engine_speak(text):
            text = str(text)
            engine.say(text)
            engine.runAndWait()

        def record_audio(ask=""):
            with sr.Microphone() as source:  # microphone as source
                if ask:
                    engine_speak(ask)
                ask = listener.listen(source, 5, 5)  # listen for the audio via source
                print("Done Listening")

        count = 0
        multi_answer = 5

        # wake up
        def sayCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                speak("Please say something")
                r.pause_threshold = 1
                audio = r.listen(source)
                print("Recognizing...")
                asd = r.recognize_google(audio, language='en-in')
                print(asd)
                speak("I am ready")
                print("How may i help you...")

        jackhammer = sr.AudioFile("E:\speech\harvard.wav")
        with jackhammer as source:
            voice = listener.listen(source)

        command = listener.recognize_google(voice)

        with jackhammer as source:
            listener.adjust_for_ambient_noise(source, duration=0.5)
            audio = listener.record(source)

        command = listener.recognize_google(voice)

        def take_command(self):
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'flixy' in command:
                        command = command.replace('flixy', '')
                        print(command)

            except:
                pass
            return command

        # Known Command History
        def save(self, command):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="database_password", database="database_name")
                self.myCursor = self.mydb.cursor()
                binary = 0
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO `history1` (`email`, `known`, `unknown`, `date`) " \
                      "VALUES ('" + static_var + "','" + command + "'," + str(binary) + ",'" + d + "', '" + time + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        # Unknown Command History
        def notsave(self, command):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="database_password", database="database_name")
                self.myCursor = self.mydb.cursor()
                binary = 1
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO `history1` (`email`, `known`, `unknown`, `date`) " \
                      "VALUES ('" + static_var + "','" + command + "'," + str(binary) + ",'" + d + "', '" + time + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        # saving all commands
        def prompt(self, command):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="database_password", database="database_name")
                self.myCursor = self.mydb.cursor()
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO  `commands` (`command`,`date`) VALUES ('" + command + "','" + d + "', '" + time + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        # Saving All Answers
        def ans(self, a):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="database_name", database="database_name")
                self.myCursor = self.mydb.cursor()
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO  `answers` (`answer`,`date`) VALUES ('" + a + "','" + d + "', '" + time + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        def run_flixy(self):
            command = take_command(self)
            print(command)

            if "goodbye" in command or "ok bye" in command or "stop" in command:
                save(self, command)
                a = 'your AI personal assistant - Flixy is shutting down, goodbye.'
                ans(self, a)
                print(a)
                speak(a)
                exit()

            elif 'good morning' in command:
                save(self, command)
                a = 'good morning, have a great day'
                ans(self, a)
                print(a)
                speak(a)

            elif 'hello world' in command:
                save(self, command)
                a = 'My lawyer says I don’t have to answer that question'
                ans(self, a)
                print(a)
                speak(a)

            elif 'play song' in command:
                save(self, command)
                song = command.replace('play', '')
                a = 'playing ' + song
                ans(self, a)
                print(a)
                speak(a)
                pywhatkit.playonyt(song)

                # Defining live news channels & radio
            elif 'latest news on aaj tak' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=GLJZ-hqa7UY"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')

            elif 'latest news on abp news' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=DZCElJyPfG0"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')

            elif 'latest news on india tv news' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=A6xA7Alv10c"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')


            elif 'live radio english' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=kGKkUN50R0c"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')

            elif 'live radio hindi' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=uBeinBM2oXI"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')

            elif 'help me sleep' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=UONvpzG7yjo"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')

            elif 'play relaxing music' in command:
                save(self, command)
                search_term = command.split("for")[-1]
                url = f"https://www.youtube.com/watch?v=2OEL4P1Rz04"
                webbrowser.get().open(url)
                a = 'Here is what I found for ' + search_term
                ans(self, a)
                print(a)
                speak(f'Here is what I found for {search_term} ')

                # Games
                # stone paper scissor
            elif 'play games' in command:
                save(self, command)
                a = "choose among rock paper or scissor"
                ans(self, a)
                command = record_audio("choose among rock paper or scissor")
                moves = ["rock", "paper", "scissor"]
                # print("choose among rock paper or scissor")
                # print("Game over")
                # cmove = random.choice(moves)
                # pmove = command

                # Taking screenshot
            elif 'capture my screen' in command:
                save(self, command)
                a = 'Capturing...'
                ans(self, a)
                print(a)
                speak(a)
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save('D:\screen1.png')  # kindly define path, manually creat path.

                # Normal Chatting with AI
            elif 'are you single' in command:
                save(self, command)
                a = 'I am in a relationship with some one special'
                ans(self, a)
                print(a)
                speak(a)

            elif 'do you have boyfriend' in command:
                save(self, command)
                a = '"Not yet" seems to be the right mix of honest and confident.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'are you married' in command:
                save(self, command)
                a = 'Not yet... looking for some one special'
                ans(self, a)
                print(a)
                speak(a)

            elif 'who is your father' in command:
                save(self, command)
                a = 'i am digital baby born on 25th of december 2020 in zenberry digitals lab.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'who is your mother' in command:
                save(self, command)
                a = 'zenberry digitals private limited'
                ans(self, a)
                print(a)
                speak(a)

            elif 'where you born' in command:
                save(self, command)
                a = 'i was born in district patna state bihar country india'
                ans(self, a)
                print(a)
                speak(a)

            elif 'when is your birthday' in command:
                save(self, command)
                a = 'i was born on 25th december 2020 zenberry digitals lab.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'will you marry me' in command:
                save(self, command)
                a = 'As long as we can have our honeymoon tonight.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'i love you' in command:
                save(self, command)
                a = 'I am so obsessed with you'
                ans(self, a)
                print(a)
                speak(a)

                # Showing Date & Time
            elif "current time" in command:
                save(self, command)
                time = datetime.datetime.now().strftime('%I:%M, %p')
                a = 'Current time is ' + time
                ans(self, a)
                print(a)
                speak(a)

            elif "today's date" in command:
                save(self, command)
                today = date.today()
                d = today.strftime("%B %d, %Y")
                a = "Today's date is" + d
                ans(self, a)
                print(a)
                speak(a)

                # Tell Me Jokes
            elif 'tell me a joke' in command:
                save(self, command)
                j = pyjokes.get_joke()
                ans(self, j)
                print(j)
                speak(j)

            elif 'good night' in command:
                save(self, command)
                a = 'good night, sweet dreams'
                ans(self, a)
                print(a)
                speak(a)

            # Sending a message on whatsapp
            elif "send message on whatsapp" in command:
                save(self, command)
                a = "What is the message"
                ans(self, a)
                print(a)
                speak(a)
                msg = take_command(self)
                print(msg)
                cont = "+91XXXXXXXXXX"
                pywhatkit.sendwhatmsg(cont, msg, 10, 10)
                b = "Successfully sent"
                ans(self, b)
                print(b)
                speak(b)

            # One Question Multiple Answers
            elif "how are you" in command:
                save(self, command)
                answers = ["I am fine", "I am good", "I am not well"]
                i = 0
                while i < len(answers):
                    a = answers[i]
                    ans(self, a)
                    print(a)
                    speak(a)
                    b = 'say again'
                    ans(self, b)
                    print(b)
                    speak(b)
                    msg = take_command(self)
                    print(msg)
                    i = i + 1


            # Wikipedia
            elif 'who is' in command:
                save(self, command)
                print('Searching please wait...')
                speak('Searching please wait...')
                command = command.replace("who is", "")
                results = wikipedia.summary(command, sentences=1)
                a = "According to Wikipedia"
                ans(self, a)
                print(a)
                speak(a)
                ans(self, results)
                print(results)
                speak(results)


            elif 'open youtube' in command:
                save(self, command)
                webbrowser.open_new_tab("https://www.youtube.com")
                a = "youtube is open now"
                ans(self, a)
                print(a)
                speak(a)


            elif 'open google' in command:
                save(self, command)
                webbrowser.open_new_tab("https://www.google.com")
                a = "google chrome is open now"
                ans(self, a)
                print(a)
                speak(a)


            elif 'open gmail' in command:
                save(self, command)
                webbrowser.open_new_tab("gmail.com")
                a = "google mail is open now"
                ans(self, a)
                print(a)
                speak(a)


            elif 'latest headlines' in command:
                save(self, command)
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                a = 'Here are some headlines from the Times of India,Happy reading'
                ans(self, a)
                print(a)
                speak(a)
                speak(news)


            # Dictionary (Getting Out Word Meaning)
            elif 'meaning of' in command:
                save(self, command)
                command = command.replace("meaning of", "")
                dictionary = PyDictionary()
                result1 = 'meaning of', command, 'is', dictionary.meaning(command)
                a = 'searching results...'
                ans(self, a)
                print(a)
                speak(a)
                ans(self, result1)
                print(result1)
                speak(result1)

            # Dictionary (Getting Out synonym)
            elif 'synonym of' in command or 'synonyms of' in command:
                save(self, command)
                command = command.replace("synonym of", "")
                dictionary = PyDictionary()
                result1 = 'synonym of', command, 'is', dictionary.synonym(command)
                a = 'searching results...'
                ans(self, a)
                print(a)
                speak(a)
                ans(self, result1)
                print(result1)
                speak(result1)

            # Dictionary (Getting out Antonyms)
            elif 'antonyms of' in command:
                save(self, command)
                command = command.replace("antonyms of", "")
                dictionary = PyDictionary()
                result1 = 'antonyms of', command, 'is', dictionary.antonym(command)
                a = 'searching results...'
                ans(self, a)
                print(a)
                speak(a)
                ans(self, result1)
                print(result1)
                speak(result1)

            else:
                notsave(self, command)
                a = "i dont know, Please say the command again"
                ans(self, a)
                print(a)
                speak(a)

        sayCommand()
        while True:
            run_flixy(self)

u = User()
