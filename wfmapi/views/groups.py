from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from wfmapi.models import Group, Worker


class WorkerNestedSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only = True)

    class Meta:
        model = Worker
        fields = ['id' 'email', 'status']


class GroupSerializer(serializers.ModelSerializer):
    #read
    workers = WorkerNestedSerializer(many=True, read_only = True)
    #write
    worker_ids = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all(), many=True, write_only=True, required=False)


    class Meta:
        model = Group
        fields= ['id', 'name', 'workers', 'worker_ids']

    def create(self, validated_data):
        wids = validated_data.pop('worker_ids', [])
        group = super().create(validated_data)
        group.workers.set(wids)
        return group

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.prefetch_related('workers__user').all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]






