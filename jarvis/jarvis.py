
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)

    if hour>0 and hour<12:
        speak(" Good morning anay.")
    elif hour>12 and hour<17:
        speak("good afternoon anay")
    else:
        speak("good evening anay")
    speak(" friday is here in your service. What can i do for you..")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=0.8
        
        audio= r.listen(source)

    try:
        print("Trying to recognize...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")




    except Exception as e:
        #print(e)
        print("unable to recognise. could you please repeat..")
        return "none"
   
    return query 

    
if __name__ == "__main__":
    wishme()

    while(1):

        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("please wait while i m searching wiki.")
            query=query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
        elif  'youtube' in query:
            webbrowser.open("youtube.com")
            
        elif  'google' in query:
            webbrowser.open("google.com")


        elif  'song' in query:
            webbrowser.open("https://music.youtube.com/watch?v=iMW4rNtKjQ4&list=RDAMVMiMW4rNtKjQ4")


        elif 'time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"current time is {strtime}")

        elif 'vs code' in query:
            path= "C:\\Users\\anayj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'quit' in query or 'bye' in query or 'exit' in query:
            speak("..ok bye...have a nice day")
            exit()


        elif 'hi' in query or 'hey' in query or 'friday' in query  :
            speak("Hey anay whatsup...how you doing....what can i do for you")

       




       
