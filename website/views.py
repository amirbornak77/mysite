from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Contact
from django.views.decorators.csrf import csrf_protect
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')



# ...
@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        # Create a mutable copy of the POST data
        post_data = request.POST.copy()
        # Set the 'name' field to 'anonymous'
        post_data['name'] = 'anonymous'

        contact_form = ContactForm(post_data)

        if contact_form.is_valid():
            # Save the contact to the database with 'name' set to 'anonymous'
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
            
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket has not been approved')
            
    else:
        contact_form = ContactForm()

    return render(request, 'website/contact.html', {'contact_form': contact_form})



@csrf_protect
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to our newsletter!')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email address for newsletter subscription.')

    return HttpResponseRedirect(reverse('website:index'))  # Redirect to the homepage after submission

            

