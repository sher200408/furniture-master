from django.views.generic import TemplateView, CreateView

from app_pages.forms import ContactModelForm
from app_pages.models import ContactModel


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class ProductListTemplateView(TemplateView):
    template_name = 'shop/products-list.html'

class ContactTemplateView(TemplateView):
    template_name = 'pages/contact.html'

class UserRegisterTemplateView(TemplateView):
    template_name = 'auth/user-register.html'


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    model = ContactModel
    success_url = '/contact'

    # def form_valid(self, form):
    #     pass
    #
    # def form_invalid(self, form):
    #     pass
    #
    #
    # def get(self,requ):