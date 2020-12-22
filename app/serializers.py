from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','profile','password']

    def validate(self, data):
        user_obj = User(
            username=data.get('username'),
            email=data.get('email')
        )
        user_obj.set_password(data.get('password'))
        user_obj.is_active = True
        user_obj.save()
        return user_obj

class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'password','email','joinDate')

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            auth = authenticate(username=username, password=password)
            if auth:
                return auth
            else:
                raise exceptions.ValidationError('Username or Password Invalid')
        else:
            raise exceptions.ValidationError('All Fields Required***')

class UserBlogSerializer(serializers.ModelSerializer):
    user = CreateUserSerializer()

    class Meta:
        model = BlogPageContent
        fields = ('id', 'user', 'title', 'content', 'postDate')
