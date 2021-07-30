import pyttsx3
import speech_recognition 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# these is the set up of speak section ok 

speak("tell me what is you wanted to calculate ")
speak("1 for  Add ")
speak("2 for  sup ")
speak("3 for Mul ")
speak("4 for  Div ")
speak("please select one option ")

print("tell me what is you want to do")
print("1 for  Add ")
print("2 for  sup ")
print("3 for Mul ")
print("4 for  Div ")
print("please select one option to which you wanted to calcutation ")

allcalculation=int(input("please select one option \n"))
speak("enter the first number ")
num=int(input("enter the first number \n"))
speak("enter the second number")
num1=int(input("enter the second number \n"))

if allcalculation==1:
    speak(f"The sum of two number is:{num+num1}" )
    print("The sum of two number is:" ,num+num1 )

elif allcalculation==2:
    speak(f"The Sup of two number is:{num-num1}" )
    print("The Sup of two number is:" ,num-num1 )

elif allcalculation==3:
    speak(f"The Mul of two number is:{num*num1}" )
    print("The Mul of two number is:" ,num*num1 )

elif allcalculation==4:
    speak(f"The Div of two number is:{num+num1}" )
    print("The Div of two number is:" ,num/num1 )

else:
    speak("Some thing is wrong please check it again")
    print("Some thing is wrong please check it again")

# there is another section of function

print()
print("Hope you like My calculater")
speak("There are many othere feature on these program")
speak("If like get visit . you can also get many information on these program.")
print("If you are interested on all our  function please enter 1 \n")
speak("Please enter 1  number to get more info:")
inputfun=int(input("Please enter 1  number to get more info:\n"))

            
