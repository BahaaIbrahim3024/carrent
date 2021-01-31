from django.urls import path, re_path
from .views import CustomerList
app_name = 'customer'

urlpatterns = [
    re_path(r'^(?P<id>[0-9]+)/$', CustomerList.as_view(), name='details'),
    re_path(r'^(?P<id>[0-9]+)/update$', CustomerList.as_view(), name='update'),
    re_path(r'^(?P<id>[0-9]+)/delete$', CustomerList.as_view(), name='delete'),
    path('create', CustomerList.as_view(), name='create'),

]
