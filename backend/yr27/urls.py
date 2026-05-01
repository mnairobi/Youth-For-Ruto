# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# admin.site.site_header = 'YR27 Administration'
# admin.site.site_title = 'YR27 Admin'
# admin.site.index_title = 'Youths for Ruto 2027 – Dashboard'

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('core.urls')),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({
        'status':  'ok',
        'service': 'YR27 Backend API',
        'version': '1.0.0',
        'message': '2027 – Ruto Tena. Youth Power. National Power.',
        'endpoints': {
            'api':      '/api/',
            'admin':    '/admin/',
            'counties': '/api/counties/',
            'leaders':  '/api/leaders/',
            'stats':    '/api/stats/',
        }
    })


admin.site.site_header  = 'YR27 Administration'
admin.site.site_title   = 'YR27 Admin'
admin.site.index_title  = 'Youths for Ruto 2027 – Dashboard'

urlpatterns = [
    path('',          health_check,                     name='health'),
    path('admin/',    admin.site.urls),
    path('api/',      include('core.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )