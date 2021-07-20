from configuration import Configuration
import datetime
class Speak(Configuration):
    def Say(self, text: str)-> None:
        self.enigma.say(text)
        self.enigma.runAndWait()

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.Say("Dzień dobry")
        elif hour >= 12 and hour < 18:
            self.Say("Dzień dobry")
        else:
            self.Say("Dobry wieczór!")
        self.Say("Witamy! Proszę powiedz mi, jak mogę ci pomóc")