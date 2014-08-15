from django.shortcuts import render, render_to_response
from django.db.models import Q
from models import Book
from django.core.mail import send_mail
from myapp.forms import ContactForm
# Create your views here.

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains = query) |
			Q(authors__first_name__icontains = query) |
			Q(authors__last_name__icontains = query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response(template_name='books/search.html',dictionary = {
			'results': results,
			'query': query
		})


def contact(request):
	if request.method =='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			topic = data['topic']
			message = data['message']
			sender = data['sender']
#			send_mail(
#				message, sender, ['aguiarlima.roberto@gmail.com']
#			)
			print '***'
			print message
			print sender

	else:
		form = ContactForm()
	return render(request,'books/contact.html', {'form': form})
