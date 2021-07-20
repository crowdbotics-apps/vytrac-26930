import datetime

from django.db.models import Q
from icecream import ic
from rest_framework import fields, serializers

from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import REC
from . import models
from .Functions.overlap import overlapping
from users.models import Availability

# TODO fix error messages
from .models import Event

MyModel = models.Event


class OverlapDatesSer(serializers.ModelSerializer):
    # TODO recurrence = serializers.ChoiceField(Required=False)
    class Meta:
        model = MyModel
        fields = ["start", "end", "from_time", 'to_time', "recurrence"]


class OverAvailabilitySer(serializers.ModelSerializer):
    # TODO recurrence = serializers.ChoiceField(Required=False)
    class Meta:
        model = Availability
        fields = ["start", "end", "from_time", 'to_time', "recurrence"]


class CalinderSeriazliser(DynamicSerializer):
    recurrence = fields.MultipleChoiceField(choices=REC)
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

        dates = MyModel.objects.filter(Q(Q(start__gte=today) and Q(end__gte=today) and Q(users__in=users)))

        ava_dates = Availability.objects.filter(Q(Q(start__gte=today) and Q(end__gte=today) and Q(user__in=users)))

        overlaps = overlapping(data, dates)
        availability_no_overlaps = overlapping(data, ava_dates, True)
        is_ava_overlap = len(availability_no_overlaps) == 0
        is_overlap = len(overlaps) > 0


        if (start or end) <= today:
            raise serializers.ValidationError(
                "You can't have " + date_name + " start or end before today.")

        if start >= end:
            raise serializers.ValidationError(
                "Start date must be before the end date.")

        if len(users) < 2 and date_type.name == 'appointment':
            raise serializers.ValidationError(
                'At least two people should have an appointment.')






        if not is_ava_overlap:
            raise serializers.ValidationError(
                {
                    'no overlap error': OverAvailabilitySer(availability_no_overlaps, many=True).data,
                    'availabilities': OverAvailabilitySer(ava_dates, many=True).data,
                    'help': '"no overlap error" means the data must be overlap with the at leas on of availabilities'
                },
            )

        if is_overlap:
            raise serializers.ValidationError(
                {'overlap error': OverlapDatesSer(overlaps, many=True).data,
                 'existed dates': OverlapDatesSer(dates, many=True).data,
                 'availability': OverlapDatesSer(ava_dates, many=True).data,
                 },
            )



        return data
        # start_date = pytz.UTC.localize(parser.parse(request.data['start']))
        # end_date = pytz.UTC.localize(parser.parse(request.data['end']))
        # users_list = request.data.getlist('users')

    class Meta:
        model = MyModel
        fields = '__all__'
