from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('about/', views.about, name='about'),
    path('chocolate/', views.chocolate, name='chocolate'),
    path('contact/', views.contact, name='contact'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('login/', views.login, name='key'),
    path('product_form/', views.product_form, name='product_form'),
    path('email_form/', views.email_form, name='email_form'),
    path('review_form/', views.review_form, name='review_form'),
    path('reviews/', views.review_list, name='review_list'),
    path('politica/', views.politica, name='politica'),
    path('product/<int:product_id>/', views.view_product, name='view_product'),
    path('log/', views.log, name='log'),
    path('buy_vip/', views.buy_vip, name='buy_vip'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('success/', views.success_view, name='success_view'),
    path('profile', views.profile_view, name="profile")

   ]





# Сделал Айхан