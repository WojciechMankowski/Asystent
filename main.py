from listen import Listen
from speak import Speak
from check import CheckingWhatWasSaid
from GoogleSearch import googlesearch
from Seach import seach_in_wikipedia
from Exceptions import IncomprehensionException
from CalendarSupport import calendarsupport
from time import sleep


listen = Listen()
speaks = Speak()
checks = CheckingWhatWasSaid()




detect = ["bot", 'robot', "wojtek"]
goodbye = ["do", "widzenia", "goodbye", "papa"]
search = ["szukaj", "znajdź", 'pokaż']
wikipedia = ["wikipedia", "wiki", 'wikipedia']
calendar = ["kalendarz", "dodaj"]
# speaks.wishMe()
while True:
    sleep(0.5)
    text= listen.listen_for_speech()
    print(end="\r")
    print(text)
    if not text == "":
       if checks.CheckingTheCall(text, detect) == True:
           if checks.SecondWordCheck(text, search) == True:
               if checks.ThirdWordCheck(text) != "":
                   text_query = checks.ThirdWordCheck(text)
                   print("Zapytanie")
                   print(text_query)
                   googlesearch(text_query)
           elif checks.SecondWordCheck(text, wikipedia) == True:
                    text_query = checks.ThirdWordCheck(text)
                    text = seach_in_wikipedia(text_query)

                    print(text)
                    speaks.Say(text)
           elif checks.SecondWordCheck(text, calendar) == True:
               calendarsupport()
           elif checks.SecondWordCheck(text, goodbye) == True:
               speaks.Say("Do zobaczenia!!")
               break
    else:
        raise IncomprehensionException()








