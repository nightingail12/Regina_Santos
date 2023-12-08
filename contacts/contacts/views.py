from django.shortcuts import render
from contacts.models import crudst
from django.contrib import messages

def contact_display(request):
    results = crudst.objects.all()
    return render(request, 'index.html', {'crudst': results})

def contact_insert(request):
    if request.method == "POST":
        if request.POST.get('contact_name') and request.POST.get('contact_email'):
            contact_saved = crudst()
            contact_saved.contact_name = request.POST.get('contact_name')
            contact_saved.contact_email = request.POST.get('contact_email')
            contact_saved.save()
            messages.success(request, '<contact_saved.contact_name> has been added.')
            return render(request,'new_contact.html')
    else:
        return render(request,'new_contact.html')
