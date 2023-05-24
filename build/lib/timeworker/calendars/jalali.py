from . import CalendarBase
from timeworker.calendars.jalali_parser import jalali_parser


class JalaliCalendar(CalendarBase):
    """Calendar class for Jalali calendar."""

    parser = jalali_parser
