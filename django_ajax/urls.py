"""django_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from simple_ajax.views import UserSignUpView, ValidateUsername
from crud_ajax.views import CreateCrudUser, CrudView, DeleteCrudUser, UpdateCrudUser

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Front Page
    path('', TemplateView.as_view(template_name='front_page.html')),

    # Simple Ajax Example
    path('simpleajax/', UserSignUpView.as_view(), name='simple_ajax'),
    path('ajax/validate-username/', ValidateUsername.as_view(), name='simple_ajax_validate'),

    # Django Ajax CRUD Operations
    path('crud/', CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),

    # Chat
    path('chat', TemplateView.as_view(template_name='chat/chat_login.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
