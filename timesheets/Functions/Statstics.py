import pandas as pd
from rest_framework.response import Response

from collections import OrderedDict, defaultdict


def Resampling(df,resample,cal):
    df = getattr(df.resample(resample, on='date_created').field_value, cal)()
    df = df.reset_index()
    df['date_created'] = df['date_created'].apply(lambda x: x.strftime('%Y-%m-%d_%H%M%S.%f'))
    return df


def Duration(df):
    df = df.pivot(index='object_id', columns='field_value', values=['date_created'])
    false = df.xs('False', axis='columns', level=1)
    true = df.xs('True', axis='columns', level=1)

    df['durations'] = true.sub(false)
    return df


def statistics(data, getter):
    data = data
    resample = getter.get('resample')
    cal = getter.get('cal')
    df = pd.DataFrame(data)
    is_cal = True
    try:
        resample = resample.title()
        cal = cal.lower()
        df['date_created'] = pd.to_datetime(df['date_created'])
    except:
        pass

    try:
        df['date_created'] = pd.to_datetime(df['date_created'])
    except:
        is_cal = False

    if is_cal:
        if resample:
            df = Resampling(df,resample,cal)

        if cal == 'duration':
            df = Duration(df)
            data = df['durations'].to_dict()
        else:
            # TODO calculate change in blood purser over different periods of time
            pass

    return data
