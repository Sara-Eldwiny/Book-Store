from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bookstore.views import welcome, index,logout_view, profile, landing, bookstore_index, register_view, new_book_show, create_form, book_delete, author_detail, delete_author, create_author, all_authors, book_edit, edit_author, login_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', index, name="book_data"),
    path('books/<int:id>/', profile, name="select_item"),
    path('land/', landing, name="bookstore_land"),
    path('bookstore/', welcome, name="bookstore_welcome"),
    path('index/', bookstore_index, name="bookstore_index"),
    path("index/<int:id>", new_book_show, name="new_book_show"),
    path("index/<int:id>/delete", book_delete, name="book_delete"),
    path("create/", create_form, name="create.form"),
    path('book/edit/<int:id>/', book_edit, name='book_edit'),
    path('authors/', all_authors, name='all_authors'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('create_author/', create_author, name='create_author'),
    path('delete_author/<int:author_id>/', delete_author, name='delete_author'),
    path('authors/<int:author_id>/edit/', edit_author, name='edit_author'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
