from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .util import getCity
import json

# Create your views here.
@swagger_auto_schema(
    method='get', 
    manual_parameters=[
        openapi.Parameter(
            name='query_param',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='A query parameter',
            required=True,
        ),
    ],
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
        "redoc deocumentation": "/redoc"
    }
    return Response(data)
    

@api_view(["GET","POST"])
def suggestions(request):

    if request.method == "GET":
        q = request.query_params.get('q', None)
        longitude = float(request.query_params.get('longitude', 0))
        latitude = float(request.query_params.get('latitude', 0))
        suggestions = getCity.getCity(q, longitude, latitude)
    else:
        r = request.data
        q = r.get('q', None)
        longitude = float(r.get('longitude', 0))
        latitude = float(r.get('latitude', 0))
        suggestions = getCity.getCity(q, longitude, latitude)
    
    data = {
            "suggestions": suggestions
        }
    return Response(data)
    
    