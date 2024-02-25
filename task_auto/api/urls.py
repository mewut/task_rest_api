from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExecutorViewSet, TaskViewSet, create_task, update_task, destroy_task


router = DefaultRouter()
router.register(r'executors', ExecutorViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('create/', create_task),
    path('update/<int:pk>/', update_task),
    path('destroy/<int:pk>/', destroy_task),
]

