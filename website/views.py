from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Error')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})