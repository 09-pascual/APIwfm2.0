from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from wfmapi.models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source = 'user.email', read_only = True)

    class Meta:
        model = Worker
        fields = ['id', 'user', 'email', 'status']


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.select_related('user').all()
    serializer_class = WorkerSerializer
    permission_classes = {IsAuthenticated}
    