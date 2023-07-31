from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

class HandlerFileUpload(APIView):

    def post(self, request):
        try:
            data = request.data

            serializers = FileListSerializer (data= data)

            if serializers.is_valid():
                serializers.save()
                return Response({
                    'status': 200,
                    'message': 'file upload successfully',
                })

            return Response({
                'status' : 400,
                'message': 'Something went wrong',
                'data': serializers.errors
            })

        except Exception as e:
            print(e)
            return Response({
            'status': 500,
            'message': 'Internal Server Error',
            'data': str(e)
        })



