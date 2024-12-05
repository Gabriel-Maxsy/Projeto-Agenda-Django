from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20] # Fatiamente, estou pegando do contato 10 até mais 10 a frente.

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )