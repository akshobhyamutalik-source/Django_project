"""
URL configuration for TeddyPups project.
Routes incoming web requests to the appropriate app.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

# Customizing Django Admin branding for TeddyPups U.A.E.
admin.site.site_header = "TeddyPups U.A.E. Administration"
admin.site.site_title = "TeddyPups Admin Portal"
admin.site.index_title = "Welcome to TeddyPups Management Portal"

urlpatterns = [
    # Admin dashboard URL
    path('admin/', admin.site.urls),

    # Main home page and info pages
    path('', include('home.urls')),

    # Puppy listings and details
    path('puppies/', include('puppies.urls')),

    # Customer enquiries and contact forms
    path('enquiries/', include('enquiries.urls')),

    # Universal media file serving (ensures puppy photos always load on live deployment)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
