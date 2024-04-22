from django.shortcuts import render,redirect
from django.views.generic import View
from works.forms import GenreForm,MovieForm
from works.models import Genre,Movie

# Create your views here.

class movieview(View):
    def get(self,request):
        form=MovieForm()
        return render(request,"addmovies.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            form=MovieForm()
            return render(request,"addmovies.html",{"form":form})
        else:
            return render(request,"addmovies.html",{"form":form})
        
class Genreview(View):
    def get(self,request):
        form=GenreForm()
        return render(request,"addmovies.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=GenreForm(request.POST)
        if form.is_valid():
            form.save()
            form=GenreForm()
            return render(request,"addgenre.html",{"form":form})
        else:
            return render(request,"addgenre.html",{"form":form})
        
class Genrelist(View):
    def get(self,request):
        res=Genre.objects.all()
        return render(request,"genlist.html",{"res":res})
    
# class Genredelete(View):
#     def get(self,request,**kwargs):
#         id=kwargs.get("pk")
#         Genre.objects.get(id=id).delete()
#         return redirect("list")
    
class Genrespecific(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        res=Genre.objects.get(id=id)
        return render(request,"genrespecific.html",{"res":res})
    
class Genreupdate(View):
    def get(self,request,**kwargs):
        k=kwargs.get("pk")
        res=Genre.objects.get(id=k)
        form=GenreForm(instance=res)
        return render(request,"genreedit.html",{"form":form})
    
    def post(self,request,**kwargs):
        k=kwargs.get("pk")
        res=Genre.objects.get(id=k)
        form=GenreForm(request.POST,instance=res)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
           return render(request,"genreedit.html",{"form":form})
        
class Movielist(View):
    def get(self,request):
        res=Movie.objects.all()
        return render(request,"movielist.html",{"res":res})
    
class Moviespecific(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        res=Movie.objects.get(id=id)
        return render(request,"moviespecific.html",{"res":res})
    
class Movieupdate(View):
    def get(self,request,**kwargs):
        k=kwargs.get("pk")
        res=Movie.objects.get(id=k)
        form=MovieForm(instance=res)
        return render(request,"movieedit.html",{"form":form})
    
    def post(self,request,**kwargs):
        k=kwargs.get("pk")
        res=Movie.objects.get(id=k)
        form=MovieForm(request.POST,instance=res)
        if form.is_valid:
            form.save()
            return redirect("list1")
        else:
            return render(request,"movieedit.html",{"form":form})
        
class Moviedelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("list1")


        


        

        

            


