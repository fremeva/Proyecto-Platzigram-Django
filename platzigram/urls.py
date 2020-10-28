""" Platzigram URLs module. """

#Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)