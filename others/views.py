from django.shortcuts import render
from .models import About, Contact, Terms, Privacy, Faq, Part, Section

def about(request):
    about_data = About.objects.first()
    return render(request, 'others/about.html', {'about': about_data})

def contact(request):
    contact_data = Contact.objects.all()
    return render(request, 'others/contact.html', {'contacts': contact_data})

def terms(request):
    terms_data = Terms.objects.first()
    parts = Part.objects.filter(terms=terms_data)
    sections = Section.objects.filter(terms=terms_data)
    return render(request, 'others/terms.html', {
        'terms': terms_data,
        'parts': parts,
        'sections': sections
    })

def privacy(request):
    privacy_data = Privacy.objects.first()
    return render(request, 'others/privacy.html', {'privacy': privacy_data})

def faq(request):
    faqs = Faq.objects.all()
    return render(request, 'others/faq.html', {'faqs': faqs})