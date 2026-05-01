from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'counties', views.CountyViewSet)
router.register(r'leaders', views.LeaderViewSet)
router.register(r'news-categories', views.NewsCategoryViewSet)
router.register(r'news', views.NewsArticleViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'gallery-categories', views.GalleryCategoryViewSet)
router.register(r'gallery', views.GalleryImageViewSet)
router.register(r'testimonials', views.TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('join/', views.MemberRegistrationView.as_view(), name='join'),
    path('contact/', views.ContactMessageView.as_view(), name='contact'),
    path('donate/', views.DonationView.as_view(), name='donate'),
    path('subscribe/', views.SubscriberView.as_view(), name='subscribe'),
    path('settings/', views.site_settings, name='settings'),
    path('stats/', views.stats, name='stats'),
]