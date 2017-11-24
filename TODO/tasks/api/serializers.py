from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    ListSerializer
    )
from tasks.models import TasksList

class TaskListSerializer(ModelSerializer):
    created_by = SerializerMethodField()

    class Meta:
        model = TasksList
        fields = [
            'name_task',
            'description',
            'created_by',
            'created_at',
            'updated_at',
        ]
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.username
        else:
            return None

class TasksListSerializer(ListSerializer):
    def create(self, validated_data):
        books = [TasksList(**item) for item in validated_data]
        return TasksList.objects.bulk_create(books)

class TaskCreateSerializer(ModelSerializer):

    class Meta:
        model = TasksList
        fields = [
            'name_task',
            'description',
            'created_by',
        ]
        list_serializer_class = TasksListSerializer

class TaskUpdateSerializer(ModelSerializer):

    class Meta:
        model = TasksList

        fields = [
            'name_task',
            'description',
        ]