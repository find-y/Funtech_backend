from events.models import Event
from rest_framework.viewsets import ModelViewSet

from .serializers import EventSerializer

# from users.models import (Position, Experience, Specialization, Stack)


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# заготовки для энпоинта со списками в анкету
"""
class ProfileLists(APIView):

    def get(self, request):
        position_list = list(Position.objects.values_list("name", flat=True))
        experience_list = list(
            Experience.objects.values_list("name", flat=True)
        )
        specialization_list = list(
            Specialization.objects.values_list("name", flat=True)
        )
        stack_list = list(Stack.objects.values_list("name", flat=True))

        return Response(
            {
                "position": position_list,
                "experience_years": experience_list,
                "specialization": specialization_list,
                "stack": stack_list,
            }
        )

class ProfileLists(APIView):

    def get(self, request):
        position_list = Position.objects.all()
        experience_list = Experience.objects.all()
        specialization_list = Specialization.objects.all()
        stack_list = Stack.objects.all()

        position_serializer = PositionSerializer(position_list, many=True)
        experience_serializer = ExperienceSerializer(experience_list, many=True)
        specialization_serializer = SpecializationSerializer(
            specialization_list,
            many=True
        )
        stack_serializer = StackSerializer(stack_list, many=True)

        return Response(
            {
                "position": position_serializer.data,
                "experience_years": experience_serializer.data,
                "specialization": specialization_serializer.data,
                "stack": stack_serializer.data,
            }
        )
"""
