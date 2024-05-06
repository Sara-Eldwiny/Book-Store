from django.shortcuts import render , redirect, get_object_or_404
from django.urls import reverse
from django.core.files.storage import default_storage
from django.http import HttpResponse
from bookstore.models import new_book
from .models import Author
from .forms import AuthorForm
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


books = [
    {"id": 1, "name": "book 1", "price": 100, "author": "sara", "paper": 400, "image": "img1.jpg"},
    {"id": 2, "name": "book 2", "price": 150, "author": "arwa", "paper": 500, "image": "img2.jpg"},
    {"id": 3, "name": "book 3", "price": 100, "author": "mona", "paper": 600, "image": "img3.avif"}
]

def welcome(request):
    return render(request, 'welcome.html')

def landing(request):
    return render(request, 'landing.html', {'books': books})

def profile(request, id):
    book_detail = next((book for book in books if book['id'] == id), None)
    if book_detail:
        return render(request, 'profile.html', {'book': book_detail})
    else:
        return HttpResponse("Book not found")

def index(request):
    return HttpResponse(books)


def bookstore_index(request):
    bookstore = new_book.objects.all()
    return render(request, 'index.html', {'bookstore': bookstore})

def new_book_show(request, id):
    try:
        book = new_book.objects.get(id=id)
        return render(request, 'show.html', {'book': book})
    except new_book.DoesNotExist:
        return HttpResponse("Book not found")




def create_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        price = request.POST.get("price")
        pages = request.POST.get("pages")
        image = request.FILES.get("image")  # Use request.FILES to get the uploaded file

        # Save the image file to your media directory
        file_path = default_storage.save(image.name, image)

        mybook = new_book.objects.create(
            name=name,
            author=author,
            price=price,
            pages=pages,
            image=file_path  # Save the file path to the database
        )

        return redirect("bookstore_index")

    return render(request, 'create.html')


def book_delete(request,id):
    dbook = new_book.objects.get(id=id)
    dbook.delete()
    url = reverse("bookstore_index")
    return redirect(url)
    
def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'all_authors.html', {'authors': authors})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'author_detail.html', {'author': author})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_authors')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('all_authors')

# views.py

def book_edit(request, id):
    try:
        book = new_book.objects.get(id=id)
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES, instance=book)  # Pass instance to update existing book
            if form.is_valid():
                form.save()
                return redirect('bookstore_index')
        else:
            form = BookForm(instance=book)
        return render(request, 'edit.html', {'form': form})
    except new_book.DoesNotExist:
        return HttpResponse("Book not found")




def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)  # Pass instance to update existing author
        if form.is_valid():
            form.save()
            return redirect('author_detail', author_id=author_id)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'edit_author.html', {'form': form, 'author': author})




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('bookstore_welcome')  # Redirect to home page after successful registration
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('bookstore_index')  # Redirect to bookstore index after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('bookstore_welcome') 