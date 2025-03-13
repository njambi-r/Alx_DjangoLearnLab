from .models import Author, Book
from rest_framework import serializers
import datetime

# Creating the serializers for the book and author models
class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Validate to ensure the publication date is not in the future
    def validate(self, data):
        if data['publication_year'] > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return data['publication_year']
