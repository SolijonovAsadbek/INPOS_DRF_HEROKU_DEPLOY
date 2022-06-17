from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, ProductViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categorys', CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='IN Point of Sale Django Rest Framework API',
        default_version='v1',
        description='This is INPOS system API Docs',
        terms_of_service='',
        contact=openapi.Contact(email="Solijonov Asadbek <solijonovasadbek25111999@gmail.com>"),
        license=openapi.License(name='')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]

# from product import views

# urlpatterns = [
# path('', views.apiOverview, name='apiOverview'),
# path('task-all/', views.taskAll, name='task-all'),
# path('task-detail/<int:pk>/', views.taskDetail, name='task-detail'),
# path('task-create/', views.taskCreate, name='task-create'),
# path('task-update/<int:pk>', views.taskUpdate, name='task-update'),
# path('task-delete/<int:pk>', views.taskDelete, name='task-delete'),
# ]
