from django.conf.urls import url
from django.urls import reverse
from articles import views

urlpatterns = [
    url(r'^images/$', views.create_images, name="images"),
]
