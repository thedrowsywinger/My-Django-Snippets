from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers

from drf_app.models import DRF_Model

from drf_app.serializers import info_serializer

from rest_framework.views import APIView
from rest_framework.response import Response



class drf_testing_view(APIView):

    serializer_class = info_serializer

    def get(self, request):
        queryset = DRF_Model.objects.all().values()
        return JsonResponse({"objects": list(queryset)})

    def post(self, request):
        serializer_class = info_serializer
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print("All good")
            instance = DRF_Model(
                first_name = serializer.data.get('first_name'),
                last_name = serializer.data.get('last_name'),
                email = serializer.data.get('email')
            )

            instance.save()

            return Response({'Good Request': 'Info Received'})


