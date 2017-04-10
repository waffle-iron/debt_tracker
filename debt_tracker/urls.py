from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^debug/', include('debug.urls')),
    # TODO uncomment when there are patterns in transaction.urls
    #url(r'^transaction/', include('transaction.urls')),
    url(r'^admin/', admin.site.urls),
]
