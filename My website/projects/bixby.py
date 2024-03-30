import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import image
#import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!...I am Bixby....")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!...I am Bixby....")   

    else:
        speak("Good Evening!...I am Bixby....")  

    speak("Hello Sir ... How can i help you...")
    speak("Choose Your Option from the above")

    print("Choose Your Option from the above")

    print("Youtube\nGoogle\nImperial\nGmail\nRomantic song\nSad song\nLofi song\nBhajan\nDeshbhakti song\nItom song\nTMKOC\nSambalpuri gaana\nLearn\nDj\nParty song")
    print("Play music\nImage\nDirecter sir\nPatel sir\nMeher sir\n mam")

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        print("Say that again please...")  
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

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'imperial' in query:
            webbrowser.open("https://www.imperial.edu.in/")
            
        elif 'gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
            
        elif 'romantic song ' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=romantic+songs+hindi")
            
        elif 'sad song ' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=sad+songs+hindi+old")
            
        elif 'lofi songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=lofi+songs")
            
        elif 'bhajan' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=bhajan")
            
        elif 'desh bhaki song ' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=desh+bhakti+song")
            
        elif 'itom song ' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=itom+songs")
            
        elif 'tmkoc' in query:
            webbrowser.open("https://www.youtube.com/watch?v=p0dWoUvDGYw&list=PLPbh-P_C0BzRYOkpGxKL-6QmvYSL_ZuCu&ab_channel=TaarakMehtaKaOoltahChashmah")
            
        elif 'sambalpuri gaana' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=sambalpuri+song+")
            
        elif 'learn' in query:
            webbrowser.open("https://www.youtube.com/@GateSmashers")
            
        elif 'dj' in query:
            webbrowser.open("https://www.youtube.com/@djnyk")
            
        elif 'party song ' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=party+mashup")
            


        elif 'play music' in query:
            music_dir ='D:\BIKASH\HINDI GANE\AUDIO FILE mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'image' in query:
            image_dir = 'D:\BIKASH\IMAGE\College image'
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'director sir' in query:
            image_dir = "D:\BIKASH\IMAGE\College image\dire"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'mam' in query:
            image_dir = "D:\BIKASH\IMAGE\College image\mam"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'pritam sir' in query:
            image_dir = "D:\BIKASH\IMAGE\College image\pritam sir"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'meher sir' in query:
            image_dir = "D:\BIKASH\IMAGE\College image\meher sir"
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))



        elif'Send ' in query:

            number='+91 7438995127'
            kit.sendwhatmsg(
                number,
                'hello!', 11,20
                )

    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        else:
            print("thanks")
            speak("thanks")
