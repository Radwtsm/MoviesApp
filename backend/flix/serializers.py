from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


from .models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_superuser']
