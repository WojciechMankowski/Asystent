from check import WebBrowser
from speak import Speak


def googlesearch(text: list[str]) -> None:
    webbrowser_ = WebBrowser()
    speaks = Speak()
    url = webbrowser_.link_building(text)
    speaks.Say("Otwieram przeglądarkę")
    webbrowser_.OpeningAWebBrowser(url)
    speaks.Say("Otworzyłem przeglądarkę")