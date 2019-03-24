from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views

from vehicles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('vehicles/', include("vehicles.urls")),
    # path('', include('vehicles.urls')),

    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='vehicles/password_reset.html'),
         name='password_reset'
         ),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='vehicles/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='vehicles/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='vehicles/password_reset_complete.html'),
         name='password_reset_complete'
         ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

# ] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
