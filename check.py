import webbrowser
from typing import Union


class CheckingWhatWasSaid:

    def CheckingTheCall(self, word: str, word_list: list[str]) -> bool:
        WORD = word.lower().split(" ")
        if WORD[0] in word_list:
            return True
        return False

    def SecondWordCheck(self, word: str, word_list: list[str]) -> bool:
        WORD = word.lower().split(" ")
        if WORD[1] in word_list:
            return True
        return False

    def ThirdWordCheck(self, word: str) -> list[str]:
        WORD = word.lower().split(" ")
        del WORD[0:2]
        return WORD

class WebBrowser:

    def link_building(self, text: Union[str, list[str]]) -> str:
        str_text: str = ""
        for element in text:
            str_text += element + " "
        str_text = str_text.rstrip()
        text = str_text.replace(" ", "+").replace("?", "%3F")
        url = f"www.google.com/search?q={text}"
        return url

    def OpeningAWebBrowser(self, URL: str) -> None:
        web_browser = webbrowser.open(URL)


