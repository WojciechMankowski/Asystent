from configuration import Configuration
import datetime

class Speak(Configuration):

    def Say(self, text: str)-> None:
        self.enigma.say(text)
        self.enigma.runAndWait()
