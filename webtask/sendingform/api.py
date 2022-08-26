from .models import Feedback
from rest_framework import viewsets, permissions
from .serializers import FeedbackSerializer


# Класс api позволяющий просматривать и редактировать отзывы
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FeedbackSerializer