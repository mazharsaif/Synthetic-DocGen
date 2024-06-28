
import random
from datetime import datetime, timedelta

def get_random_year():
    return random.choice(list(range(1990, 2030)))


def get_random_date(start=datetime(1990, 1, 1), end=datetime(2024, 1, 1)):
    """Generate a random datetime between `start` and `end`"""
    delta = end - start
    int_delta = delta.days
    random_day = random.randrange(int_delta)
    date = start + timedelta(days=random_day)


    # Define the different formats
    # TODO: Can add more random date_formats
    formats = [
        "%d-%m-%Y",         # DD-MM-YYYY
        "%d-%m",            # DD-MM
        "%d-%B-%y",         # DD-January-YY
        "%b/%d",            # Jan/12,
        "%d/%m/%Y",         # DD/MM/YYYY,
        "%d/%m/%y",         # DD/MM/YY
    ]

    return date.strftime(random.choice(formats))