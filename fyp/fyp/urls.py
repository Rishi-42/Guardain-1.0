from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('guardian.urls')),
    path('account/' , include('account.urls')),
    path('address/' , include('address.urls')),
    path('pharmacy/' , include('pharmacy.urls')),
    path('counsellor/' , include('counsellor.urls')),	
    path('froala_editor/', include('froala_editor.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('counselor/', include('counselor.urls')),
    path('blog/', include('blog.urls')),
    path('booking/', include('booking.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)