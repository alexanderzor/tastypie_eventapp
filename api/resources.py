from tastypie.resources import ModelResource, Serializer
from models import New, Broadcast, Summary
from tastypie.constants import ALL, ALL_WITH_RELATIONS
import datetime
class NewsResource(ModelResource):
    class Meta:
        queryset = New.objects.all()
        allowed_methods = ['get']
        #The fields we want to show
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        #The fields we don't want to show
        excludes = ['resource_uri']
        serializer = Serializer(formats=['json'])
        limit = 200
        filtering = {
            'news': ALL,
            'date': ['gte', 'lt', 'gt', 'lte', 'exact'],
            'time': ['gte', 'lt', 'gt', 'lte', 'exact'],
            'title': ['exact', ],
            }


class BroadcastResource(ModelResource):
    class Meta:
        queryset = Broadcast.objects.all()
        allowed_methods = ['get']
        #The fields we want to show
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        #The fields we don't want to show
        excludes = ['resource_uri']
        serializer = Serializer(formats=['json'])
        limit = 200
        filtering = {
            'broadcast': ALL,
            'date': ['gte', 'lt', 'gt', 'lte', 'exact'],
            'time': ['gte', 'lt', 'gt', 'lte', 'exact'],
            'title': ['exact', ],
            }
    def dehydrate(self, bundle):
        bundle.data['online_date'] = Summary.objects.first().online_date
        #bundle.data['date'] = datetime.date.today()
        return bundle

