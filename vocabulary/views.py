from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class testView(TemplateView):
	template_name = "test_index.html"