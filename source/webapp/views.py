from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from webapp.models import Tasks
from webapp.serializers import TasksSerializer
from rest_framework.response import Response


class TasksModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def list(self, request, *args, **kwargs):
        objects = Tasks.objects.all()
        slr = TasksSerializer(objects, many=True, context={'request': request})
        return Response(slr.data)

    def create(self, request, *args, **kwargs):
        slr = TasksSerializer(data=request.data, context={'request': request})
        if slr.is_valid():
            task = slr.save()
            print(task)
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def retrieve(self, request, pk=None, *args, **kwargs):
        product = get_object_or_404(Tasks, pk=pk)
        slr = TasksSerializer(product, context={'request': request})
        return Response(slr.data)

    def update(self, request, pk=None, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=pk)
        slr = TasksSerializer(data=request.data, instance=task, context={'request': request})
        if slr.is_valid():
            task = slr.save()
            print(task)
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def destroy(self, request, pk=None, *args, **kwargs):
        product = get_object_or_404(Tasks, pk=pk)
        product.delete()
        return Response({'pk': pk})
