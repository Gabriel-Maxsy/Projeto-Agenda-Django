from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20] # Fatiamento, estou pegando do contato 10 até mais 10 a frente.

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        #  pk faz a pesquisa nos contatos e o parametro é passado em 
        #  contact_id tanto no clique como o arquivo html mostra, 
        #  quanto passando direto na url do site como o arquivo urls mostra
    )

    site_title = f'{single_contact.first_name} {single_contact.last_name} '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    
    return render(
        request,
        'contact/contact.html',
        context
    )