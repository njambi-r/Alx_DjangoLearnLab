from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#django.contrib.auth.get_user_model:~:text=as%20described%20below.-,Referencing%20the%20User%20model,-%C2%B6 
"""
Since the AUTH_USER_MODEL setting has been changed to a 
different user model, it is referenced using django.contrib.auth.get_user_model().
This method will return the currently active user model - 
the custom user model if one is specified, or User otherwise.
"""
#User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ['username','password','email','bio','profile_picture','followers']
        #extra_kwargs = {'password': {'write_only': True}} #This prevents the password from being included in API responses.

# serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Ensures that the password is treated as a string and is write-only (not included in responses)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password'] #fields we allow users to provide when registering

    # method called when serializer.save() is executed
    # it receives validated_data -- which is cleaned up user input
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data) # Django’s built-in create_user() method to create a new user
        token, created = Token.objects.create(user=user)
        """
        If the user is newly created, a token is generated for them.
        If the user already exists, their existing token is retrieved.
        """
        return user   
       