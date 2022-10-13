""" Blog site yaratishni boshlaymiz birinchi dars """

# 1 => python3 -m venv venv
# 2 => source venv/bin/activate
# 3 => pip3 install django
# 4 => pip3 list
# 5 => django-admin startproject config .
# 6 => ./manage.py runserver
# 7 => ./manage.py startapp blog
# 8 => ./manage.py migrate

""" settings.py fayliga o`tib INTALLED_APPS ga yaratgan app ni qo`shamiz """

""" blog app ni ichida models.py ga model yozamiz """

from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=202)
#     author = models.ForeignKey(
#         'auth.User',
#         on_delete=models.CASCADE
#     )
#     text = models.TextField()
#
#     def __str__(self):
#         return self.title


""" blog app ni ichidagi admin.py ga admin panelda ko`rinish uchun malumot kiritamiz """

# from django.contrib import admin
# from .models import Post
#
# admin.site.register(Post)

""" blog app ni ichidagi views.py ga view yaratamiz """

# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Post


# class BlogListView(ListView):
#     model = Post
#     template_name = 'home.html'


""" Endi blog app ni ichida urls.py degan fayil yaratib olamiz va ichiga malumot qo`shamiz """

# from django.urls import path
# from .views import BlogListView
#
# urlpatterns = [
#     path('', BlogListView.as_view(), name='home'),
# ]

""" config ni ichigagi urls.py ga malumot qo`shamiz """

# from django.contrib import admin
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),     # <= manashu qatorni qo`shib qo`yamiz
# ]

""" Loyigamizni ichida templates degan papka yaratib olamiz """

# Papka ni yaratib olganimizgan so`ng manashu papkani setting.py ni ichiga qo`ship qo`yamiz

""" TEMPLATES ni ichiga yani 'DIRS':[BASE_DIR / 'templates'] """

""" Yaratgan templates papkamizni ichiga 'base' va 'home' html fayl yaratamiz """

""" base.html faylni ichiga """

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>AbRuIs Blog</title>
# </head>
# <body>
#    <header>
#       <h1><a href="{% url 'home'%}">AbRuIs Blog </a><h1>
#    </header>
# <div>
#   {% block content %}
#   {% endblock %}
# </div>
# </body>
# </html>

""" home.html faylni ichiga """

# {% extends 'base.html' %}
# {% block content %}
#   {% for post in object_list %}
#     <div class="post-entry">
#         <h2><a href="">{{ post.title }}</a></h2>
#         <p>{{ post.text}}</p>
#     </div>
#   {% endfor %}
# {% endblock %}


""" DetailView """

""" blog app ni ichidagi viewga DetailView qo`shamiz """

# from django.views.generic import ListView, DetailView
#
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'detail'

""" blog app ni ichdagi urls.py ga qo`shamiz """

# from .views import BlogListView, BlogDetailView
#
# urlpatterns = [
#     path('', BlogListView.as_view(), name='home'),
#     path('post/<int:pk>/' BlogDetailView.as_view(), name='detail ')
# ]


""" tremplates papkani ichida 'detail' html fayl ochamiz va ichiga """

# {% extends 'base.html' %}
#
# {% block content %}
#     <div class="post-entry">
#         <h2>{{ post.title }}</h2>
#         <p>{{ post.text }}</p>
#     </div>
# {% endblock %}

""" home.html ga deteilni ko`rsatib qo`yamiz """

# {% extends 'base.html' %}
# {% block content %}
#   {% for post in object_list %}
#     <div class="post-entry">
# ==>        <h2><a href="{% url 'deteil' post.pk %}">{{ post.title }}</a></h2>   <==
#         <p>{{ post.text}}</p>
#     </div>
#   {% endfor %}
# {% endblock %}
