from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task

        # you can type some fields to be serialized
        #fields = ('id', 'title', 'description', 'done')
        
        # or you can simply call all fields
        fields = '__all__'