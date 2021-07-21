from listen import Listen
from speak import Speak
from check import CheckingWhatWasSaid
from GoogleSearch import googlesearch
from Seach import seach_in_wikipedia
from Exceptions import IncomprehensionException
from CalendarSupport import calendarsupport
from time import sleep
from ListCommands import *


def checktext(text) -> bool:
    if text != "":
        return True
    else:
        return False


def LaunchTheProgram():
    listen = Listen()
    speaks = Speak()
    checks = CheckingWhatWasSaid()
    while True:
        text = listen.listen_for_speech()
        if checktext(text):
            if checks.CheckingTheCall(text, detect) == True:
                if checks.SecondWordCheck(text, search) == True:
                    if checks.ThirdWordCheck(text) != "":
                        text_query = checks.ThirdWordCheck(text)
                        print(text_query)
                        googlesearch(text_query)
                elif checks.SecondWordCheck(text, wikipedia) == True:
                    text_query = checks.ThirdWordCheck(text)
                    text = seach_in_wikipedia(text_query)
                    speaks.Say(text)
                elif checks.SecondWordCheck(text, calendar) == True:
                    calendarsupport()
                elif checks.SecondWordCheck(text, weather) == True:
                    print(text)
                elif checks.SecondWordCheck(text, helps) == True:
                    print('POMOC')
                    speaks.Say('Zaraz wszystko Ci pokażę')
                    print("-"*50)
                    listComends = DisplayAllCommands()
                    for item in listComends:
                        print(item)
                        print('\n')
                        print("-" * 50)
                        speaks.Say(item)
                elif checks.SecondWordCheck(text, goodbye) == True:
                    speaks.Say("Do zobaczenia!!")
                    break
        else:
            raise IncomprehensionException()



if __name__ == '__main__':
    LaunchTheProgram()









