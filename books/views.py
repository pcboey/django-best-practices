from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from .models import Publisher, Book

class PublisherList(ListView):
    model = Publisher

class PublisherDetail(DetailView):

    model = Publisher

class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, slug=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context

class PublisherCreate(CreateView):
    model = Publisher
    template_name = 'books/publisher_create.html'
    fields = ['name', 'address', 'city', 'state_province', 'country', 'website']

    def form_valid(self, form):
        publisher = form.save(commit=False)
        name = form.cleaned_data['name']
        publisher.slug = name.split()[0]
        publisher.save()
        return super(PublisherCreate, self).form_valid(form)

class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'country', 'website']
    #success_url = reverse_lazy('publisher')

class PublisherDelete(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher-list')
