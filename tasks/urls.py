from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views

# api versioning, that's why you can use v1 to versioning the API

router = routers.DefaultRouter()
router.register(r'task', views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title="Task API"))
]