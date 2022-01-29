import pyttsx3
import webbrowser
import random
import datetime
import requests
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import sys
import win10toast_persist

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

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


"""currentH = int(datetime.datetime.now().hour)
#if currentH == 7:
 #   speak("Welcome sir")
  #  import pyttsx3
   # import requests


#def weather():
#api = "https://www.weatherapi.com/weather/q/lodz-poland-1966664"


jsl = requests.get(api).json()

data = jsl["main"]["temp"]
data1 = data - 273.15
print("The temperature in łodź is" + str(data1), "*C")
data2 = jsl["weather"][0]["description"]
print("It is" + str(data2))
engine.say("The current temperature in łodź is" + str(data1) + "degrees celcius")
engine.say("It is" + data2)
engine.runAndWait()"""

greetMe()
speak("I'm Jarvis !")
speak('How I can help you')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query} \n')
    except sr.UnknownValueError:
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
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
            speak(random.choice(says))
            sys.exit()


        elif 'who are you' in query:
            says = "Let me to introduce myself.I'm jarvis and your personal voice assistant."
            speak(says)

        elif 'hello' in query or 'hi' in query:
            speak('Hello Sir')

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
            print(random.choice(question))
            choose = random.choice(question)
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
