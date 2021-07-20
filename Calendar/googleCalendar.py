from __future__ import print_function
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # type: ignore
from ListEvents import listOfEvents # type: ignore
from AddEvents import AddNewEvents # type: ignore

def run():
    data = datetime(year=2021, month=7, day=14, hour=17, minute=30, second=00, tzinfo=ZoneInfo('Europe/Warsaw'))
    AddNewEvents().AddNewEvents(data, "Test test", 5)
    listOfEvents().ListOfEvents()

if __name__ == '__main__':
    run()
