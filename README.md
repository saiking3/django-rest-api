# django-rest-api
django rest api

# serializers
=> for testing open django shell -- python manage.py shell

from userdetails.models import Articles
form userdetails.serializers import ArticlesSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# serializers