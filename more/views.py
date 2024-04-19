import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import FormsRegisterForm
from django.shortcuts import get_object_or_404, render, redirect,HttpResponseRedirect
from .forms import FormsRegisterForm, ProductForm, EmailRegisterForm, ReviewForm
from .models import Product, Review
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe
from .models import VIPStatus  
from .models import VIPStatus
import ssl
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods




def home(request):
    reviews = Review.objects.all()
    place = Map(location=[39.770476, 64.445147], zoom_start=17)
    Marker(location=[39.770476, 64.445147], icon=Icon(color='gray')).add_to(place)
    
    place_html = place._repr_html_()
    return render(request, 'home.html', {'reviews': reviews,'place_html': place_html})




def about(request):
    return render(request, 'about.html')


def login(request):
    products = Product.objects.all()

    total_price = sum(product.price for product in products)

    regions = set(product.region for product in products)

    context = {
        'products': products,
        'total_price': total_price,
        'regions': regions,
    }

    return render(request, 'key.html', context)


def politica(request):
    return render(request, 'politica.html')




def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'home.html', {
        'reviews': reviews
    })


def chocolate(request):
    products = Product.objects.all()
    return render(request, 'chocolate.html', {
        'products': products
    })



def contact(request):
    place = Map(location=[39.770476, 64.445147], zoom_start=17)
    Marker(location=[39.770476, 64.445147], icon=Icon(color='gray')).add_to(place)
    
    place_html = place._repr_html_()
    return render(request, 'contact.html', {'place_html': place_html} )


def testimonial(request):
    reviews = Review.objects.all() 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('more:testimonial')
    else:
        form = ReviewForm()
    return render(request, 'testimonial.html', {
        'form': form,
        'reviews': reviews 
    })





def submit_form(request):
    if request.method == 'POST':
        form = FormsRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp_server:
                smtp_server.starttls(context=ssl_context)
                smtp_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

                msg = MIMEMultipart()
                msg['From'] = settings.EMAIL_HOST_USER
                msg['To'] = 'jumanyyazowayhan32@gmail.com'
                msg['Subject'] = 'Contact Form Submission'

                body = f'Full Name: {full_name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'
                msg.attach(MIMEText(body, 'plain'))

                smtp_server.send_message(msg)

            return HttpResponseRedirect('/')
    else:
        form = FormsRegisterForm()

    play_sound = True
    return render(request, 'error.html', {'form': form, 'play_sound': play_sound})




def product_form(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        messages.success(request, 'Продукт успешно добавлен!')
    else:
        form = ProductForm()
    play_sound = True 
    return render(request, 'error.html', {'form': form, 'play_sound': play_sound})


def email_form(request):
    if request.method == "POST":
        form = EmailRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('more:home')
    else:
        form = EmailRegisterForm()
    play_sound = True 
    return render(request, 'error.html', {'form': form, 'play_sound': play_sound})


def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.save()
            else:
                Review.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            return redirect('more:home')  
        messages.success(request, 'Отзыв успешно опубликован!')
    else:
        form = ReviewForm()
    play_sound = True 
    return render(request, 'error.html', {'form': form, 'play_sound': play_sound})


def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def log(request):
    return render(request, 'log.html')



# сделал Айхан


def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


@login_required  
def buy_vip(request):
    return render(request, 'buy_vip.html')

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import VIPStatus

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = 1000 
        if not token:
            return JsonResponse({'error': 'Invalid token'})
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'VIP статус',
                            },
                            'unit_amount': amount * 100,  
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('success_view')) + '?session_id={CHECKOUT_SESSION_ID}',  # URL для успешной оплаты
                cancel_url=request.build_absolute_uri(reverse('profile')),  
            )
            messages.success(request, 'Оплата успешно прошла!')
            return JsonResponse({'sessionId': checkout_session['id']})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'})


from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.http import HttpRequest
from .models import VisitCounter

@login_required
def success_view(request):
    user = request.user

    success = request.GET.get('success')
    vip_status, created = VIPStatus.objects.get_or_create(user=user)
    vip_status.is_vip = True
    vip_status.save()

    visit_counter, created = VisitCounter.objects.get_or_create(id=1)
    visit_counter.count += 1
    visit_counter.save()

    return render(request, 'success.html', {
        'visit_count': visit_counter.count,
        'is_vip': vip_status.is_vip,
    })



from django.http import HttpResponse


def set_cookie(request):
    response = HttpResponse("Cookie set")
    response.set_cookie('user_cookie', 'cookie_value', max_age=3600) 
    return response

def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('user_cookie')
    return response


def show_cookie(request):
    if 'my_cookie' in request.COOKIES:
        return HttpResponse(f"Value of my_cookie is: {request.COOKIES['my_cookie']}")
    else:
        return HttpResponse("No cookie found.")

def cookie_policy(request):
    return render(request, 'cookie_policy.html')

def cok(request):
    return render(request, 'cok.html')

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DinoSettings

def pashalka(request):
    return render(request, 'pashalka.html')

@csrf_exempt
def change_dino_color(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        DinoSettings.objects.update_or_create(id=1, defaults={'color': color})
        return JsonResponse({'status': 'success', 'color': color})
    return JsonResponse({'status': 'error'})


@login_required
def profile_view(request):
    return render(request, "profile.html")

@login_required
def profile1(request):
    return render(request, "profile.html")


from folium import Map, Marker, Icon

def karta(request):
    place = Map(location=[39.770476, 64.445147], zoom_start=17)
    Marker(location=[39.770476, 64.445147],
           icon=Icon(color='gray')).add_to(place)
    place_html = place._repr_html_()
    return render(request, 'karta.html', {'place_html': place_html})
