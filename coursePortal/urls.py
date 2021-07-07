from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views    #using buit-in authenticators
from django.conf.urls import include, url
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True)),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html', next_page='/login/')),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html')),
    url(r'^password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'), #not working as heroku doesn't have free smtp server
    path('api/', include(router.urls))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)