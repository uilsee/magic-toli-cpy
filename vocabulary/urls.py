from django.conf.urls import url, include
from .views import *

urlpatterns = [
	url(r'^test/$', testView.as_view(), name="test_view"),
]