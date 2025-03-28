
from django.urls import path 
from . import views
from .views import index
from .views import BookList, AddBook, DeleteBook



urlpatterns = [
    path('', index.as_view(), name='main-page'),
    path('book_list', BookList.as_view(), name='book_list'),
    path('add_book', AddBook.as_view() , name='add_book'),
    path('book_detail/<int:id>', views.book_detail, name='book-detail'),
    path('update_book/<int:id>', views.update_book, name='update_book'),
    path('delete_book/<int:id>/', DeleteBook.as_view(), name='delete_book'),
    path('tags/<slug:tag_slug>',views.books_by_tag_or_category_or_author, name='books-by-tag'),
    path('author/<slug:author_slug>',views.books_by_tag_or_category_or_author, name='books-by-author'),
    path('categories/<slug:category_slug>',views.books_by_tag_or_category_or_author, name='books-by-category')
   

]