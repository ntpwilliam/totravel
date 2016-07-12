from django.contrib import admin
from .models import Post, Sell_product # this is class

# Register your models here.
admin.site.register(Post)
admin.site.register(Sell_product)