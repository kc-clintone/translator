from django.urls import path
from .views import home, translate_text

urlpatterns = [
    path("", home, name="home"),
    path("api/v1/translate-text", translate_text),
]