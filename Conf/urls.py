from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('blogs/',include('app_blogs.urls',namespace='blogs')),
    # path('orders/', include('app_orders.urls', namespace='orders')),
    path('products/',include('app_products.urls',namespace='products')),
    path('', include('app_pages.urls', namespace='app_pages')),
)



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
