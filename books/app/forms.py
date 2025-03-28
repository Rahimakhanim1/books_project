from django import forms
from .models import BookDetail,Author, Tags, Categories

class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = [ 'title','author','tags','category','price','publisher_date','on_sale','description','img']


        title = forms.CharField(
            widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Kitabin adini daxil edin'}),
            required=True
            
        )
        author = forms.ModelChoiceField(
            queryset=Author.objects.all(),
            widget=forms.Select(attrs={'class': 'form-select'}),
            required=True
        )
        tags = forms.ModelMultipleChoiceField(
            queryset=Tags.objects.all(),
            widget=forms.SelectMultiple(attrs={'class': "form-select"}),
            required=True
        )
        img = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            required=True
        )
        category = forms.ModelChoiceField(
            queryset=Categories.objects.all(),
            widget=forms.Select(attrs={'class': 'form-select'}),
            required=True
        )
        price=forms.IntegerField(
            widget=forms.NumberInput(attrs={'class': 'form-control','min': 1700, 'max': 2025}),
            required = False
        )
        on_sale = forms.BooleanField(
            widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            required=False
        )
        description=forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': "Kitabin tesvirini daxil edin"}),
            required=False
        )



class UserForm(forms.Form):
    username = forms.CharField(max_length=50,required=True,label='Ad')
    email = forms.EmailField(required=True, label='Soyadiniz',widget=forms.EmailInput(attrs={'placeholder': 'Email daxil et','class': 'input'}))
    