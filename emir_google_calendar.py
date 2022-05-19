from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def add_event(delay_day, duration_in_hours, summary, description):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    d = datetime.now().date()
    wanted_day = datetime(d.year, d.month, d.day, 10)+timedelta(days=delay_day)
    start = wanted_day.isoformat()
    end = (wanted_day + timedelta(hours=duration_in_hours)).isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": summary,
                                               "description": description,
                                               "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                               "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                                           }
                                           ).execute()


if __name__ == '__main__':
    DAY_FROM_NOW = 12
    HOURS_FROM = 12
    SUMMARY = "Something"
    DESCRIPTION = "Description of something"
    add_event(delay_day=DAY_FROM_NOW, duration_in_hours=HOURS_FROM,
              summary=SUMMARY, description=DESCRIPTION)
