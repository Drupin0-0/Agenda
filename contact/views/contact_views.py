from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from contact.models import Contact


def index(request):
    single_contact = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20]

    context = {
        'contacts': single_contact,
        'site_title': 'Contatos -'
    }
    return render(
        request,
        'contact/index.html',
        context
    )
def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')
    
    single_contact = Contact.objects \
        .filter(show=True)\
        .filter (
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    context = {
        'contacts': single_contact,
        'site_title': 'Contatos -'
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
    )

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
    
