from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

#If statement to check if the form is valid, if it is the subject will be pre-filled
#Django has a built-in form validation that cleans the data for you
#Will take in the user email and send the message to the website email

def contact_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'email', ['covidblogsreset@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request, "home.html")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})