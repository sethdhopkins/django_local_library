from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_bookInstances_available': num_bookInstances_available,
        'num_authors': num_authors,
        'num_titles_word': num_titles_word,
        'num_genres_word': num_genres_word,
        'num_visits' : num_visits,
    }

    #Renders the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

    paginate_by = 4

    #context_object_name = 'book_list' #name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='Frameworks') [:5] #Gets 5 books containing 'Frameworks'
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

class BookDetailView(generic.DetailView):
    model = Book

#Or pass in BookDetails without the generic class
# def book_detail_view(request, primary_key):
#     try:
#         book = Book.objects.get(pk=primary_key)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')

#     return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorListView(generic.ListView):
    model = Author

    paginate_by = 3