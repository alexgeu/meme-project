import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
	#start_date = DateFilter(label="start_date", lookup_expr='gte')
	#end_date = DateFilter(label='end_date', lookup_expr='lte')
	
	title = CharFilter(label='title', lookup_expr='icontains')
	
	class Meta:
		model = Products
		fields = '__all__'
		exclude = ['user', 'liked', 'summary', 'description', 'start_date', 'end_date']
