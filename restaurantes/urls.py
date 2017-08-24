from .views import *
from django.conf.urls import url
urlpatterns = [
      url(r'^$', RestaurantListView.as_view()),
      url(r'^restaurantes/(?P<restaurant>\w{1,50})/', RestaurantView.as_view(), name='restaurant_detail'),
      url(r'^comprar/(?P<plate_id>\w{1,50})/', RestaurantView.as_view(),name='buy'),

]
