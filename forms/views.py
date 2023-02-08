from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def homepage(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'phone': form.cleaned_data['phone'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'gymnasium.sofia@gmail.com ', ['gymnasium.sofia@gmail.com ']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("sofia:homepage")
      
	form = ContactForm()
	return render(request, "index.html", {'form':form})

def complete(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())