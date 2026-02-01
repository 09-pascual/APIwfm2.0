from rest_framework import serializers,viewsets
from rest_framework.permissions import IsAuthenticated
from wfmapi.models import Project, Worker, Group, Client
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class WorkerBriefSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source='user.email', read_only = True)

    class Meta:
        model = Worker
        fields = ['id', 'email']

class GroupBriefSerializer(serializers.ModelSerializer):
    
     class Meta:
         model = Group
         fields = ['id', 'name']

class ClientBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name']
    

class ProjectSerializer(serializers.ModelSerializer):
    #Read
    workers = WorkerBriefSerializer(many= True, read_only=True)
    groups = GroupBriefSerializer(many=True, read_only=True)
    client = ClientBriefSerializer(read_only = True)
    client_id = serializers.PrimaryKeyRelatedField(queryset= Client.objects.all(), write_only=True)

    #Write
    worker_ids = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all(), many = True, write_only=True, required=False)
    group_ids = serializers.PrimaryKeyRelatedField(queryset= Group.objects.all(), many=True, write_only=True, required=False)

    class Meta:
        model = Project
        fields = ['id', 'client','client_id', 'name', 'status',
            'start_date', 'end_date', 'expected_duration', 'address',
            'workers', 'worker_ids',
            'groups',  'group_ids',]
        
    def create(self, validated_data):
        # FIXED: Extract the client and create project explicitly
        wids = validated_data.pop('worker_ids', [])
        gids = validated_data.pop('group_ids', [])
        client = validated_data.pop('client_id')
        
        # Create the project with the client assigned
        project = Project.objects.create(client=client, **validated_data)
        
        # Set the many-to-many relationships
        project.workers.set(wids)
        project.groups.set(gids)
        return project


    def update(self, instance, validated_data):
        # FIXED: Cleaner update logic
        wids = validated_data.pop('worker_ids', None)
        gids = validated_data.pop('group_ids', None)
        client = validated_data.pop('client_id', None)
        
        # Update client if provided
        if client:
            instance.client = client
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update many-to-many relationships if provided
        if wids is not None:
            instance.workers.set(wids)
        if gids is not None:
            instance.groups.set(gids)
        
        return instance


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.select_related('client') \
                              .prefetch_related('workers__user','groups') \
                              .all()

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_projects(request):
    worker = Worker.objects.get(user=request.user)
    projects = Project.objects.filter(workers=worker)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)