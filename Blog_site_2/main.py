""" Biz bu darsda yangi post qo`shish, uni tahrirlash va o`chirish ni ko`ramiz """

""" Yangi post qo`shish uchun CreateView dan foydalanamiz """

""" blog app ni ichidagi views.py faylini ochamiz va CreateView ni chaqiramiz """

# from django.views.generic.edit import CreateView
# from .models import Post
#
#
# class BlogCreateView(CreateView):
#     model = Post
#     template_name = 'create.html'
#     fields = ['title', 'author', 'text']


""" blog app ichidagi urls.py ga qo`shamiz """

# from .views import BlogCreateView
#
# urlpatterns = [
#     path('post/create/', BlogCreateView.as_view(), name='create'),
# ]

""" templates papkasiga 'create' html fayl ochamiz va ichiga quyidagilarni yozamiz """

# {% extends 'base.html' %}
# {% block content %}
#   <h2> Yangi Post </h2>
#   <form action="" method="post">
#       {% csrf_token %}
#       {{ from.as_p }}
#       <input type="submit" value="Saqlash">
#   </form>
# {% endblock %}

""" Yangi post qo`shish tugmasini 'base.html' fayliga qo`shamiz """

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
# ==>  <footer>
#           <h2><a href="{% url 'create' %}">Yangi post qo`shish</a></h2>
#      </footer>    <==
# </body>
# </html>

""" blog app ni ichidagi 'models.py' fayliga o`zgartirish kiritamiz """

# from django.db import models
# ==> from django.urls import reverse <==

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
# ==> def get_absolute_url(self):
#         return reverse('detail', args=[str(self.pk)])    <==


""" Habarlarni(Post) ni tahrirlash """

""" templates ni ichidagi 'detail.html' fayliga o`zgartirish kiritamiz """

# {% extends 'base.html' %}
#
# {% block content %}
#     <div class="post-entry">
#         <h2>{{ post.title }}</h2>
#         <p>{{ post.text }}</p>
#     </div>
# ==> <a href="{% url 'edit' post.pk %}">Postni tahrirlash</a>  <==
# {% endblock %}


""" templates papkani ichiga 'edit' html fayl ochamiz va uni ichiga quyidagilarni yozamiz """

# {% extends 'base.html' %}
# {% block content %}
# </h2>Postni tahrirlash</h2>
#  <form action="" method="post">
#       {% csrf_token %}
#       {{ from.as_p }}
#       <input type="submit" value="Yangilash">
#   </form>
# {% endblock %}

""" blog app ichidagi 'views.py' fayliga UpdateView ni chaqirib olamiz """

# from django.views.generic.edit import CreateView, UpdateView
# from .models import Post

# class BlogUpdateView(UpdateView):
#     model = Post
#     template_name = 'edit.html'
#     fields = ['title', 'body']

""" blog app ni ichidagi urls.py fayliga yaratilgan UpdateView ni qo`shamiz """

# from .views import BlogCreateView, BlogUpdateView
#
# urlpatterns = [
#     path('post/create/', BlogCreateView.as_view(), name='create'),
#     path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='edit'),
# ]


""" Habarni(Post) ni o`chirish """

""" blog app ni ichidagi 'views.py' fayliga DeleteView ni chaqirib olamiz """

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Post
# from django.urls import reverse_lazy

# class BlogDeleteView(DeleteView):
#     model = Post
#     template_name = 'delete.html'
#     success_url = reverse_lazy('home')

""" templates papkani ichida 'delete' html fayl yaratamiz va uni ichiga quyidagilatni yozamiz """

# {% extends 'base.html' %}
# {% block content %}
# </h2>Postni o`chirish</h2>
#  <form action="" method="post">
#       {% csrf_token %}
#       <p>"{{ post.title }}" postni o`chiraymi?</p>
#       <input type="submit" value="O`chirish">
#   </form>
# {% endblock %}

""" templates papkani ichida 'detail.html' faylini ichiga o`chirish tugmasini qoshamiz """

# {% extends 'base.html' %}
#
# {% block content %}
#     <div class="post-entry">
#         <h2>{{ post.title }}</h2>
#         <p>{{ post.text }}</p>
#     </div>
#   <a href="{% url 'edit' post.pk %}">Postni tahrirlash</a>
#  ==>  <a href="{% url 'delete' post.pk %}">Postni O`chirish</a>  <==
# {% endblock %}


""" blog app ni ichidagi 'urls.py' fayliga yaratilgan view ni qo`shamiz """

# from .views import BlogCreateView, BlogUpdateView, BlogDeleteView

# urlpatterns = [
#     path('post/create/', BlogCreateView.as_view(), name='create'),
#     path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='edit'),
#     ==> path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete') , <==
# ]