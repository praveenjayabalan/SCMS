from rest_framework import serializers
from django.contrib.auth import get_user_model
from .signals import (
    welcome_email
)   
from django.contrib.auth.models import Group

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'is_staff',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):    
        my_group = Group.objects.get(name='Student') 
        
        username = validated_data['username']
        email = validated_data['email']
        password = "password123"
        user_obj = User(
            username=username,
            email=email,
            is_staff=True
        )
        user_obj.set_password(password)
        user_obj.save() 
        user_obj.groups.add(my_group)

        welcome_email.send(sender=self.__class__,username =username, email=email,request=self)
        return validated_data

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance
