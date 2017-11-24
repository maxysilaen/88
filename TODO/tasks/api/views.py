from rest_framework.authentication import SessionAuthentication

from rest_framework import generics, mixins, permissions

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from .permissions import IsOwnerOrReadOnly

from .serializers import (
TaskListSerializer,
TaskCreateSerializer,
TaskUpdateSerializer

)
from tasks.models import TasksList



class TaskListAPIView(ListAPIView):
    # Call Serializers
    serializer_class = TaskListSerializer
    # Filter Option in List API
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]

    # Field yang ingin di filter
    search_fields = ['name_task', ]


    # Override queryset
    def get_queryset(self, *args, **kwargs):
        queryset_list = TasksList.objects.filter(created_by=self.request.user).order_by('-created_at')

        return queryset_list

class TaskCreateApiView(CreateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = TasksList.objects.all()
    permission_classes = [AllowAny]


class TaskDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    #queryset = Comment.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self, *args, **kwargs):
        queryset = TasksList.objects.filter(pk__gte=0)
        return queryset

    def put(self, request, *args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
