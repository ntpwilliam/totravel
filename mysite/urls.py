"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from draw_member import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.second, name="second"), # for template page
	#url(r'^[A-Za-z0-9]*/$', views.math, name="math"), # for template page
	url(r'^draw_member/', include('draw_member.urls')), #for accont page
	url(r'^search_form/$', views.search_form), # for template page
	url(r'^search/$', views.search),
	url(r'^home/$', views.home),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^addOne/$', views.addOne),
    url(r'^updateOne/$', views.updateOne),
    url(r'^刪除/$', views.刪除),
	url(r'^myimg/$', views.myimg), # still can't use
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
