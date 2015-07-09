from django.conf.urls import patterns, include, url
from django.contrib import admin


from tastypie.api import Api
from api.resources import NewsResource
from api.resources import BroadcastResource

v1_api = Api(api_name='v1')
v1_api.register(NewsResource())
v1_api.register(BroadcastResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
