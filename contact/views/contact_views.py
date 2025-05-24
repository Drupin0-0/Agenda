from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    filtro = request.GET.get('filtro', 'all')
    query = request.GET.get('query', '').strip()

    contacts = Contact.objects.filter(show=True)

    if query:
        if filtro == 'id':
            contacts = contacts.filter(id__icontains=query)
        elif filtro == 'nome':
            contacts = contacts.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        elif filtro == 'telefone':
            contacts = contacts.filter(phone__icontains=query)
        elif filtro == 'email':
            contacts = contacts.filter(email__icontains=query)
        else:
            contacts = contacts.filter(
                Q(id__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(phone__icontains=query) |
                Q(email__icontains=query)
            )

    contacts = contacts.order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
        'search_value': query,
        'selected_filter': filtro,
    }

    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': contact,
        'site_title': f'{contact.first_name} {contact.last_name} - ',
    }

    return render(request, 'contact/contact.html', context)

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact:index')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'site_title': 'Criar Contato - ',
    }

    return render(request, 'contact/create.html', context)


