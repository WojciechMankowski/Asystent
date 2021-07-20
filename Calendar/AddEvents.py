from __future__ import print_function
from typing import Optional, List, Dict, Union  # type: ignore
from googleapiclient.discovery import build # type: ignore
from datetime import datetime, timedelta # type: ignore
from Calendar.confingCalendar import Config


class AddNewEvents(Config):
    def AddNewEvents(self, data: Union[int, str, datetime], summary: str,
                     duration: float=1,
                     attendees: Optional[List[Dict[str, str]]]=None,
                     description: str=None, location: str=None):
        service = build('calendar', 'v3', credentials=self.creds)

        Data = data.date()
        Time = data.time()
        Time_end = data + timedelta(hours=duration)
        DATA_start = f"{Data}T{Time}"

        Data = Time_end.date()
        Time = Time_end.time()
        DATA_end = f"{Data}T{Time}"

        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'attendees': attendees,
            'start': {
                'dateTime': DATA_start,
                'timeZone': 'Europe/Warsaw',
            },
            'end': {
                'dateTime': DATA_end,
                'timeZone': 'Europe/Warsaw',
            },
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        # print('Event created: %s' % (event.get('htmlLink')))
if __name__ == '__main__':
    data = datetime(
        year=2021, day=16, month=7, hour=12, minute=00, second=0
    )
    AddNewEvents().AddNewEvents(data, "Zastrzyk testoseronu", 1.5)