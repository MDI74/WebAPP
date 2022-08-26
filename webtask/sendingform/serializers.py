from rest_framework import serializers
from .models import Feedback


#Класс отвечающий за сериализацию данных, т.е преобразования данных в нативный тип в  Python
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__' #В сериалайзере создаются поля для обслуживания всех полей моделей