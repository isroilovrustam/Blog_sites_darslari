""" Biz bu darsimizda  foydalanuvchilar sayitimizdan ro`yxatdan o`tishi uchun kodlar yozamiz """


""" Asosiy config ni ichidagi urls.py fayliga yangi path qo`shamiz """

# urlpatterns = [
#     path('account/', include('django.contrib.auth.urls')),
# ]

""" templates papkani ichida yana bita 'registration' degan papka yaratamiz 
 va shu papkani ichida 'login' nomli html fayl ochamiz """

""" login.html faylni ichiga """

# {% extends 'base.html' %}
# {% block content %}
#   <h2>Saytga kirish</h2>
#   <form method="post">
#       {% csrf_token %}
#       {{ form.as_p }}
#       <button type="submit">Kirish</button>
# </form>
# {% endblock %}

""" config papkani ichidagi settings.py faylining ohiriga manashu kodni yozamiz """

# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

""" templates papka ni ichida gi base.html fayliga o`zgartirish kiritamiz """

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
#  ==>  {% if user.is_authenticated %}
#       <p>Xush kelibsiz! {{ user.username }}</p>
#       <p><a href="{% url 'logout' %}">Chiqib ketish</a></p>
#    {% else %}
#       <p>
#       <a href="{% url 'login' %}">Sytga kirish</p> |
#       <a href="{% url 'signup' %}">Ro`yxatdan o`tish</a>
#        </p>
#    {% endif %}   <==
# <div>
#   {% block content %}
#   {% endblock %}
# </div>
# ==>  <footer>
#           <h2><a href="{% url 'create' %}">Yangi post qo`shish</a></h2>
#      </footer>    <==
# </body>
# </html>

""" Ana endi foydalanuvchilar saytimizdan ro`yxatdan o`tishi 
    Foydalanuvchilarni accountidan foydalanish uchun yangi app ochamiz"""

""" Terminalda manashu kodni yozamiz """

# ./manage.py startapp accounts

""" Endi bu app ni settings.py faylidagi app larga qo`shib qo`yamiz"""

""" config papkani ichidagi urls.py fayliga o`zgartirish qo`shamiz """

# urlpatterns = [
#     path('accounts/', include('django.contrib.auth.urls')),
# ==>  path('accounts/', include('accounts.urls')), <==
# ]

""" accounts app ni ichiga urls.py fail ochamiz va uni ichiga quyidagi narsalarni qo`shamiz """

# from django.urls import path
# from .views import SignUpView
#
# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
# ]

""" accounts app ni ichiga views.py fail ochamiz va uni ichiga quyidagi narsalarni qo`shamiz """

# from django.contrib.auth.forms import UserCretionForm
# from django.urls import reverse_lazy
# from django.views import generic
#
# class SignUpView(generic.CreateView):
#     form_class = UserCretionForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

""" templates papkani ichidagi registration papkani ichiga signup html fayl ochamiz va uni ichiga quyidagi kodlarni yozamiz """

# {% extends 'base.html' %}
# {% block content %}
#   <h2>Ro`yxatdan o`tish</h2>
#   <form method="post">
#       {% csrf_token %}
#       {{ form.as_p }}
#       <button type="submit">Ro`yxatdan o`tish</button>
# </form>
# {% endblock %}
