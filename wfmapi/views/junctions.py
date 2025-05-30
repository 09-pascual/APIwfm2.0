from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from wfmapi.models import ProjectWorker, GroupWorker, ProjectGroup

class ProjectWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectWorker
        fields = '__all__'

class ProjectWorkerViewSet(viewsets.ModelViewSet):
    queryset = ProjectWorker.objects.all()
    serializer_class = ProjectWorkerSerializer
    permission_classes = [IsAuthenticated]

class GroupWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWorker
        fields = '__all__'

class GroupWorkerViewSet(viewsets.ModelViewSet):
    queryset = GroupWorker.objects.all()
    serializer_class = GroupWorkerSerializer
    permission_classes = [IsAuthenticated]

class ProjectGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGroup
        fields = '__all__'

class ProjectGroupViewSet(viewsets.ModelViewSet):
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
    permission_classes = [IsAuthenticated]
