import datetime

from calendars.models import DateType


def create_before_date(self, n):
    d = datetime.datetime
    date_format = '%Y-%m-%d'

    x = d.now() - datetime.timedelta(days=n)
    x = x.strftime(date_format)
    setattr(self, f'before_{n}_d', x)


def create_date(self, n):
    d = datetime.datetime
    date_format = '%Y-%m-%d'

    x = d.now() + datetime.timedelta(days=n)
    x = x.strftime(date_format)
    setattr(self, f'after_{n}_d', x)


def create_before_time(self, n):
    d = datetime.datetime
    time_format = '%H:%M:%S'
    x = d.now() - datetime.timedelta(hours=n)
    x = x.strftime(time_format)
    setattr(self, f'before_{n}_h', x)


def create_time(self, n):
    d = datetime.datetime
    time_format = '%H:%M:%S'
    x = d.now() + datetime.timedelta(hours=n)
    x = x.strftime(time_format)
    setattr(self, f'after_{n}_h', x)


def calendar_setup(self):
    for i in range(1, 12):
        create_time(self, i)
        create_before_time(self, i)

    for i in range(1, 12):
        create_date(self, i)
        create_before_date(self, i)
    self.date1 = DateType.objects.create(name='meeting')
    self.date2 = DateType.objects.create(name='appointment')
