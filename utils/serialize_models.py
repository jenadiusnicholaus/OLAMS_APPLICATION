
import json
from rest_framework.renderers import JSONRenderer
from django.core import serializers



class SerializerManager:
    @staticmethod
    def jsonfySerialize( obj):
        jsonObj=json.dumps(obj)
        _json = JSONRenderer().render(jsonObj)
        return  _json