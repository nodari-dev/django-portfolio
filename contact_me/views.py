from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import MessageForm
from .models import Message

def message_create(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'done.html')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)