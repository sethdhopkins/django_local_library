from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """View function for home page of site."""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books
    num_bookInstances_available = BookInstance.objects.filter(status__exact = 'a').count()

    #The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #Queries the number of books that contain the word "Frameworks"
    num_titles_word = Book.objects.filter(title__icontains = 'Frameworks').count()

    #Queries the number of genres that contain the word "Fiction"
    num_genres_word = Genre.objects.filter(name__icontains = 'Fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_bookInstances_available': num_bookInstances_available,
        'num_authors': num_authors,
        'num_titles_word': num_titles_word,
        'num_genres_word': num_genres_word,
    }

    #Renders the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)