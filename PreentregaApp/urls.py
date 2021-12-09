from django import template
from django.urls.conf import path
from .views import inicio, guitarras, cuerdas, mastil


urlpatterns=[
    path('', inicio, name='inicio'),
    path('guitarras/', guitarras, name='guitarras'),
    path('cuerdas/', cuerdas, name='cuerdas'),
    path('mastil/', mastil, name='mastil'),
]