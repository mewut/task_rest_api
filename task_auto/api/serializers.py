from rest_framework import serializers
from .models import Executor, Task


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = ('id', 'name')

    
class TaskSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'created_at', 'executor', 'priority', 'title', 'comment')
