from django.conf.urls import patterns, include, url
from django.contrib import admin

import djangomaster

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^master/', include(djangomaster.urls)),
)
