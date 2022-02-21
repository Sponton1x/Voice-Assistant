import pyttsx3

def Engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    voices = engine.setProperty('rete', 100)
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
