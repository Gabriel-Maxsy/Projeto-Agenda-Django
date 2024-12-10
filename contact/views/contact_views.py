from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id') # [10:20]  Fatiamento, estou pegando do contato 10 até mais 10 a frente.
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Create contact - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):                # Se o valor estiver vazio retornará ''
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) | # A letra "Q" faz com que seja possivel usar "or(|)"
            Q(last_name__icontains=search_value) | # A letra "Q" faz com que seja possivel usar "or(|)"
            Q(phone__icontains=search_value) | # A letra "Q" faz com que seja possivel usar "or(|)"
            Q(email__icontains=search_value)  # A letra "Q" faz com que seja possivel usar "or(|)"
        )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
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

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    
    return render(
        request,
        'contact/contact.html',
        context
    )