from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string

from .forms import ContactForm
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def contact(request):
	if request.method == "GET":
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		bot_trap_value = form.cleaned_data.get("bot_trap", "")
		if bot_trap_value:
			print("Bot submission detected")
			return HttpResponseRedirect(success_url)
		if form.is_valid():
			print('The form is valid')
			name = form.cleaned_data["name"]
			subject = form.cleaned_data["subject"]
			from_email = form.cleaned_data["email"]
			message = form.cleaned_data["message"]

			# Ready the contact_email to be sent
			contact_html = render_to_string('contact_email.html', {
				'name': name,
				'email': from_email,
				'subject': subject,
				'message': message,
				})

			confirmation_html = render_to_string('confirmation_email.html', {
				'name': name,
				'email': from_email,
				'subject': subject,
				'message': message,
				'my_email': os.getenv('EMAIL_ADDRESS'),
				})

			# Try to send the contact email and then send confirmation email to the person
			try:
				send_mail(subject, message, from_email, [os.getenv('EMAIL_ADDRESS')], html_message=contact_html)
				print("Contact email sent")
				send_mail("Kaleb's Contact Form Confirmation Email", message, os.getenv('EMAIL_ADDRESS'), [from_email], html_message=confirmation_html)
				print("Confirmation email sent")
			except BadHeaderError:
				print("badheader")
				return HttpResponse("Invalid header found.")
			success_url = reverse("successView") + f"?name={name}&email={from_email}&subject={subject}&message={message}"
			return HttpResponseRedirect(success_url)
	return render(request, "contact/contact.html", {"form": form})

def successView(request):
	name = request.GET.get("name")
	email = request.GET.get("email")
	subject = request.GET.get("subject")
	message = request.GET.get("message")
	my_email = os.getenv('EMAIL_ADDRESS')

	return render(request, "contact/thank-you.html", {"name": name, "email": email, "subject": subject, "message": message, "my_email": my_email})