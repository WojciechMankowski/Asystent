import speech_recognition as sr # type: ignore

class Listen:
    def listen_for_speech(self, text: str="Powiedz cość") -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(text)
            audio = r.listen(source)
            try:
                recoding = r.recognize_google(audio, language="pl-PL")
                if recoding != "":
                    return recoding.lower()
                return ""
            except sr.UnknownValueError:
                print("Nie zrozumiałem")
            except sr.RequestError as e:
                print(f"Error: {e}")
        return ''