# views.py

from django.shortcuts import render
from contacts.models import crudst
from django.contrib import messages
from contacts.forms import contact_form

def contact_display(request):
    results = crudst.objects.all()
    return render(request, 'index.html', {'crudst': results})

def contact_insert(request):
    if request.method == "POST":
        if request.POST.get('contact_name') and request.POST.get('contact_email') or request.POST.get('contact_notes'):
            contact_saved = crudst()
            contact_saved.contact_name = request.POST.get('contact_name')
            contact_saved.contact_email = request.POST.get('contact_email')
            contact_saved.contact_notes = request.POST.get('contact_notes')
            contact_saved.save()
            messages.success(request, f'{contact_saved.contact_name} has been added.')
            return render(request,'new_contact.html')
    else:
        return render(request,'new_contact.html')


def contact_edit(request, contact_name):
    contact_details = crudst.objects.get(contact_name=contact_name)
    return render(request, 'edit.html', {"crudst": contact_details})

def contact_update(request, contact_name):
    contact_update = crudst.objects.get(contact_name=contact_name)
    form = contact_form(request.POST, instance=contact_update)
    if form.is_valid():
        form.save()
        messages.success(request, "Record has been updated.")
        return render(request, "edit.html", {"crudst": contact_update})

def contact_delete(request, contact_name):
    contact_delete = crudst.objects.get(contact_name=contact_name)
    contact_delete.delete()
    results = crudst.objects.all()
    return render(request, 'index.html', {"crudst": results})