
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Agrim")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Agrim")
    else:
        speak("Good Evening Agrim")
    speak("I am Dramiti. Sive Dramiti. How may I help you")




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :    
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print("User said: "+ query)
    except Exception as e:
        print("Please say that again..")
        return "None"
    return query


def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('email@gmail.com','password123') #login credentials of the account to sentd the mail through
    server.sendmail('email@gamil.com',to,content)
    server.stop


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Wikipedia information gatherer
        if 'wikipedia' in query:
            speak('Searching in Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(resutls)
            speak(results)
            #Opening various websites on command
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open my github ' in query:
            webbrowser.open("github.com/agrimbishnoi")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.com")
        #Playing music
        elif 'play music' in query:
            music_dir = ''#Directory in which all music files are placed
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,song[0]))
        #insult of jarvi
        elif 'who jarvis' in query:
            speak("Jarvis is a cheap rip of version of mine. I request you not to mention him in front of me again.")
        #Time inquiry
        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is" ,strTime)
        #opening code editior
        elif 'open code' in query:
            code_path = ""#Path/target of code editior at 'properties/detailes'
            os.startfile(code_path)
        elif 'emain to papa' in query :
            try:
                speak("What should I say? ")
                content = takeCommand()
                to = ""# email of reciever 
                speak = f"Do you want to send mail saying {content} to {to} Say in yes or no."
                permission = takeCommand()
                if permission.lower() == 'yes':
                    sendMail(to,content)
                    speak("Mail successfully sent")
                elif permission == 'no' :
                    speak("Mail aborted")
                else:
                    speak("Sorry i did not get what you said. Mail aborted")
            except Exception as e:
                speak("Error occured.Could not send the mail. error code is excepterroratmail")
        else:
            speak("Sorry that is not in my knowledge. Cause i am under development")






