from django.contrib import admin
from django.urls import path, include
from tasks.views import daily_tasks_home, complete_task  # <-- Added complete_task here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', daily_tasks_home, name='home'), 
    
    # This URL captures the specific ID of the task you want to complete
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    
    path('university/', include('university.urls')),
    path('finance/', include('finance.urls')), 
]