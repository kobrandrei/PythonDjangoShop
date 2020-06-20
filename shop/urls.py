from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('registration/', userViews.register, name="reg"),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name='web/index.html'), name="exit"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
