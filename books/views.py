from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Publisher

class PublisherList(ListView):
    model = Publisher

