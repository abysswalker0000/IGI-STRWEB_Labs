from django.urls import path
from django.conf.urls.static import static
from autoservice import settings
from . import views

urlpatterns = [ 
    path('login/', views.login, name ='login'),
    path('', views.index, name='index'),
    path('about/', views.about_view , name ='about'),
    path('news/', views.news , name ='news'),
    path('faq/', views.faq , name ='faq'),
    path('contacts/', views.contacts , name ='contacts'),
    path('policy/', views.policy , name ='policy'),
    path('vacancy/', views.vacancy , name ='vacancy'),
    path('review_list/', views.review_list , name ='review_list'),
    path('coupons/', views.coupons , name ='coupons'),
    path('register/', views.register , name ='register'),
    path('cataloge/', views.cataloge , name ='cataloge'),
    path('settings/', views.contacts_view , name ='settings'),
    path('create_review/', views.create_review , name ='create_review'),
    path('cart/', views.view_cart,name='view_cart'),
    path('popular_products/', views.popular_products,name='popular_products'),
    path('view_orders/', views.view_orders,name='view_orders'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('complete_order/', views.complete_order, name='complete_order'),
    path('news/<int:news_id>/', views.news_detail_view, name='news_detail'),
    path('cart/increase/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    # path('toggle_coupon/<int:coupon_id>/', views.toggle_coupon_status, name='toggle_coupon_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
