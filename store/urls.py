from django.contrib import admin
from django.urls import include, path
from account.views import aboutView, accountView, checkoutView, contactView, register, shopView, user_login
from store import settings
from account.views import PasswordChangeView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountView, name="account"),
    path('index.html', accountView, name="account"),
    path('about.html', aboutView, name="about"),
    path('contact.html', contactView, name="contact"),
    path('shop.html', shopView, name="shop"),
    path('checkout.html', checkoutView, name="checkout"),
    path('shop/', include('shop.urls')),
    path('showcase/', include('showcase.urls')),
    path('cart/', include('cart.urls')),

    # login and rigister #

    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
