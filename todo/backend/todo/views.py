from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import TODO
from .serializers import TODOSerializer


class TODOViewSet(viewsets.ModelViewSet):
  queryset = TODO.objects.all()
  serializer_class = TODOSerializer
  filter_backends = [
    DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
  ]
  filterset_fields = ("title", "user", "is_complete")
  search_fields = ("title")
  OrderingFilter = ("is_complete", "created_at", "updated_at")