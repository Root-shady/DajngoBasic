from django.conf.urls import url
from account import views
from django.urls import reverse

urlpatterns = [
    url(r'^home/$', views.HomePageView.as_view(), name="home"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^register/$', views.SignUpView.as_view(), name='signup'),
    #url(r'^logout/$', views.Logout.as_view(), name="logout"),
]
