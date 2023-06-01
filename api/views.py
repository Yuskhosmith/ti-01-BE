from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .util import getCity

# Create your views here.
@swagger_auto_schema(
    method='get',
    responses={200: 'OK'}
)
@api_view(["GET"])
def endpoints(request):
    """
    Describes where the documentation is
    """
    data = {
        "suggestions": "/suggestions",
        "swagger documentation": "/swagger",
        "redoc documentation": "/redoc"
    }
    return Response(data)
    
@swagger_auto_schema(
    method='get', 
    manual_parameters=[
        openapi.Parameter(
            name='query',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='City',
            required=True,
        ),
        openapi.Parameter(
            name='longitude',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
            format=openapi.FORMAT_FLOAT,
            description='longitude',
        ),
        openapi.Parameter(
            name='latitude',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
            format=openapi.FORMAT_FLOAT,
            description='latitude',
        ),
    ],
    responses={200: 'OK'}
)
@api_view(["GET"])
def suggestions(request):
    """
    Suggestions
    Parameters q(String), longitude(Float / Decimal / None), latitude (Float / Decimal / None)
    """
    q = request.query_params.get('q', None)
    longitude = request.query_params.get('longitude', 0)
    latitude = request.query_params.get('latitude', 0)
    try:
        longitude = float(longitude)
        latitude = float(latitude)
        if q is not None:
            suggestions = getCity.getCity(q, longitude, latitude)
        else:
            suggestions = []
    except ValueError:
        return Response({"ValueError": {
            "value(dataType)": {
                f"{q}({type(q)})": "Expected String",
                f"{longitude}({type(longitude)})": "Expected None / Number / Decimal / Float",
                f"{latitude}({type(latitude)})": "Expected None / Number / Decimal / Float"
            }
        }})
    
    data = {
            "suggestions": suggestions
        }
    return Response(data)
    
    