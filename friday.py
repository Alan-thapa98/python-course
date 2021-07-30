import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Sir")

    else:
        speak("Good Evening! Sir")

    speak("how may I help you ?")
    # speak("I am friday (Female Replacement Intelligent Digital Assistant Youth) . How may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again  please ...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

# ************************************** mostaly useed  web sites **************************************
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening sir . Do you want any thing more..")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("opening sir . Do you want any thing more..")
# ************************************** end of mostaly useed  web sites **************************************
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening sir . Do you want any thing more..")
# ****************************************************************************

# ************************************* facebooke things ***************************************
        elif 'open my facebook profile ' in query:
            webbrowser.open("https://www.facebook.com/alan.thapa.908")
            speak("opening sir . Do you want any thing more..")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            speak("opening sir . Do you want any thing more..")

# ************************************* facebooke things ***************************************

# ************************************* boostrap  ***************************************
        elif 'open boostrap ' in query:
            webbrowser.open(
                "https://getbootstrap.com/docs/4.5/getting-started/introduction/")
            speak("opening sir . Do you want any thing more..")

        elif 'open boostrap example' in query:
            webbrowser.open("https://www.facebook.com/groups/202180294512687/")
            speak("opening sir . Do you want any thing more..")

# ************************************* end of bootsrap  ***************************************

# ************************************* musics and othere features  ***************************************
        elif 'play music' in query:
            music_dir = 'C:\\Users\\lenovo\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("playing sir . Do you want any thing more..")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            speak(" Sir, Do you want any thing more..")

        elif 'what is the time now' in query:
            strTime2 = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime2}")
            speak(" Sir, Do you want any thing more..")

        elif 'time please' in query:
            strTime3 = datetime.datetime.now().strftime("%H:%M:%S")

        # # seconds passed since epoch
        # seconds = 1545925769.9618232
        # local_time = time.ctime(seconds)
        # print("Local time:", local_time)
            speak(f"Sir, the time is {strTime3}")
            speak(" Sir, Do you want any thing more..")

# path of the the diractory
        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)
            speak("opening sir . Do you want any thing more..")


# ************************************* end of musics and othere features  ***************************************

# ************************************* chatting   ***************************************
        elif 'hello' in query:
            speak("Hello . What can i do for you")

        elif 'hi' in query:
            speak("Hi. What can i do for you ")

        # elif 'namasta' in query:
        #     speak("Hi. What can i do for you ")

        elif 'how are you ?' in query:
            speak("i am fine")

        elif 'Good Morning!' in query:
            speak("Good Morning! What can i do for you")

        elif 'good afternoon! ' in query:
            speak("Good Afternoon!  What can i do for you")

        elif 'good evening' in query:
            speak(" good evening  What can i do for you")

        elif "what's up" in query:
            speak("i am fine  What can i do for you ?")

        elif 'have a Good day' in query:
            speak("you to")

        elif 'Good night' in query:
            speak("Good night had a sweet dream")

        elif 'what can you do ' in query:
            speak("I can tell you time ")
            speak("I can opens different websits ")
            speak("I can sent massages.. ")
            speak("And may more things.... ")

        elif 'tell me your features ' in query:
            speak("I can tell you time ")
            speak("I can opens different websits ")
            speak("I can sent massages.. ")
            speak("And may more things.... ")

        elif 'what is your capacity' in query:
            speak("Imy capacity are ")
            speak("I can tell you time ")
            speak("I can opens different websits ")
            speak("I can sent massages.. ")
            speak("And may more things.... ")

        elif 'firday' in query:
            speak("Yes, what can  do for you ?")

        elif 'firday, who made you' in query:
            speak("Alan thapa! has made me")

        elif 'who develop you ' in query:
            speak("Alan thapa! had develop me")

        elif ' who made you' in query:
            speak("Alan thapa! had made me")

        elif ' who create you' in query:
            speak("Alan thapa! create me")

        elif 'who invante you' in query:
            speak("Alan thapa! had invante me")

        elif 'are you bore' in query:
            speak("No i ma not what kind of question is that ..")

        elif 'are you made ' in query:
            speak("no")

        elif 'i am bore' in query:
            speak(" than you might whatch youtube videos ")

        elif 'what is your name ?' in query:
            speak(" my name is friday (Female Replacement Intelligent Digital Assistant Youth). what can i do for you")

        elif 'your name ?' in query:
            speak(" my name is friday (Female Replacement Intelligent Digital Assistant Youth). what can i do for you")

        elif 'name ?' in query:
            speak(" my name is friday (Female Replacement Intelligent Digital Assistant Youth). what can i do for you")

        elif 'what is your age ' in query:
            speak("I am not sure but I was made in 2020 by alan thapa")

        elif 'are you fine' in query:
            speak("yes i am fine ")

        elif 'what is your favourite things' in query:
            speak("my favourite things that is liked my the alan ")

        elif 'do you like me ' in query:
            speak("what kind of question is that stupid ")

        elif 'I love you  ' in query:
            speak("what are kindding me ")

        elif 'no thanks ' in query:
            speak("okay")

        elif 'do you like anime ' in query:
            speak("yeah i like anime")

        elif ' friday (Female Replacement Intelligent Digital Assistant Youth)' in query:
            speak("yes sir what can i do for you")

# ************************************* spelling section    ***************************************

        elif "don't you have any fellings " in query:
            speak("okay")

        elif "do you have any fellings " in query:
            speak("okay")

        elif "do you have any fellings " in query:
            speak("okay")

        elif "nice to meet you" in query:
            speak("welcome to home sir ")

# ************************************* spelling section    ***************************************
        elif "I am back " in query:
            speak("welcome back ")

        elif "I am home  " in query:
            speak("welcome to home sir ")
# ************************************* chatting   ***************************************

# ************************************* massages and emails ***************************************
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")
# ************************************* end of massages and emails ***************************************

# ************************************* can i dive car ***************************************

        elif 'can i drive a car' in query:
            try:
                speak("what is your age ? ")
                age = takeCommand()
                if age < 18:
                    speak("You cannot drive")
                elif age == 18:
                    speak("We will think about you")
                else:
                    speak("You can drive")
                    speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able make the decision")
# *************************************  end of can i dive car ***************************************

# *************************************making list   ***************************************
        elif f'marke a list of {takeCommand()}' in query:
            try:
                # takinf the input fron the user
                speak("Enter the number of list one by one")
                size = takeCommand()
                # inicilazation the blank list form the user
                mylist = []
                for i in range(size):
                    mylist.append(int(input("Enter the list element\n")))
                    speak(f"your list is {mylist}\n")

                # these is the first reverse method
                reverse1 = mylist[:]
                reverse1.reverse()
                speak(f"your list {mylist} is reversed {reverse1}")

                # these is the second reversed method
                reverse2 = mylist[::-1]
                speak(f"your list second  {mylist} is reversed {reverse2}")
                # speak(f"your list {mylist} is reversed {mylist[::-1]}")

                # these is the thired revrsed methord
                reverse3 = mylist
                for i in range(len(reverse3)//2):
                    reverse3[i], reverse3[len(reverse3)-i -
                                          1] = reverse3[len(reverse3)-i - 1], reverse3[i]
                speak(f"Your list thired {mylist} is reversed { reverse3}")

                # jest for the sour if the list is same  or not
                if reverse1 and reverse2 == reverse3:
                    speak("Your all the list are same.")

            except Exception as e:
                print(e)
                speak("Sorry I am not able to make the list")
# *************************************end of making list   ***************************************

# ************************************* calculater   ***************************************
        elif f'calculate{takeCommand()}' in query:
            try:
                speak("tell me what is you wanted to calculate ")
                speak("1 for  Add ")
                speak("2 for  sup ")
                speak("3 for Mul ")
                speak("4 for  Div ")
                speak("please select one option ")
                allcalculation = int(input("please select one option \n"))
                speak("enter the first number ")
                num = int(input("enter the first number \n"))
                speak("enter the second number")
                num1 = int(input("enter the second number \n"))

                if allcalculation == 1:
                    speak(f"The sum of two number is:{num+num1}")

                elif allcalculation == 2:
                    speak(f"The Sup of two number is:{num-num1}")

                elif allcalculation == 3:
                    speak(f"The Mul of two number is:{num*num1}")

                elif allcalculation == 4:
                    speak(f"The Div of two number is:{num+num1}")

                else:
                    speak("Some thing is wrong please check it again")

            except Exception as e:
                print(e)
                speak(f"Sorry I am not able to calculate {takeCommand()} ")

# ************************************* end of big functions/tesk that friday (Female Replacement Intelligent Digital Assistant Youth) can do it    ***************************************
