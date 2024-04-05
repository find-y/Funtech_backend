from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from events.models import (Event,)

from .serializers import (EventSerializer,)


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# class AllData(APIView):

    def get(self, request):
        skills_list = list(Skill.objects.values_list("name", flat=True))
        education_list = list(Education.objects.values_list("name", flat=True))
        payments_list = list(Payments.objects.values_list("name", flat=True))
        towns_list = list(Towns.objects.values_list("name", flat=True))
        # date = datetime.now().strftime("%Y-%m-%d")

        return Response(
            {
                "specialization": specialization_list,
                "towns": towns_list,
                # salary
                "experience": experience_list,
                "education": education_list,
                "skills": skills_list,
                "languages": languages_list,
                "languages_levels": languages_levels_list,
                "registration": registration_list,
                "occupation": occupation_list,
                "timetable": timetable_list,
                "mission": BOOLEAN_CHOICES,
                "bonus": BOOLEAN_CHOICES,
                "expectations": expectations_list,
                "date": date,
                "recruiter_count": RECRUITER_COUNT_CHOICES,
                "candidates_count": CANDIDATES_COUNT_CHOICES,
                "payments": payments_list,
                # award
            }
        )