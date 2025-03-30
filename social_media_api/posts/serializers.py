from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    # display the username instead of the id of the author
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta: 
        model = Post
        fields = '__all__' # fields to include in the api response
        read_only_fields = ['author','created_at','updated_at']

class CommentSerializer(serializers.ModelSerializer):
    # show the username of the author instead of the author id
    author = serializers.ReadOnlyField(source='author.username')
    """
    Note: ReadOnlyField allows only reading (GET requests). It does
    not allow writing (POST, PUT requests). It should thus not be used
    for ForeignKey fields where input is required. 
    """

    # reference the post by id'
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    """
    The PrimaryKeyRelatedField in Django REST Framework (DRF) 
    is used to represent a ForeignKey or ManyToManyField in a 
    serializer by showing only the related object's primary key 
    instead of serializing the full object. 
    It allows read and write.
    Also provides automatic validation to check if the post exists

    Alternatives: 
    - StringRelatedField: post = serializers.StringRelatedField() # When you need a readable string representation instead of an ID
    - Nested Serializer (PostSerializer()) #Basically, if we don't specify any of the above. This shows the full object details
    """
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author','created_at','updated_at']
        # post not included to allow a user to create a comment with a specific post
        
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta: 
        model = Like
        fields = '__all__'
    