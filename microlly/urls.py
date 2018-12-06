from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('compte/', include('compte.urls')),
]

urlpatterns += staticfiles_urlpatterns()