import django_filters
from django_filters import DateFilter, CharFilter
from .models import Meme


class OrderFilter(django_filters.FilterSet):
	start = DateFilter(label='Start Date', field_name='timestamp', lookup_expr='gte')
	end_date = DateFilter(label='End Date',field_name='timestamp', lookup_expr='lte')
	
	title = CharFilter(label='Title', lookup_expr='icontains')
	
	class Meta:
		model = Meme
		fields = '__all__'
		exclude = ['liked', 'image', 'user', 'caption', 'category', 'timestamp']

