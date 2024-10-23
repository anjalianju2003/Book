from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from store.forms import BookForm

from store.models import Book

class BookView(View):
    
    template_name="book.html"

    form_class=BookForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():
            
            data=form_instance.cleaned_data

            print(data)

            Book.objects.create(**data)

        return render(request,self.template_name,{"form":form_instance})

class BookListView(View):

    template_name="book_list.html"

    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        return render(request,self.template_name,{"data":qs})