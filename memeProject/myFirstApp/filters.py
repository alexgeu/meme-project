import django_filters
from django_filters import DateFilter, CharFilter
from .models import Meme


class OrderFilter(django_filters.FilterSet):
	# start_date = DateFilter(label="start_date", lookup_expr='gte')
	# end_date = DateFilter(label='end_date', lookup_expr='lte')
	
	title = CharFilter(label='title', lookup_expr='icontains')
	
	class Meta:
		model = Meme
		fields = '__all__'
		exclude = ['liked', 'image', 'user', 'caption']
