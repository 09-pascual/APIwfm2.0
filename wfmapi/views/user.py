from rest_framework import serializers
from wfmapi.models import User
from rest_framework import viewsets

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'is_owner']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer