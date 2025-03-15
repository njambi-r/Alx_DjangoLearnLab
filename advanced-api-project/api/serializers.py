from .models import Author, Book
from rest_framework import serializers
import datetime

# Creating the serializers for the book and author models
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Validate to ensure the publication date is not in the future
    def validate(self, data):
        if data['publication_year'] > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return data
    
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to show the author along with their related books
    books = BookSerializer(many=True, read_only=True)
    class Meta: 
        model = Author
        fields = ['name']
