import datetime

from calendars.models import DateType


def calendar_setup(self):
    date_format = '%Y-%m-%d'
    time_format = '%H:%M:%S'
    d = datetime.datetime


    self.now = d.now().strftime(time_format)

    before_1_d = d.now() - datetime.timedelta(days=1)
    before_3_d = d.now() - datetime.timedelta(days=3)

    self.before_1_d = before_1_d.strftime(date_format)
    self.before_3_d = before_3_d.strftime(date_format)

    after_1_h = d.now() + datetime.timedelta(hours=1)
    after_5_h = d.now() + datetime.timedelta(hours=5)
    self.after_1_h = after_1_h.strftime(time_format)
    self.after_5_h = after_5_h.strftime(time_format)

    after_2_h = d.now() + datetime.timedelta(hours=2)
    after_3_h = d.now() + datetime.timedelta(hours=3)
    self.after_2_h = after_2_h.strftime(time_format)
    self.after_3_h = after_3_h.strftime(time_format)

    after_10_h = d.now() + datetime.timedelta(hours=10)
    after_11_h = d.now() + datetime.timedelta(hours=11)
    self.after_10_h = after_10_h.strftime(time_format)
    self.after_11_h = after_11_h.strftime(time_format)

    after_1_d = d.now() + datetime.timedelta(days=1)
    after_3_d = d.now() + datetime.timedelta(days=3)

    self.after_1_d = after_1_d.strftime(date_format)
    self.after_3_d = after_3_d.strftime(date_format)

    self.date1 = DateType.objects.create(name='meeting')
    self.date2  = DateType.objects.create(name='appointment')