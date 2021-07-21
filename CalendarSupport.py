from Calendar.AddEvents import AddNewEvents
from Calendar.ListEvents import listOfEvents
from Data import Data
from listen import Listen
from speak import Speak
from Exceptions import NoCommandException
from ListCommands import *

listen = Listen()
speaks = Speak()
data = Data()

add_events = AddNewEvents()
list_events = listOfEvents()


def calendarsupport() -> None:

    for i, item in enumerate(hello_list):
        speaks.Say(item)

    txt = f"{hello_list[1]} {hello_list[2]} {hello_list[3]}. " \
          f"Czekam na Twój wybór"

    text = listen.listen_for_speech(txt)

    if text in commands:

        txt = "Wpisz datę w  poniżczym formacie: "
        speaks.Say(txt)
        print("format daty %Y-%M-%D %H:%M np: 2021-07-15 15:25")
        str_data = input(txt)
        data_obj = data.ObjectData(str_data)

        txt = "Wykonuj poniższcze wydarzenia"
        speaks.Say(txt)

        txt = "Podaj tytuł wydarzenia: "
        summary = input(txt)

        txt = "Wpisz jak długo planujesz spotkanie"
        speaks.Say(txt)
        txt2 = "Jeśli nie chcerz poddawać czasu wpiszcz zero"
        speaks.Say(txt2)
        duration = int(input(txt))

        txt = "Wpisz opis wydarzenia"
        speaks.Say(txt)
        txt2 = "Jeśli nie chcerz poddawać zostaw puste"
        speaks.Say(txt2)
        opis = input(txt)

        if duration != 0:
            if opis != "":
                add_events.AddNewEvents(
                    data=data_obj, summary=summary, duration=duration
                )
            else:
                add_events.AddNewEvents(
                    data=data_obj, summary=summary, duration=duration, description=opis
                )
        else:
            if opis != "":
                add_events.AddNewEvents(
                    data=data_obj, summary=summary, duration=duration
                )
            else:
                add_events.AddNewEvents(
                    data=data_obj, summary=summary, duration=duration, description=opis
                )
    elif text in commands_list:
        txt = list_events.ListOfEvents()
        for item in txt:
            speaks.Say(item)
    else:
        raise NoCommandException(text)


if __name__ == "__main__":
    calendarsupport()
