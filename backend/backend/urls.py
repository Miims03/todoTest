
from django.contrib import admin
from django.urls import path , include , re_path
from rest_framework import routers 
from rest_framework.permissions import AllowAny , IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from private_storage import urls

from api.urls import routers as api_routers
from user_management.urls import router as user_management_router

from django.conf import settings 
from django.conf.urls.static import static

from api.views import helloWorld

schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Desc Todo API",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="amine.chr2@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(AllowAny,),
)

router = routers.DefaultRouter()
router.registry.extend(api_routers.registry)
router.registry.extend(user_management_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('hello/<str:name>', helloWorld),
    re_path('private-media/', include('private_storage.urls')),
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
