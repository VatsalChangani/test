from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    repeat_password = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.repeat_password = validated_data.get('repeat_password', instance.repeat_password)
        instance.save()
        return instance