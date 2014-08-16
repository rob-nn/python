from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db.models import Q
from myapp.models import Book
# Create your views here.

def search(request):
	import pdb; pdb.set_trace()
	query = request.GET.get('q', '')
	if query:
		qset(
			Q(title__icontains = query) |
			Q(authors__first_name = query) |
			Q(authors__last_name = query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('books/search.html',
		{
			'results': results,
			'query': query
		})
