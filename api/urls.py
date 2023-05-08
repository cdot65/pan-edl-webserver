from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EDLEntryViewSet, edl_view

router = DefaultRouter()
router.register(r"edl-entries", EDLEntryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('edl/', edl_view, name='edl'),
]
