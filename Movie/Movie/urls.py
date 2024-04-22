"""
URL configuration for Movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from works.views import movieview,Genreview,Genrelist,Genrespecific,Genreupdate,Movielist,Moviespecific,Movieupdate,Moviedelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movieview.as_view()),
    path('genre/', Genreview.as_view()),
    path('genre/list', Genrelist.as_view(),name="list"),
    # path('genre/<pk>/remove', Genredelete.as_view()),
    path('genre/<pk>', Genrespecific.as_view(),name="specific"),
    path('genre/<pk>/update', Genreupdate.as_view(),name="update"),
    path('movies/list', Movielist.as_view(),name="list1"),
    path('movies/<pk>', Moviespecific.as_view(),name="specific1"),
    path('movies/<pk>/update', Movieupdate.as_view(),name="update1"),
    path('movies/<pk>/delete', Moviedelete.as_view(),name="delete"),

]
