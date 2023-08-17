from django.http.response import JsonResponse
from django.core.mail import send_mail

import os
import json
import requests
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import ArticleSerializer
from .models import Article


AUTH_USER = os.getenv('EMAIL_HOST_USER')
AUTH_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


def get_weather(request):
    """Отправляет запрос к api open-meteo и
    возвращает данные о погоде в саратове"""

    long = '46.0086'  # долгота Саратова
    lat = '51.5406'  # широта Саратова
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true'
    response = requests.get(url)
    weather_data = response.json()
    return JsonResponse(weather_data)


class SendEmailAPIView(APIView):
    """Реализует метод POST для отправки писем
    На вход принимает два параметра: адресант и текст письма"""

    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        message = data.get('message')
        send_mail(
                'тема письма',
                message,
                AUTH_USER,
                [email],
                fail_silently=False,
                auth_user=AUTH_USER,
                auth_password=AUTH_PASSWORD,
            )
        return Response({'status': 'success'})


class SortNumbersAPIView(APIView):
    """Реализует метод POST для сортировки массива.
    На вход дается массив чисел и индекс алгоритма сортировки, где
    1 - быстрая сортировка, 2 - пузырьковая, 3 - Timsort, 4 - вставками"""

    def post(self, request):
        numbers = request.data.get('numbers', [])
        algorithm = request.data.get('algorithm', None)

        if algorithm == 1:
            sorted_numbers = self.quick_sort(numbers)
        elif algorithm == 2:
            sorted_numbers = self.bubble_sort(numbers)
        elif algorithm == 3:
            sorted_numbers = sorted(numbers)
        elif algorithm == 4:
            sorted_numbers = self.insertion_sort(numbers)
        else:
            return Response({'error': 'Invalid algorithm'}, status=400)

        return Response({'sorted_numbers': sorted_numbers}, status=200)

    def quick_sort(self, numbers):
        if len(numbers) <= 1:
            return numbers
        else:
            pivot = numbers[0]
            less = [x for x in numbers[1:] if x <= pivot]
            greater = [x for x in numbers[1:] if x > pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def bubble_sort(self, numbers):
        n = len(numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers

    def insertion_sort(self, numbers):
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i - 1
            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = key
        return numbers


class ArticleListCreateView(generics.ListCreateAPIView):
    """Реализует методы GET для получения
    всех статей и POST для создания новой статьи"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Реализует методы PUT DELETE и
    GET для получения конкретной статьи"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
