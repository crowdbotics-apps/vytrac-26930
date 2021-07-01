
def overlapping(date_item, date_set):
    date_format = '%Y-%m-%d'
    time_format = 'T%H:%M:%S.%fZ'
    overlaps = []

    def overlap(first_inter, second_inter):
        for f, s in ((first_inter, second_inter), (second_inter, first_inter)):
            for time in (f["i"], f["f"]):
                if s["i"] <= time <= s["f"]:
                    return True
        else:
            return False

    for date in date_set:
        Day_overlap = False
        Time_overlap = False
        Rec_overlap = False

        date1 = {}
        date2 = {}
        date1['i'] = getattr(date, 'start').strftime(date_format)
        date1['f'] = getattr(date, 'end').strftime(date_format)
        date2['i'] = date_item['start'].strftime(date_format)
        date2['f'] = date_item['end'].strftime(date_format)
        if (overlap(date1, date2)):
            Day_overlap = True

        time1 = {}
        time2 = {}
        time1['i'] = getattr(date, 'from_time').strftime(time_format)
        time1['f'] = getattr(date, 'to_time').strftime(time_format)
        time2['i'] = date_item['from_time'].strftime(time_format)
        time2['f'] = date_item['to_time'].strftime(time_format)
        if overlap(time1, time2):
            Time_overlap = True

        if bool(set(date.recurrence) & set(date_item['recurrence'])):
            Rec_overlap = True

        if len(date_item['recurrence']) == 0:
            Rec_overlap = True

        if Rec_overlap and Time_overlap and Day_overlap:
            overlaps.append(date)

    return overlaps

