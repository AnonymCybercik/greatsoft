"""greatsoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from greatsoftapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",views.OverAll,name = "OverAll"), # barcha api urllari
    
    path("api/Blog-Create",views.BlogCreate,name = "BlogCreate"), #blog yaratish
    path("api/Blog-Update",views.BlogUpdate,name = "BlogUpdate"), #blogni yangilash
    path("api/Blog-Detail/<int:pk>",views.BlogDetail,name = "BlogDetail"), # alohida olingan blog
    path("api/Blog-Delete/<int:pk>",views.BlogDelete,name = "BlogDelete"), # blogni o'chirish
    path("api/Blog-List",views.BlogList,name = "BlogList"), #barcha bloglar
    
    path("api/Portfolio-Create",views.PortfolioCreate,name = "PortfolioCreate"), #portfolio yaratish
    path("api/Portfolio-Update",views.PortfolioUpdate,name = "PortfolioUpdate"), #portfolioni yangilash
    path("api/Portfolio-Detail/<int:pk>",views.PortfolioDetail,name = "PortfolioDetail"), # alohida olingan portfolio
    path("api/Portfolio-Delete/<int:pk>",views.PortfolioDelete,name = "PortfolioDelete"), # portfolioni o'chirish
    path("api/Portfolio-List",views.PortfolioList,name = "PortfolioList"), #barcha portfoliolar

    path("api/Contact-Create",views.ContactCreate,name = "ContactCreate"),#contact yaratish
    path("api/Contact-Update",views.ContactUpdate,name = "ContactUpdate"),#contactni yangilash
    path("api/Contact-Detail/<int:pk>",views.ContactDetail,name = "ContactDetail"),# alohida olingan contact
    path("api/Contact-Delete/<int:pk>",views.ContactDelete,name = "ContactDelete"),# contactni o'chirish
    path("api/Contact-List",views.ContactList,name = "ContactList"),#barcha contactlar


]