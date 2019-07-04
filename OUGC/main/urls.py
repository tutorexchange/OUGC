from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("home/", views.homepage, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
     path("login/", views.login_request, name="login"),
     path("play/",views.play,name="play"),
     path("profile_update/",views.profile_update,name="profile_update"),
     path("tournaments/",views.tournaments,name="tournaments"),
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

