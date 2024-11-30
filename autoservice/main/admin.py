from django.contrib import admin
from .models import Profile
from .models import Product
from .models import Vacancy
from .models import Coupons
from .models import Contacts, Review, News, FAQ, Cart, CartItem,Order,OrderItem, Partner, Company
# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Vacancy)
admin.site.register(Coupons)
admin.site.register(Contacts)
admin.site.register(Review)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Partner)
admin.site.register(Company)