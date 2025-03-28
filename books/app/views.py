from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookForm, UserForm
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, View, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class index(TemplateView):
    template_name = 'index.html'


 

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    
    #     context['authors'] = Author.objects.all()
    #     return context
       


# def main_page(request):
#     context = {
#         #'UserForm': UserForm
#     }
#     return render(request,'index.html',context)

# def book_list(request):
#     books = BookDetail.objects.all()
#     tags = Tags.objects.all()[:5]
#     categories = Categories.objects.all()[:5]
#     authors = Author.objects.all()[:5]
#     context = {
#         'books': books,
#         'tags': tags,
#         'categories': categories,
#         'authors': authors
#     }
#     return render(request,'books.html',context)

class BookList(LoginRequiredMixin,TemplateView):
    login_url = 'login'
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['books'] = BookDetail.objects.all()
        context['tags'] = Tags.objects.all()[:5]
        context['categories'] = Categories.objects.all()[:5]
        context['authors'] = Author.objects.all()[:3]

        return context



@login_required(login_url='login')
def book_detail(request,id):
    book = BookDetail.objects.get(id=id)
    book_category = book.category
    book_tags = book.tags.all()

    context={
        'book': book,
        'book_category': book_category,
        'book_tags': book_tags
    }
    return render(request,'book-detail.html', context)

@login_required(login_url='login')
def books_by_tag_or_category_or_author(request,tag_slug=None,category_slug=None, author_slug=None):
    tags = Tags.objects.all()[:5]
    categories = Categories.objects.all()[:5]
    authors = Author.objects.all()[:5]

    if tag_slug!=None:
        tag = Tags.objects.get(slug=tag_slug)
        books = tag.books.all()
    elif category_slug!=None:
        category = Categories.objects.get(slug=category_slug)
        books = category.books.all()
    elif author_slug!=None:
        author = Author.objects.get(slug=author_slug)
        books = author.books.all()


    context = {
        'books': books,
        'tags': tags,
        'categories': categories,
        'authors': authors
    }
    
   

    return render(request, 'books.html',context)



# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     context = {
#         'form': form
#     }
#     return render(request,'add-book.html', context)

class AddBook(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        print('get')
        form = BookForm()
        return render(request, 'add-book.html', {'form': form})
    
    def post(self, request):
        print('post')
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'add-book.html', {'form': form})

@login_required(login_url='login')
def update_book(request,id):
    book = get_object_or_404(BookDetail, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')

    form = BookForm(instance=book)
    context = {
        'form': form,
        'book': book
    }
    return render(request,'update_book.html', context)


# class BookCreateUpdateView(CreateView, UpdateView):
#     model = BookDetail
#     form_class = BookForm
#     template_name = "add-book.html"
#     success_url = reverse_lazy('book_list')

#     def get_object(self):
#         book_id = self.kwargs.get("id")
#         if book_id:
#             return get_object_or_404(BookDetail, id=book_id)
#         return None  
    

# def delete_book(request,id):
#     book = get_object_or_404(BookDetail,id=id)
#     if request.method=='POST':
#         book.delete()
#         return redirect('book_list')
    
#     context={
#         'book': book
#     }
#     return render(request,'delete-book.html',context)

class DeleteBook(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = BookDetail
    template_name = 'delete-book.html'
    success_url = reverse_lazy('book_list')

    
    def get_object(self):
        book_id = self.kwargs.get("id")
        print(self.kwargs)
        if book_id:
            return get_object_or_404(BookDetail, id=book_id)
        return None
    
    def get(self,request,*args,**kwargs):
        obj = self.get_object()
        context = {
            'book' :obj
        }

        return self.render_to_response(context)
    
    
    def post(self,request,*args,**kwargs):
        obj = self.get_object()
        obj.delete()


        return redirect(self.success_url)


# class ContactFormView(FormView):
#     template_name = "contact.html"
#     form_class = ContactForm
#     success_url = reverse_lazy('success')

#     def form_valid(self, form):
#         print("Məlumat:", form.cleaned_data)
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         print("Səhvlər:", form.errors)
#         return super().form_invalid(form) 
    

    
# Create your views here.
