from django.shortcuts import render
from django.http import HttpResponse
from random import random
from .forms import SubscriberForm

def index(request):
    return HttpResponse('Hello world!')

def second(request):    
    '''функция second отвечает за отображение страницы - формы в html, которая содержит в себе модель subscriber. Если в этой форме нажать
    на кнопу submit, подействует post метод, который вернет заполненные поля модели subscriber '''

    #return HttpResponse('Second')

    context = {
        'name': 'Biba',
        'age': 20,
        'random': random(),
        'form': SubscriberForm(request.POST or None),
    }

    if request.method == 'POST' and context['form'].is_valid():
        '''Если POST запрос, то сохраняем значения полей модели, которые находятся в html'''
        #print(request.POST)
        print(context['form'].cleaned_data)

        new_form = context['form'].save()
    

    return render(request, 'landing/landing.html', context)