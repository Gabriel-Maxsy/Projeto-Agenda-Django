from django.shortcuts import redirect, render
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            # form.save(commit= False) o commiit false faz com que o contato não seja salvo na base de dados. (assim podendo o manipular antes de salvar)
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'site_title': 'Create Contact - '
    }

    return render(
        request,
        'contact/create.html',
        context
    )