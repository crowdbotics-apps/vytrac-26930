from rest_framework import generics, status
from rest_framework.response import Response

from Functions.DynamicSer import DynamicSerializer
from Functions.queryset_filtering import queryset_filtering
from .. import models

MyModel = models.AllDataStr


class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
        depth = 1


class Views(generics.ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
    def get(self, request, *args, **kwargs):
        context = {'request': request, 'method': 'view'}

        items = queryset_filtering(self.queryset.model, request.GET)
        serializer = self.serializer_class(
            items, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)