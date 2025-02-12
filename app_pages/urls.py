from tkinter.font import names

from django.urls import  path


from app_pages.views import HomeTemplateView,ProductListTemplateView,ContactTemplateView,UserRegisterTemplateView

app_name = 'app_pages'

urlpatterns = [
    path('products/',ProductListTemplateView.as_view(),name='product'),
    path('contacts/',ContactTemplateView.as_view(),name="contact"),
    path('', HomeTemplateView.as_view(), name='home'),
    path('users/',UserRegisterTemplateView.as_view(), name='user')
]