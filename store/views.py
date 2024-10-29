from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from store.forms import BookForm

from store.models import Book

from django.db.models import Q

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
            return redirect("book-list")

        return render(request,self.template_name,{"form":form_instance})

class BookListView(View):

   
    template_name="book_list.html"

    def get(self,request,*args,**kwargs):

        search_text=request.GET.get("filter")

        qs=Book.objects.all()

        all_name=Book.objects.values_list("name",flat=True).distinct()
        all_fuel_types=Book.objects.values_list("author",flat=True).distinct()
        all_owner_types=Book.objects.values_list("price",flat=True).distinct()
        all_records=[]
        all_records.extend(all_name)
        all_records.extend(all_fuel_types)
        all_records.extend(all_owner_types)
        print(all_records)
       

        if search_text:
             
            qs=qs.filter(

                Q(name__contains=search_text)|Q(author__contains=search_text)|

                Q(price__contains=search_text)
            )

        return render(request,self.template_name,{"data":qs,"records":all_records})
class BookDetailView(View):
    template_name="book_detail.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})

class BookDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Book.objects.get(id=id).delete()

        return redirect("book-list")

class BookUpdateView(View):

    template_name="book_update.html"

    form_class=BookForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        book_object=Book.objects.get(id=id)

        data={
            "name":book_object.name,
            "author":book_object.author,
            "price":book_object.price,
            "genre_type":book_object.genre_type
        }

        form_instance=self.form_class(initial=data)

        return render(request,self.template_name,{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        form_data=request.POST

        from_instance=self.form_class(form_data)

        if from_instance.is_valid():

            data=from_instance.cleaned_data

            Book.objects.filter(id=id).update(**data)

            return redirect("book-list")

        return render(request,self.template_name,{"form":from_instance})   
