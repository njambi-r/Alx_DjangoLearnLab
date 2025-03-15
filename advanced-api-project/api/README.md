## Project Overview
This project extends the `advanced_api_project` by implementing generic views in Django REST Framework (DRF) to handle CRUD operations efficiently for the `Book` model. The API includes endpoints for listing, retrieving, creating, updating, and deleting book records while enforcing appropriate permissions.

## Features
- **ListView**: Retrieve all books.
- **DetailView**: Retrieve a single book by ID.
- **CreateView**: Add a new book (restricted to authenticated users).
- **UpdateView**: Modify an existing book (restricted to authenticated users).
- **DeleteView**: Remove a book (restricted to authenticated users).