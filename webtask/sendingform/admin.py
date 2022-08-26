from django.contrib import admin
from . models import Feedback


#Класс отображающий указанные поля в панеле администратора
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'estimation') #Поля которые необходимо вывести
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'text', 'estimation') #Поля по которым необходимо осуществлять поиск
    list_filter = ('id', 'name', 'text', 'estimation') #Поля по которым необходимо осуществлять фильтрации

admin.site.register(Feedback, FeedbackAdmin) #Регистрация модели Feedback на сайте администрации
