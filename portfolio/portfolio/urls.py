
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('details/',views.product_detail,name='details'),
    path('email',views.emailsend,name='email'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
