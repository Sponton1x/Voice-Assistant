import datetime
import random
import sys
import webbrowser
import pyttsx3
import requests
import wikipedia
import win10toast_persist
import wolframalpha
from func import randoming, createTable, insert, cmd

# for voice in voices:
#    print(voice.id)

client = wolframalpha.Client('Your_App_ID')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voices = engine.setProperty('rete', 200)
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")


# for voice in voices:
#    print(voice.id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Sir!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

greetMe()
speak("How I can help you")


if __name__ == '__main__':

    while True:

        query = input()
        query = query.lower()

        if 'open facebook' in query:
            speak('sure')
            webbrowser.open('www.fb.com')

        elif 'open google' in query:
            speak('for sir always')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ["I'm boring in virtual world ", "fine", 'cool', "I'm full energy"]
            speak(random.choice(stMsgs))

        elif 'lock screen' in query:
            import ctypes
            ctypes.windll.user32.LockWorkStation()


        elif 'close' in query or 'quit' in query or 'stop' in query:
            says = [f"Jarvis Quiting ,have a good day ", "Sure", f'Closing the program ,have a good day',
                    f"Stopping the program ,have a good day"]
            speak(randoming(says))
            sys.exit()


        elif 'who are you' in query:
            says = ["Let me to introduce myself. I am Jarvis and your personal voice assistant.", "I am Virtual Voice Assistent has been written by Sponton", "My owner is Sponton and I am his assistent"]
            speak(randoming(says))

        elif 'hello' in query or 'hi' in query:
            says = ["hi sir, good day", "hello, how are you"]
            speak(randoming(says))

        elif 'good' in query or 'fine' in query or 'ok' in query:
            speak("So good, if you will need me say Jarvis")

        elif 'time' in query:
            currTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current Time is {currTime}")

        elif "what's the weather" in query:
            with open("api_keys.txt", 'r') as f:
                api_keys = f.read()

            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            city = "Łódź"
            complete_url = base_url + city + "&appid=" + api_keys
            responde = requests.get(complete_url)
            x = responde.json()
            y = x['main']
            temp = y['temp']
            feels_like = y['feels_like']
            pressure = y['pressure']
            humidity = y['humidity']
            today = datetime.datetime.now().strftime("%d/%m/%Y")
            toaster = win10toast_persist.ToastNotifier()
            toaster.show_toast(f"The weather on {today}", "Temperature:" + str(round(temp - 273.15)) + "°C" +
                               "\nFeel Temperature:" + str(round(feels_like - 273.15)) + "°C" +
                               "\nPressure" + str(pressure) + 'hPa' +
                               "\nHumidity" + str(humidity) + '%',
                               icon_path=None, duration=None)


        elif "enter a code" in query or "tell me code" in query:
            speak("That's information require authorization.")
            speak("Random Question authorization")
            question = ['Favourite team?', 'Favourite dishes?', "What's your favourite subject?"]
            speak('Please responede from question.')
            print(randoming(question))
            choose = randoming(question)
            responde = input()

            if choose == question[0]:
                if responde == "MAN":
                    speak("Acess, show your code in terminal")
                    print('9854778255')
                else:
                    speak("You don't have permission")
                    pass

            if choose == question[1]:
                if responde == "pizza":
                    speak("Acess, show your code in terminal")
                    print("9854778255")
                else:
                    speak("You don't have permission")
                    pass

            if choose == question[2]:
                if responde == "math":
                    speak("Acess, show your code in terminal")
                    print("9854778255")
                else:
                    speak("You don't have permission")
                    pass

        elif "thx" in query or "thank" in query or "thanks" in query:
            speak("I am for you")

        elif "url" in query:
            createTable("database.db", "urls", "category", "TEXT", "url")

            var = input().split()
            #print(query)
            if query[0] == "add":
                insert("datebase.db", f'{var[1]}', f'{var[2]}')


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('Wikipedia says - ')
                    speak(results)
            except:
                pass