from __future__ import print_function
from typing import List
from zoneinfo import ZoneInfo # type: ignore
from googleapiclient.discovery import build  # type: ignore
from httplib2 import Http  # type: ignore
from datetime import datetime  # type: ignore

from Calendar.confingCalendar import Config
from Data import Data


class listOfEvents(Config):
    def ListOfEvents(self) -> List[str]:
        service = build("calendar", "v3", credentials=self.creds)

        now = (
            datetime.utcnow().isoformat().format("%Y-%m-%d %H:%M") + "Z"
        )  # 'Z' indicates UTC time
        day = datetime.now().date()
        max = datetime(
            year=day.year,
            month=day.month,
            day=day.day,
            hour=0,
            minute=0,
            tzinfo=ZoneInfo("Europe/Warsaw"),
        )

        events = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        DataStart = []
        DataEnd = []
        Summary = []
        TXT = []
        for event in events["items"]:
            summary = event["summary"]
            Summary.append(summary)
            date_start = event["start"]
            date_end = event["end"]
            dataStart = self.ExtractionOfTheStartDate(date_start)
            DataStart.append(dataStart)
            dataEnd = self.ExtractingTheEndDate(date_end)
            DataEnd.append(dataEnd)

            if dataStart.date() != max.date():
                break
        del DataStart[-1]
        del DataEnd[-1]
        del Summary[-1]

        for index in range(len(DataStart)):
            txt = (
                f"Dzisiaj w tych godzinach "
                f"od {DataStart[index].time()} do {DataEnd[index].time()} masz zaplonowe {Summary[index]}."
            )
            TXT.append(txt)
        return TXT

    def ExtractionOfTheStartDate(self, date_start):
        if "dateTime" in date_start.keys():
            Date_start = date_start["dateTime"]
        else:
            Date_start = date_start["date"]
        data = Data().ObjectData(Date_start)
        return data

    def ExtractingTheEndDate(self, date_end):

        if "dateTime" in date_end.keys():
            Date_end = date_end["dateTime"]
        else:
            Date_end = date_end["date"]
        data = Data().ObjectData(Date_end)
        return data


if __name__ == "__main__":
    txt = listOfEvents().ListOfEvents()
    for item in txt:
        print(item)
