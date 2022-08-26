from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm, FeedbackFilterForm


# Функция передачи данных из формы FeedbackFor
def send(request):
    error = ' '
    if request.method == 'POST':
        form = FeedbackForm(request.POST) #Создает объект на основе класса FeedbackForm
        if form.is_valid():
            form.save()
        else:
            error = "Введены некорректные данные"

    form = FeedbackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'sendingform/sendform.html', context) #Передает данных из представления в указанный шаблон


# Функция передачи данных из модели Feedback
def read(request):
    feedback = Feedback.objects.all()
    form = FeedbackFilterForm(request.GET)

    # Проверка полученных данных из формы FeedbackFilterForm на правильность
    if form.is_valid():
        if form.cleaned_data["name"]:
            feedback = feedback.filter(name=form.cleaned_data["name"]) #Фильтрует записи по полю name

        if form.cleaned_data["text"]:
            feedback = feedback.filter(text__contains=form.cleaned_data["text"]) #Фильтрует записи по полю текст

        if form.cleaned_data["estimation"]:
            feedback = feedback.filter(estimation=form.cleaned_data["estimation"])

        if form.cleaned_data["ordering_name"]:
            feedback = feedback.order_by(form.cleaned_data["ordering_name"]) #Сортирует записи по полю name

        if form.cleaned_data["ordering_estimation"]:
            feedback = feedback.order_by(form.cleaned_data["ordering_estimation"])

    return render(request, 'sendingform/readform.html', {'feedback': feedback, "form": form})