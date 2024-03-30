import smtpd
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect,HttpResponseRedirect
from .forms import FormsRegisterForm, ProductForm, EmailRegisterForm, ReviewForm
from .models import Product, Review
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Sum, Count
from .models import VIPStatus
import ssl

def home(request):
    reviews = Review.objects.all() 
    return render(request, 'home.html', {'reviews': reviews})


def about(request):
    return render(request, 'about.html')


def login(request):
    # Получаем список продуктов
    products = Product.objects.all()

    # Вычисляем общую стоимость всех продуктов
    total_price = sum(product.price for product in products)

    # Получаем уникальные регионы продуктов
    regions = set(product.region for product in products)

    # Подготавливаем контекст для передачи в шаблон
    context = {
        'products': products,
        'total_price': total_price,
        'regions': regions,
    }

    # Рендерим шаблон 'key.html' с переданным контекстом
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
    return render(request, 'contact.html')


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



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import FormsRegisterForm
import ssl

def submit_form(request):
    if request.method == 'POST':
        form = FormsRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Создаем контекст SSL и отключаем проверку сертификата
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            # Устанавливаем соединение с SMTP сервером
            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp_server:
                smtp_server.starttls(context=ssl_context)
                smtp_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

                # Создаем объект сообщения
                msg = MIMEMultipart()
                msg['From'] = settings.EMAIL_HOST_USER
                msg['To'] = 'jumanyyazowayhan32@gmail.com'
                msg['Subject'] = 'Contact Form Submission'

                # Добавляем текст сообщения в тело письма
                body = f'Full Name: {full_name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'
                msg.attach(MIMEText(body, 'plain'))

                # Отправляем письмо
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




# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from .models import VIPStatus

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from .models import VIPStatus

# @login_required
# def buy_vip(request):
#     if request.method == 'POST':
#         user = request.user
#         vip_status, created = VIPStatus.objects.get_or_create(user=user)
#         vip_status.is_vip = True
#         vip_status.save()

#         subject = 'Уведомление о покупке VIP-статуса'
#         message = f'{user.username} ({user.email}) купил VIP-статус.'
#         recipient_list = ['jumanyyazowayhan32@gmail.com']  # Замените на ваш адрес электронной почты

#         send_mail(subject, message, 'jumanyyazowayhan32@gmail.com', recipient_list, fail_silently=False)

#         return redirect('/')
    
#     return render(request, 'buy_vip.html')




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import VIPStatus  # Подставьте правильный импорт вашей модели VIPStatus

@login_required  # Декоратор, требующий аутентификации пользователя
def buy_vip(request):
    if request.method == 'POST':
        # Получаем текущего пользователя
        user = request.user

        # Получаем или создаем объект VIPStatus для текущего пользователя
        vip_status, created = VIPStatus.objects.get_or_create(user=user)

        # Обновляем статус на VIP
        vip_status.is_vip = True
        vip_status.save()

        return redirect('/')

    return render(request, 'buy_vip.html')



@login_required
def profile_view(request):
    return render(request, "profile.html")