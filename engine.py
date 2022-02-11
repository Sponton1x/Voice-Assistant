from main import voices

class Engine:
    engine = pyttsx3.init(self)
    voices = engine.getProperty('voices')
    voices = engine.setProperty('rete', 200)
    engine.setProperty('voice')