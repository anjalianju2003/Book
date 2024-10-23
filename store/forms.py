from django import forms

from store.models import Book

class BookForm(forms.Form):

    name=forms.CharField()

    author=forms.CharField()

    price=forms.IntegerField()

    genre_type=forms.ChoiceField(choices=Book.genre_options)

     













