from timeworker.calendars import CalendarBase
from timeworker.calendars.hijri_parser import hijri_parser


class HijriCalendar(CalendarBase):
    parser = hijri_parser
