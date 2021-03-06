from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),    
    url(r'^b$', hello.views.startbot, name='startbot'),
    url(r'^s$', hello.views.stopbot, name='stopbot'),
    path('admin/', admin.site.urls),
]
