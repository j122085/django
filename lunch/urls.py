"""lunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
# from stores.views import store_list, store_detail
from pages.views import home


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    # url(r'^store/$', store_list, name='store_list'),
    # url(r'^store/(?P<pk>\d+)/$', store_detail,name='store_detail'), # 新增這行
    url(r'^store/', include('stores.urls')),
]
