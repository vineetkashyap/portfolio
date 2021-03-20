from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Product
# Create your models here.
def index(request):
    pics = Product.objects.all()
    return render(request,'index.html',{'pics':pics})

def product_detail(request):
    return render(request,'portfolio-details.html')


def emailsend(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']  
    context={'name':name,'email':email,'subject':subject,'message':message}
    template = render_to_string('email.html',context)
    email = EmailMessage(
        subject,
        template,
        email,
        [settings.EMAIL_HOST_USER],
    )
    email.fail_silently=False
    email.send()
    return redirect("index")    