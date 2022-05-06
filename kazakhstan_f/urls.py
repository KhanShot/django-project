import imp
from django.urls import path
from kazakhstan_f import views
from kazakhstan_f.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('tours/', tours, name='tours'),
    path('contacts/', contacts, name='contacts'),

    path('blog/', blog, name='blog'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout, name='logout'),

    #######

    path('adm/', adm, name='adm'),
    path('adm/login', admLogin, name='adm.login'),
    path('adm/logout', admLogout, name='adm.logout'),

    path('adm/managers', managers, name='adm.managers'),
    path('adm/managers/create', managersCreate, name='adm.managersCreate'),
    path('adm/managers/edit/<slug:id>/', managersEdit, name='adm.managersEdit'),
    path('adm/managers/update/<slug:id>', managersUpdate, name='adm.managersUpdate'),
    path('adm/managers/delete/<slug:id>', managersDelete, name='adm.managersDelete'),
    path('adm/tours', toursBack, name='adm.tours'),
    path('adm/tours/create', toursCreate, name='adm.toursCreate'),
    path('adm/tours/edit/<slug:id>', toursEdit, name='adm.toursEdit'),
    path('adm/tours/update/<slug:id>', toursUpdate, name='adm.toursUpdate'),
    path('adm/tours/delete/<slug:id>', toursDelete, name='adm.toursDelete'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)