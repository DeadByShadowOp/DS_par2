from django.views.generic import TemplateView
from .models import *
from django.http import Http404

# Create your views here.


class RestaurantListView(TemplateView):
    template_name = "restaurants.html"

    def get_context_data(self, **kwargs):
        context = super(RestaurantListView, self).get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.all()
        return context


class RestaurantView(TemplateView):
    template_name = "single.html"

    def get_context_data(self, **kwargs):
        context = super(RestaurantView, self).get_context_data(**kwargs)
        r = Restaurant.objects.filter(name=kwargs['restaurant'])
        if not r:
            raise Http404("Restaurant does not exist")
        r = r[0]
        context['restaurant'] = r
        context['plates'] = BasePlate.objects.filter(restaurant=r).all()
        return context
