from django.test import TestCase
from main.models import Profile, Product, Cart, CartItem, Vacancy, Coupons, Contacts, News, Review, FAQ, Order, OrderItem
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.profile = Profile.objects.create(
            user=self.user,
            phone_number='123456789',
            id_user=123,
            address='Test Address',
            role='customer',
            orders=0,
            age=25
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00
        )
        
        self.cart = Cart.objects.create(
            user=self.user
        )
        
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=1
        )
        
        self.vacancy = Vacancy.objects.create(
            title='Test Vacancy',
            description='Test Description'
        )
        
        self.coupon = Coupons.objects.create(
            title='Test Coupon',
            description='Test Description',
            number='12345',
            active=True
        )
        
        self.contact = Contacts.objects.create(
            title='Test Contact',
            description='Test Description',
            phone_number='123456789',
            email='test@example.com'
        )
        
        self.news = News.objects.create(
            title='Test News',
            description='Test Description'
        )
        
        self.review = Review.objects.create(
            user=self.user,
            rating=5,
            text='Test Review'
        )
        
        self.faq = FAQ.objects.create(
            question='Test Question',
            answer='Test Answer'
        )
        
        self.order = Order.objects.create(
            user=self.user,
            address='Test Address',
            total_price=10.00
        )
        
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.phone_number, '123456789')
        self.assertEqual(self.profile.id_user, 123)
        self.assertEqual(self.profile.address, 'Test Address')
        self.assertEqual(self.profile.role, 'customer')
        self.assertEqual(self.profile.orders, 0)
        self.assertEqual(self.profile.age, 25)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.price, 10.00)

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 1)

    def test_vacancy_creation(self):
        self.assertEqual(self.vacancy.title, 'Test Vacancy')
        self.assertEqual(self.vacancy.description, 'Test Description')

    def test_coupons_creation(self):
        self.assertEqual(self.coupon.title, 'Test Coupon')
        self.assertEqual(self.coupon.description, 'Test Description')
        self.assertEqual(self.coupon.number, '12345')
        self.assertTrue(self.coupon.active)

    def test_contacts_creation(self):
        self.assertEqual(self.contact.title, 'Test Contact')
        self.assertEqual(self.contact.description, 'Test Description')
        self.assertEqual(self.contact.phone_number, '123456789')
        self.assertEqual(self.contact.email, 'test@example.com')

    def test_news_creation(self):
        self.assertEqual(self.news.title, 'Test News')
        self.assertEqual(self.news.description, 'Test Description')

    def test_review_creation(self):
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.text, 'Test Review')

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, 'Test Question')
        self.assertEqual(self.faq.answer, 'Test Answer')

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.address, 'Test Address')
        self.assertEqual(self.order.total_price, 10.00)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.quantity, 1)

class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

       
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.00)
        self.vacancy = Vacancy.objects.create(title='Test Vacancy', description='Test Description')
        self.coupon = Coupons.objects.create(title='Test Coupon', description='Test Description', number='12345', active=True)
        self.contact = Contacts.objects.create(title='Test Contact', description='Test Description', phone_number='123456789', email='test@example.com')
        self.news = News.objects.create(title='Test News', description='Test Description')
        self.review = Review.objects.create(user=self.user, rating=5, text='Test Review')
        self.faq = FAQ.objects.create(question='Test Question', answer='Test Answer')
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)
        self.order = Order.objects.create(user=self.user, address='Test Address', total_price=10.00)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=1)

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_news_view(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_faq_view(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)

    def test_contacts_view(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_policy_view(self):
        response = self.client.get('/policy/')
        self.assertEqual(response.status_code, 200)

    def test_catalogue_view(self):
        response = self.client.get('/catalogue/')
        self.assertEqual(response.status_code, 200)

    def test_vacancy_view(self):
        response = self.client.get('/vacancy/')
        self.assertEqual(response.status_code, 200)

    def test_review_list_view(self):
        response = self.client.get('/review/list/')
        self.assertEqual(response.status_code, 200)

    def test_coupons_view(self):
        response = self.client.get('/coupons/')
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)  

    def test_settings_view(self):
        response = self.client.get('/settings/')
        self.assertEqual(response.status_code, 200)

    def test_view_orders_view(self):
        response = self.client.get('/view_orders/')
        self.assertEqual(response.status_code, 200)

    def test_my_orders_view(self):
        response = self.client.get('/my_orders/')
        self.assertEqual(response.status_code, 200)

    def test_complete_order_view(self):
        response = self.client.post('/complete_order/', {'address': 'Test Address'})
        self.assertEqual(response.status_code, 302)  

    def test_add_to_cart_view(self):
        response = self.client.get(f'/add_to_cart/{self.product.id}/')
        self.assertEqual(response.status_code, 302)  

