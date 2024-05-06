# Book-Store

**Project Overview:**
This Django project is a simple bookstore application that allows users to view, add, edit, and delete books and authors. It also provides user registration, login, and logout functionalities.

**Project Structure:**
- **bookstore:** The main Django application containing the project settings and URL configurations.
- **bookstore/models.py:** Defines the database models for books and authors.
- **bookstore/forms.py:** Contains form classes for creating and editing authors and books.
- **bookstore/templates:** Directory for HTML templates.
- **bookstore/static:** Directory for static files like CSS, JavaScript, and images.
- **bookstore/migrations:** Contains database migration files.
- **bookstore/views.py:** Defines the view functions for rendering pages and handling user interactions.
- **bookstore/urls.py:** Specifies the URL patterns for the application.
- **media:** Directory for storing uploaded files like book and author images.

**Features:**
- **User Registration:** Users can create accounts to access the bookstore functionalities.
- **User Authentication:** Registered users can log in and out of their accounts securely.
- **Bookstore Index:** Displays a list of all books available in the store.
- **Book Details:** Shows detailed information about a specific book, including name, author, price, and pages.
- **Author Details:** Provides information about individual authors, including their name, birth date, and image.
- **CRUD Operations:** Users can create, read, update, and delete both books and authors.
- **Image Upload:** Supports uploading images for both books and authors.
- **Form Validation:** Validates user input to ensure data integrity and consistency.

**Dependencies:**
- Django
- Python


