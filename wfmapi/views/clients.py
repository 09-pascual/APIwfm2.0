from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from wfmapi.models import Client

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'address', 'phone_number', 'email']



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

