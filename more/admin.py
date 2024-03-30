from django.contrib import admin
from .models import info, FormsRegister, Product, Review, EmailRegister

@admin.register(info)
class infoAdmin(admin.ModelAdmin):
    pass

@admin.register(FormsRegister)
class FromsRegisterAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(EmailRegister)
class EmailRegisterAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
