from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'YR27 Administration'
admin.site.site_title = 'YR27 Admin'
admin.site.index_title = 'Youths for Ruto 2027 – Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)