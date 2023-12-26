from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

@api_view(['GET'])
def get_data(request):
    data_objects = Data.objects.all()
    serializer = DataSerializer(data_objects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_data(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return a 201 Created status for successful POST
    return Response(serializer.errors, status=400)  # Return a 400 Bad Request status for invalid data

@api_view(['GET'])
def get_data_detail(request, pk):
    data_object = get_object_or_404(Data, pk=pk)
    serializer = DataSerializer(data_object)
    return Response(serializer.data)

@api_view(['PUT'])
def put_data(request, pk):
    data_object = get_object_or_404(Data, pk=pk)
    serializer = DataSerializer(data_object, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_data(request, pk):
    data_object = get_object_or_404(Data, pk=pk)
    data_object.delete()
    return Response(status=204)  # Return a 204 No Content status for successful DELETE
