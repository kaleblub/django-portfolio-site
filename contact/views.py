from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def contact(request):
	if request.method == "GET":
		form = ContactForm()

	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			print('The form is valid')
			name = form.cleaned_data["name"]
			subject = form.cleaned_data["subject"]
			from_email = form.cleaned_data["email"]
			message = form.cleaned_data["message"]

			html = render_to_string('emails.html', {
				'name': name,
				'email': from_email,
				'subject': subject,
				'message': message,
				})

			try:
				send_mail(subject, message, from_email, [os.getenv('EMAIL_ADDRESS')], html_message=html)
				print("mail sent")
			except BadHeaderError:
				print("badheader")
				return HttpResponse("Invalid header found.")
			return redirect("contact")
	return render(request, "contact/contact.html", {"form": form})

def successView(request):
	return HttpResponse("Success! Thank you for your message.")