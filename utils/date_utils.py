import calendar
import datetime


def get_end_of_the_month_formatted():
    # Get the last day of the current month in yyyy-mm-dd format
    today = datetime.date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]
    return f"{today.year}-{today.month:02d}-{last_day:02d}"
