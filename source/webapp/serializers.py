from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from webapp.models import Tasks


class TasksSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(read_only=True, view_name='tasks-detail')

    class Meta:
        model = Tasks
        fields = '__all__'
