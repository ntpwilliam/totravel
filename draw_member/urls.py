from django.conf.urls import include, url
from .views import home  # explicit relative import

urlpatterns = [
    url(r'^$', home, name="home"),	
]