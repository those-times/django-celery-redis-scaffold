from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from celery.result import AsyncResult
from core.tasks import add


def index(request):
    res = add.delay(3, 5)
    print('async add:', res)
    return JsonResponse({'taskId': res.id, 'status': res.status }) 

def task(request, id):
    res = AsyncResult(id)
    return JsonResponse({'taskId': res.id, 'status': res.status })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<uuid:id>/', task),
    path('', index)
]
