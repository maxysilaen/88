import requests
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin, View
from .models import TasksList
# Create your views here.
class MyTasksListView(LoginRequiredMixin,TemplateResponseMixin, View):
    template_name = "tasks/my_tasks_list.html"

    def get(self, request, *args, **kwargs):
        # print request.Session()
        url = "http://localhost:8001/api/tasks/task-list/"
        r = requests.get(url)
        print r.text
        if r.status_code == 200:
            r_json = r.json()
            object_list = r_json

        return self.render_to_response({'object_list': object_list,})

    # [
    #     {
    #         "name_task": "Goreng",
    #         "description": "Goreng Ayam",
    #         "created_by": "maxysilaen",
    #         "created_at": "2017-11-23T10:16:16.711561Z",
    #         "updated_at": "2017-11-23T10:16:16.711586Z"
    #     },
    #     {
    #         "name_task": "Bakar",
    #         "description": "Bakar Makanan",
    #         "created_by": "maxysilaen",
    #         "created_at": "2017-11-23T10:15:43.588889Z",
    #         "updated_at": "2017-11-23T10:15:43.588918Z"
    #     }
    # ]
