from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook_app/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        Contact.objects.create(
            name=name,
            surname=surname,
            phone_number=phone_number,
            address=address
        )

    return render(request, 'phonebook_app/add_contact.html')
