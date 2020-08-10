# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this
]

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#
# Django 2
#
# # add this import
# from django.contrib.auth import views as auth_view
#
# ...
#
# # add this path
# path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
#     html_email_template_name='registration/password_reset_email.html'
# )),
# # just before
# path('accounts/', include('django.contrib.auth.urls')),
