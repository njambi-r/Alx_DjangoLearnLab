# Test cases
# api/test_views.py doesn't contain: ["self", "class", "APITestCase"]
from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
import json
from .models import Author



User = get_user_model()

class Book(TestCase):
    # What comes before
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        #login before request
        self.client.login(username="testuser", password="testpassword")
        # Ensure author you want to create exists in the test database
        self.author = Author.objects.create(id=1, name="Chinua Achebe")  # Ensure author exists
        print ("Setup...")
    
    # What comes after
    def tearDown(self):
        print ("Tearing down...")
    
    # Define the test. Always starts with test_(underscore)
    
    # List books
    def test_list_book(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Create book
    def test_create_book(self):
        data = {"title": "A Man of the People", "publication_year": 1963, "author": self.author.id}
        response = self.client.post("/api/books/create/", data=json.dumps(data), content_type="application/json")
        print("Response:", response.json())  # Print error details
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Update book
    def test_update_book(self):
        data = {"title": "A New Earth", "publication_year": 1963, "author": self.author.id}
        response = self.client.put("/api/books/update/1/", data=json.dumps(data), content_type="application/json")
        print("Response:", response.json())  # Print error details
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    # Delete book
    def test_delete_book(self):
        #data = {"title": "A New Earth", "publication_year": 1963, "author": self.author.id}
        response = self.client.delete("/api/books/delete/1/")
        print("Response:", response.json())  # Print error details
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 