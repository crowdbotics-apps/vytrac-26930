import datetime

from icecream import ic
from rest_framework import fields, serializers

from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import REC
from users.serializers import AvalibitlySer
from . import models
from .Functions.overlap import overlapping

MyModel = models.Event
class OverlapDatesSer(serializers.ModelSerializer):
    # TODO recurrence = serializers.ChoiceField(Required=False)
    class Meta:
        model = MyModel
        fields = ["start", "end", "from_time", 'to_time', "recurrence"]


class CalinderSeriazliser(DynamicSerializer):
    recurrence = fields.MultipleChoiceField(choices=REC)
    # created_by = serializers.CharField(required=False)
    date_created = serializers.CharField(required=False)

    def validate(self, data, *args, **kwargs):
        # TODO add recursive validation logic
        # TODO for i in user.avalable if date not in i reaise 'User can be avalabel in [], user already have dates in []'
        messages = []
        my_format = '%Y-%m-%d'
        my_s_format = 'T%H:%M:%S.%fZ'
        today = datetime.datetime.now().strftime(my_format)
        # data['created_by'] = self.context['request'].user
        # created_by = data['created_by']
        data['date_created'] = today
        users = data['users']
        start = data['start'].strftime(my_format)
        end = data['end'].strftime(my_format)

        date_type = data['date_type']
        date_name = date_type.name
        date_name = "an " + date_name if date_name[0] in ['i', 'o', 'u', 'a', 'e'] else "a " + date_name

        dates = MyModel.objects.all()
        dates = dates.filter(start__gte=today, end__gte=today)
        dates = dates.filter(users__in=users)

        overlaps = overlapping(data, dates)
        is_overlap = len(overlaps) > 0
        availabilities = []

        # for user in users:
        #     aval = AvalibitlySer(user.date_avalable.all(), many=True)
        #     availabilities.append(aval.data)

        if is_overlap:
            raise serializers.ValidationError(
                {'overlap error': OverlapDatesSer(overlaps, many=True).data,
                 'existed dates': OverlapDatesSer(dates, many=True).data,
                 "availabilities": availabilities
                 },
            )

        if len(users) < 2 and date_type.name == 'appointment':
            raise serializers.ValidationError(
                'At least two people shoul have an appointment.')

        if (start or end) <= today:
            raise serializers.ValidationError(
                "You can't have " + date_name + " start or end before today.")

        if start >= end:
            raise serializers.ValidationError(
                "Start date must be before the end date.")
        # if (not created_by.is_staff or not created_by.is_superuser):
        #     users.append(created_by)

        return data
        # start_date = pytz.UTC.localize(parser.parse(request.data['start']))
        # end_date = pytz.UTC.localize(parser.parse(request.data['end']))
        # users_list = request.data.getlist('users')
        # date_type = ''
        # try:
        #     date_type = models.DateType.objects.get(
        #         id=request.data['date_type']).name
        # except:
        #     pass
        # if (not request.user.is_staff or not request.user.is_superuser):
        #     users_list.append(request.user.id)
        # busy_schadules = models.Date.objects.filter(
        #     start__gte=request.data['start'], end__gte=request.data['end'])
        # for busy_schadule in busy_schadules:
        # return super().post(request, *args, **kwargs)

    class Meta:
        model = MyModel
        fields = '__all__'