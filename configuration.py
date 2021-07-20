import pyttsx3 # type: ignore

class Configuration:
    enigma = pyttsx3.init()
    enigma.setProperty("volume", 0.05)
    enigma.setProperty("rate", 190)
    voices = enigma.getProperty('voices')
    enigma.setProperty("voice", voices[1].id)





