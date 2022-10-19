from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from products import views as product_views

schema_view = get_schema_view(
   openapi.Info(
      title="Tech Store API",
      default_version='v1',
      description="API para la tienda de tecnología / Primer Experiencia IT",
      contact=openapi.Contact(email="javicerodriguez@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# TODO: Remove endpoints in this file and move them to products/urls.py
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('products/', product_views.ProductList.as_view()),
    path('products/<int:pk>/', product_views.ProductDetail.as_view()),
    path('categories/', product_views.CategoryList.as_view()),
    path('categories/<int:pk>/', product_views.CategoryDetail.as_view()),
]
